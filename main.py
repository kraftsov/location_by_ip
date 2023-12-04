import folium
import requests
from pyfiglet import Figlet


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response: dict = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)

        data = {
            '[IP]': response['query'],
            '[Провайдер]': response['isp'],
            '[Организация]': response['org'],
            '[Город]': response['city'],
            '[Страна]': response['country'],
            '[Код страны]': response['countryCode'],
            '[Регион]': response['region'],
            '[Широта(latitude)]': response['lat'],
            '[Долгота(longitude)]': response['lon'],
        }

        for key, value in data.items():
            print(f'{key} : {value}')

        area = folium.Map(location=[response['lat'], response['lon']])
        area.save(f'{response["query"]}_{response["city"]}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Проверь соединение с интернетом!')


def main():
    #
    preview = Figlet(font='slant')
    print(preview.renderText('IP INFO'))
    #
    ip = input('Введите IP для вывода информации: ')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
