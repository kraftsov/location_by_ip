import requests


def get_info_by_ip(ip='127.0.0.1'):
    try:
        pass
    except requests.exceptions.ConnectionError:
        print('[!] Проверь соединение с интернетом!')


def main():
    get_info_by_ip()


if '__name__' == '__main__':
    main()
