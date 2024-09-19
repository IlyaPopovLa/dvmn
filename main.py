import requests

def get_weather(location):
    url_template = 'https://wttr.in/{}'
    url_params = {
        'lang': 'ru',
        'nTpqmM': ''
    }
    url = url_template.format(location)
    response = requests.get(url, params=url_params)
    response.raise_for_status()
    print(response.text)

def main():
    locations = ['london', 'Шереметьево', 'Череповец']

    for location in locations:
        get_weather(location)

if __name__ == '__main__':
    main()