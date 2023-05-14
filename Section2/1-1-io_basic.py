import requests
import time
import os
import threading


def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    # os.getpid() : return the current process id
    # threading.get_ident() :
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://apple.com", "https://google.com"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        # print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 13.21s