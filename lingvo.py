import os
from dotenv import load_dotenv
import requests


languages = {
             'De': 1031,
             'En': 1033,
             'Ru': 1049
            }


def lingvo_auth(token):
    url = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    headers = {'Authorization': f'Basic {token}'}
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    result = response.content.decode('utf-8')
    return result


def lingvo_word_forms(word, token, lang):
    result_dict = {}
    url = 'https://developers.lingvolive.com/api/v1/WordForms'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'text': word, 'lang': lang}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    result = response.json()
    return result


def translate_lingvo(word, lang_from, lang_to, token):
    url = 'https://developers.lingvolive.com/api/v1/Translation'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'text': word,
              'srcLang': lang_from,
              'dstLang': lang_to,
              'isCaseSensitive': False
              }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    result = response.json()
    return result


def parse_response(resp):
    for element in resp:
        word = element['Lexem']
        part_of_speech = element['PartOfSpeech']
        groups = element['ParadigmJson']['Groups']
        for group in groups:
            name, table = (group['Name'], group['Table'])
            print(name, table)


def main():
    load_dotenv()
    auth_token = os.getenv('LINGVO_TOKEN')
    token = lingvo_auth(auth_token)
    word = lingvo_word_forms('Fernster', token, 1031)
    parse_response(word)


if __name__ == '__main__':
    main()
