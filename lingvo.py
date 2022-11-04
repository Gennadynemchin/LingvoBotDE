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
    print(result)
    for element in result:
        list_for_parsing = element['ParadigmJson']['Groups']
        for x in list_for_parsing:
            # print(x)
            if x['Name'] == "Indikativ, Perfekt, Aktiv":
                print(x['Table'])


def main():
    auth_token = 'Yjg2YzA1YWItZmI3Ni00Y2MwLWEzNjgtOTk1YTkyMDBkZmRjOjNlNWM3YzAzYWJjNDRlMmQ5NmNmOGUzNDE4MTc0NmRl'
    token = lingvo_auth(auth_token)
    lingvo_word_forms('Alt', token, 1031)


if __name__ == '__main__':
    main()
