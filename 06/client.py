import threading
import socket
import sys
import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from collections import Counter


def client():
    pass


def main():
    sock = socket.socket()
    sock.connect(("", 9080))
    sock.sendall(b"https://github.com/mailcourses/deep_python_spring_2022/tree/main/lesson-06")
    smth = sock.recv(100000)
    sock.close()
    print(smth.decode())


if __name__ == "__main__":
    main()
