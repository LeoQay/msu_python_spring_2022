import threading
import socket
import sys
import argparse
import json
import signal
from collections import Counter
import urllib.request
from bs4 import BeautifulSoup


global_stop = [False]


def worker(num: int, top_k: int, info, locks, print_info):
    while True:
        locks[num].acquire()

        if global_stop[0]:
            return

        file_name = print_info['file']

        client = info[num]['client']

        # processing url
        url = info[num]['url']

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                text = resp.read().decode(encoding='utf-8')
            soup = BeautifulSoup(text, features='html.parser')
            stat = Counter(
                soup.get_text().split()
            ).most_common(top_k)
            str_stat = json.dumps(stat)

            client.sendall(str_stat.encode())
        except BaseException:
            print_info['lock'].acquire()
            if file_name == 'stdout':
                print('Server: error when processed:', url.strip(), end='\n\n')
            else:
                with open(file_name, 'a', encoding='utf-8') as file:
                    print('Server: error when processed:', url.strip(),
                          file=file, end='\n\n')
            print_info['lock'].release()
        finally:
            client.close()

        print_info['lock'].acquire()
        print_info['count'] += 1
        if file_name == 'stdout':
            print('Server: urls processed:', print_info['count'])
        else:
            with open(file_name, 'a', encoding='utf-8') as file:
                print('Server: urls processed:', print_info['count'], file=file)
        print_info['lock'].release()

        info[num]['client'] = None
        info[num]['url'] = None
        info[num]['free'] = True


def get_connect(sock, timeout=1.):
    sock.settimeout(timeout)
    while not global_stop[0]:
        try:
            conn, _ = sock.accept()
        except BaseException:
            pass
        else:
            return conn


def master(workers_amount: int, top_k: int, sock, out):
    print_info = {
        'count': 0,
        'lock': threading.Semaphore(1),
        'file': out
    }

    locks = [
        threading.Semaphore(0)
        for _ in range(workers_amount)
    ]

    info = [
        {'free': True, 'url': None, 'client': None}
        for _ in range(workers_amount)
    ]

    def sigint_handler(signum, frame):
        global_stop[0] = True
        for i in range(workers_amount):
            locks[i].release()

    signal.signal(signal.SIGINT, sigint_handler)

    threads = [
        threading.Thread(target=worker,
                         args=(i, top_k, info, locks, print_info),
                         daemon=True)
        for i in range(workers_amount)
    ]

    for thread in threads:
        thread.start()

    try:
        while True:
            conn = get_connect(sock)
            if conn is None:
                break
            free_num = None
            while free_num is None:
                for i in range(workers_amount):
                    if info[i]['free']:
                        free_num = i
                        break
            info[free_num]['free'] = False
            info[free_num]['url'] = conn.recv(1024).decode(encoding='utf-8')
            info[free_num]['client'] = conn
            locks[free_num].release()
    finally:
        sigint_handler(0, 0)

    print('wait')
    for thread in threads:
        thread.join()


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=7)
    parser.add_argument('-a', type=int, default=9080)
    return parser.parse_args(args=argv[1:]).__dict__


def main(argv, out_name):
    args = get_args(argv)

    sock = socket.socket()
    try:
        sock.bind(('', args['a']))
        sock.listen(1)
        master(args['w'], args['k'], sock, out_name)
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    main(sys.argv, 'stdout')
