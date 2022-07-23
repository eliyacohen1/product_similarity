import requests
import json


def alibaba_get_search_result_titles(search_string):
    # Alibaba string search is limited to 50 char max
    search_text = search_string.replace(" ", "+")[:50]
    url = f"https://open-s.alibaba.com/openservice/galleryProductOfferResultViewService?appName=magellan&appKey=a5m1ismomeptugvfmkkjnwwqnwyrhpb1&searchweb=Y&fsb=y&IndexArea=product_en&CatId=&SearchText={search_text}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            response_json = json.loads(response.text)
            return {str(x['information']['id']): (x['information']['puretitle'], x['information']['productUrl']) for x in
                    response_json['data']['offerList']}
        except Exception as e:
            print(e)


def enum_amazon_items(items_file_path):
    with open(items_file_path, "r", encoding='utf-8') as f:
        items_dict = json.load(f)
        for asin, item in items_dict.items():
            yield item['title']


# print(alibaba_get_search_result_titles('light reacher 31 r2 adult bedside feeding sounds'))
# for i, item in enumerate(enum_amazon_items('amazon_items.json')):
#     print(i, item)
