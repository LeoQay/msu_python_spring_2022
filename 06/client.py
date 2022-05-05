import threading
import socket
import argparse
import sys
from collections import deque


def thread_client(address, urls: deque[str], urls_lock, print_lock, out):
    while True:
        urls_lock.acquire()
        if len(urls) == 0:
            urls_lock.release()
            return

        url = urls.popleft()
        urls_lock.release()

        sock = socket.socket()
        try:
            sock.connect(('', address))
            sock.sendall(url.encode(encoding='utf-8'))
            data = sock.recv(100000).decode(encoding='utf-8')
        except BaseException:
            sock.close()
            return

        print_lock.acquire()
        url = url.strip('\n')
        data = data.strip('\n')
        print(f'{url}:\n{data}\n', file=out)
        print_lock.release()

        sock.close()


def client(address, members, text, out):
    # shared resource
    with open(text, encoding='utf-8') as file:
        urls = deque(list(file))

    urls_lock = threading.Semaphore(1)
    print_lock = threading.Semaphore(1)

    threads = [
        threading.Thread(target=thread_client,
                         args=(address, urls, urls_lock, print_lock, out))
        for _ in range(members)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    out.close()


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(type=int, dest='m', default=10)
    parser.add_argument(type=str, dest='text', default='urls.txt')
    parser.add_argument('-a', type=int, default=9080)
    return parser.parse_args(args=argv[1:]).__dict__


def main(argv, out_name):
    args = get_args(argv)
    if out_name == 'stdout':
        client(args['a'], args['m'], args['text'], sys.stdout)
    else:
        with open(out_name, 'a', encoding='utf-8') as out:
            client(args['a'], args['m'], args['text'], out)


if __name__ == "__main__":
    main(sys.argv, 'stdout')
