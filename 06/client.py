import threading
import socket
import argparse
import sys
from collections import deque


def thread_client(urls: deque[str], urls_lock, print_lock):
    while True:
        urls_lock.acquire()
        if len(urls) == 0:
            urls_lock.release()
            return

        url = urls.popleft()
        urls_lock.release()

        sock = socket.socket()
        sock.connect(('', 9080))
        sock.sendall(url.encode(encoding='utf-8'))
        data = sock.recv(100000).decode(encoding='utf-8')

        print_lock.acquire()
        print('{0}:\n{1}\n'.format(url.strip(), data.strip()))
        print_lock.release()

        sock.close()


def client(m, text):
    # shared resource
    urls = deque([url for url in open(text)])
    urls_lock = threading.Semaphore(1)
    print_lock = threading.Semaphore(1)

    threads = [
        threading.Thread(target=thread_client, args=(urls, urls_lock, print_lock))
        for _ in range(m)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(type=int, dest='m', default=10)
    parser.add_argument(type=str, dest='text', default='urls.txt')
    return parser.parse_args(args=sys.argv[1:]).__dict__


def main():
    args = get_args()
    client(args['m'], args['text'])


if __name__ == "__main__":
    main()
