import requests
import os
url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'
response = requests.get(url)

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/wine'):
    os.mkdir('data/wine')
if not os.path.exists('data/scripts'):
    os.mkdir('data/scripts')


with open('./data/wine.zip',mode ='wb') as f:
    f.write(response.content)

import zipfile
with zipfile.ZipFile('wine.zip',mode = 'r') as archive:
    archive.extractall(path='data/wine')

wine_index = 'data/wine/index'
wine_data = 'data/wine/wine.data'
wine_names = 'data/wine/wine.names'

import hashlib
#Compare SHA
# MacOS: shasum -a 256 filename
# Windows: certutil -hashfile filename 256
wine_data_256 = '6be6b1203f3d51df0b553a70e57b8a723cd405683958204f96d23d7cd6aea659'
wine_names_256 = 'f1b84f2ef845e0bdebf13e14fa7a213e56de4f1baa40c5974dbd1ee51c5ae710'
wine_index_256 = 'c24d1f17df97bdde234913bb0a3334227215eefd0ad3d6a9988151d49971cba7'

def hash_compare(filename,hash_value):
    with open(filename,mode='rb') as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
        if(sha256hash == hash_value):
            print('Hash matches')
        else:
            print('Not match')
hash_compare(wine_index, wine_index_256)
hash_compare(wine_data,wine_data_256)
hash_compare(wine_names,wine_names_256)