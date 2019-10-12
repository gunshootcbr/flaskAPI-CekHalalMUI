import requests

r = requests.get("https://sites.google.com/macros/exec?service=AKfycbx_-gZbLP7Z2gGxehXhWMWDAAQsTp3e3bmpTBiaLuzSDQSbIFWD&menu=nama_produk&query=oreo")

data = r.json()

for key in data:
    for value in data['data']:
        print(value['title'])