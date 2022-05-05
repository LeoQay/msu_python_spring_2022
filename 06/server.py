import threading
import socket
import sys
import argparse
import json
from collections import Counter
import urllib.request
from bs4 import BeautifulSoup


def worker(num: int, top_k: int, info, locks, print_info, out):
    while True:
        locks[num].acquire()

        if info[num]['stop']:
            return

        client = info[num]['client']

        # processing url
        url = info[num]['url']

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            text = urllib.request.urlopen(req).read().decode(encoding='utf-8')
            soup = BeautifulSoup(text, features='html.parser')
            stat = Counter(soup.get_text().split()).most_common(top_k)
            str_stat = json.dumps(stat)

            client.sendall(str_stat.encode())
        except BaseException:
            print('Server: error when processed:', url.strip(), end='\n\n')
        finally:
            client.close()

        print_info['lock'].acquire()
        print_info['count'] += 1
        print('Server: urls processed:', print_info['count'])
        print_info['lock'].release()

        info[num]['client'] = None
        info[num]['url'] = None
        info[num]['free'] = True


def master(workers_amount: int, top_k: int, sock, out):
    info = [
        {'free': True, 'stop': False, 'url': None, 'client': None}
        for _ in range(workers_amount)
    ]

    print_info = {
        'count': 0,
        'lock': threading.Semaphore(1)
    }

    locks = [
        threading.Semaphore(0)
        for _ in range(workers_amount)
    ]

    threads = [
        threading.Thread(target=worker,
                         args=(i, top_k, info, locks, print_info, out),
                         daemon=True)
        for i in range(workers_amount)
    ]

    for thread in threads:
        thread.start()

    while True:
        conn, _ = sock.accept()
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


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=7)
    return parser.parse_args(args=argv[1:]).__dict__


def main(argv, out_name):
    args = get_args(argv)

    if out_name == 'stdout':
        out = sys.stdout
    else:
        out = open(out_name, 'w', encoding='utf-8')

    sock = socket.socket()
    try:
        sock.bind(('', 9080))
        sock.listen(1)
        master(args['w'], args['k'], sock, out)
    except KeyboardInterrupt:
        pass
    finally:
        out.close()
        sock.close()


if __name__ == "__main__":
    main(sys.argv, sys.stdout)
