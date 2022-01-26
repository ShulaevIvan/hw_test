import json
from lib2to3.pgen2 import token
import requests

TOKEN = 'AQAAAAABdHjIAADLW3sSKDMni0Vhvo4GUFWFbFw'
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
HEADERS = f'Authorization' 'OAuth + {TOKEN}'


        
def auth():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(TOKEN)
        }
        
def create_folder(folder='test'):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = auth()
    params = {"path": folder}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code 
        

if __name__ == '__main__':
    auth()
    create_folder('test2')
    
    
        
        
    
