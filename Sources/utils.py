from typing import Any
import json
import requests
import os
def generate_docs(obj: Any, isSaved:bool = True,
                  folder_path: str = '/Users/sinazabanfahm/FinAT/Sources/docs') -> str:
    opt = ""
    folder_path = folder_path + "/" if folder_path[-1]!="/" else folder_path
    file_path = folder_path + str(obj) +".txt"
    for attr_name in dir(obj):
        if not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)
            try:
                if callable(attr_value):
                    opt+=(f"Documentatin for the callable {attr_name}:\n  {attr_value.__doc__}")
                else:
                    opt+=(f"{attr_name}:\n {attr_value}")
            except Exception as e:
                pass
    if isSaved:
        with open(file_path, 'w') as file:
            file.write(opt)
    return opt


def load_tickers_json(exchange: str, links_file: str = './Sources/links/tickers1.json', 
                     save_folder: str = './Sources/tickers') -> None:
    try:
        with open(links_file, 'r') as f:
            links = json.load(f)
            exchange_url = links[exchange]
            response = requests.get(exchange_url)
        if response.status_code == 200:
            tickers_list = json.loads(response.text)
            tickers_dict = {ticker['symbol']: ticker for ticker in tickers_list}
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        raise(e)
    try:
        with open(f"{save_folder}/{exchange}.json", 'w') as f:
            json.dump(tickers_dict,f)
    except Exception as e:
        raise(e)
    return 

def get_tickers_json(exchange: str, links_file: str = './Sources/links/tickers1.json', 
                     load_folder: str = './Sources/tickers') -> dict:
    
    load_path: str = load_folder + f"/{exchange}.json"
    try:
        if not os.path.exists(load_path):
            load_tickers_json(exchange = exchange, links_file = links_file, save_folder=load_folder)
        with open (load_path,'r') as f:
            return json.load(f)
    except Exception as e:
        raise(e)
