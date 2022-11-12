import requests
import pandas as pd

limit = '30'
json = 'a'
a = [1,2]
b = 1


def requisicao(limit):
    
    for b in a:
        
        headers = {
            'authority': 'api.zenklub.com.br',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pt-BR',
            'authorization': 'unknown',
            'origin': 'https://zenklub.com.br',
            'referer': 'https://zenklub.com.br/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        params = {
            'country': 'br',
            'skip': '0',
            'limit': limit,
        }
        response = requests.get('https://api.zenklub.com.br/search/professionals', params=params, headers=headers)
        json = response.json()
        limit = json['total']
        b = b +1
    return(json)

json = requisicao(limit)
df = pd.DataFrame(json)
df2 = pd.json_normalize(df['professionals'])

df2.to_csv('zen-klub.csv')



