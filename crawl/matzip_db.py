import requests
import pprint
import urllib.parse
import time
from pymongo import MongoClient

client = MongoClient('locallost', 27017)
db = client.seoul_matzip

seoul_gu = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구",
            "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]

client_id = "oa9Yhj8zcrDE3Od9ba3n"
client_secret = "Q3PBAURfTu"

def get_naver_result(keyword):
    time.sleep(0.1)
    api_url = f"https://openapi.naver.com/v1/search/local.json?query={keyword}&display=10&start=1&sort=random"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    data = requests.get(api_url, headers=headers)
    data = data.json()
    return data['items']

docs = []

for gu in seoul_gu:
    keyword = f'{gu} 맛집'
    matzip_list = get_naver_result(keyword)

    print("*"*80 + gu)

    for matzip in matzip_list:
        matzip['gu'] = gu
        pprint.pprint(matzip)
        docs.append(matzip)

db.matzip.insert_many(docs)