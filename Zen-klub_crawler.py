import requests
import pandas as pd
import json
from datetime import datetime

def executa_request(limit):
    base_url = 'https://api.zenklub.com.br'
    professionals_data = []

    batch_inicial = limit
    skip = 0
    batch_size = min(100, batch_inicial)  # Define o tamanho do lote inicial

    while skip < batch_size:
        try:
            headers = {
            # pegar no site 
        }
            params = {
                'country': 'ar',
                'skip': skip,
                'limit': batch_size,
            }
            url = f'{base_url}/search/professionals'
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            print(response)
            json_data = response.json()
            limit = json_data['total']
            professionals_data.append(json_data)
            skip = batch_size
            batch_size = min(limit, batch_inicial + skip)  # Atualiza o tamanho do lote
        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.Timeout):
                print("API Request Timeout. Retrying after 5 seconds...")
                time.sleep(5)  # Aguarda 5 segundos antes de tentar novamente
                return executa_request(limit, iteration_list)
            else:
                print(f"API Request Error: {e}")
                return None
            
    return professionals_data

def save_json(data, prefix):
    now = datetime.now().strftime('%Y_%m_%d')
    json_filename = f'{prefix}_{now}.json'
    
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def consolidate_professionals_data(professionals_data):
    if professionals_data is not None:
        all_professionals = [professional['professionals'] for professional in professionals_data]
        consolidated_professionals = [item for sublist in all_professionals for item in sublist]
        
        professionals_df = pd.json_normalize(consolidated_professionals)
        print(professionals_df)
        print(professionals_df.count())
        return professionals_df

def preprocess_data(data):
    # Transform list and dictionary columns into formatted strings
    for col in data.columns:
        if isinstance(data[col][0], (list, dict)):
            data[col] = data[col].apply(json.dumps)
    return data

def save_csv(data, prefix):
    now = datetime.now().strftime('%Y_%m_%d')
    csv_filename = f'{prefix}_{now}.csv'
    
    if isinstance(data, pd.DataFrame):
        data.to_csv(csv_filename, sep='|', index=False, encoding='utf-8')


def main():
    limit = 100
    
    professionals_data = executa_request(limit)
    save_json(professionals_data, 'zenklub_api')
    print(f'Arquivo json salvo!')
    professionals_df = consolidate_professionals_data(professionals_data)
    #problemas a resolver a partir daqui
    preprocessed_professionals_df = preprocess_data(professionals_df)
    save_csv(preprocessed_professionals_df, 'zenklub_consolidated')
    print(f'Arquivo csv salvo!')

if __name__ == "__main__":
    main()
