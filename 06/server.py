import threading
import socket
import sys
import argparse
import urllib


def worker(num: int, top_k: int, info, locks: list[threading.Semaphore]):
    while True:
        locks[num].acquire()
        if info[num]['end']:
            return

        info[num]['conn'].close()


def master(workers_amount: int, top_k: int):
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)

    info = [
        {'free': True, 'stop': False, 'url': None, 'conn': None}
        for _ in range(workers_amount)
    ]

    locks = [
        threading.Semaphore()
        for _ in range(workers_amount)
    ]

    for i in range(workers_amount):
        locks[i].acquire()

    threads = [
        threading.Thread(target=worker, args=(i, top_k, info, locks),
                         daemon=True)
        for i in range(workers_amount)
    ]

    for th in threads:
        th.start()

    while True:
        conn, address = sock.accept()
        url = conn.recv(1024)
        free_num = None
        while free_num is None:
            for i in range(workers_amount):
                if info[i]['free']:
                    free_num = i
                    break
        info[free_num]['free'] = False
        info[free_num]['url'] = url
        info[free_num]['conn'] = conn
        locks[free_num].release()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, default=10)
    parser.add_argument('-k', type=int, default=7)
    return parser.parse_args(args=sys.argv[1:]).__dict__


def main():
    args = get_args()
    master(args['w'], args['k'])


if __name__ == "__main__":
    main()
