import threading
import socket
import sys
import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from collections import Counter


def worker(num: int, top_k: int, info, locks: list[threading.Semaphore]):
    while True:
        locks[num].acquire()

        if info[num]['stop']:
            return

        client = info[num]['client']

        # processing url
        url = info[num]['url']

        response = urlopen(url)
        text = response.read().decode()
        soup = BeautifulSoup(text, features='html.parser')
        stat = Counter(soup.get_text().split()).most_common(top_k)
        str_stat = json.dumps(stat)

        client.sendall(str_stat.encode())

        info[num]['client'] = None
        info[num]['url'] = None
        info[num]['free'] = True


def master(workers_amount: int, top_k: int, sock):
    info = [
        {'free': True, 'stop': False, 'url': None, 'client': None}
        for _ in range(workers_amount)
    ]

    locks = [
        threading.Semaphore(0)
        for _ in range(workers_amount)
    ]

    threads = [
        threading.Thread(target=worker, args=(i, top_k, info, locks), daemon=True)
        for i in range(workers_amount)
    ]

    for th in threads:
        th.start()

    while True:
        conn, address = sock.accept()
        url = conn.recv(1024).decode()
        free_num = None
        while free_num is None:
            for i in range(workers_amount):
                if info[i]['free']:
                    free_num = i
                    break
        info[free_num]['free'] = False
        info[free_num]['url'] = url
        info[free_num]['client'] = conn
        locks[free_num].release()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=7)
    return parser.parse_args(args=sys.argv[1:]).__dict__


def main():
    args = get_args()
    try:
        sock = socket.socket()
        sock.bind(('', 9080))
        sock.listen(1)

        master(args['w'], args['k'], sock)
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    main()
