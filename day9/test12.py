import requests

url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"cache-control": "max-age=0",
"cookie": "GUID=d2218fe5-9161-4207-98e1-a0b818962beb; Hm_lvt_9793f42b498361373512340937deb2a0=1698047945; sajssdk_2015_cross_new_user=1; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F06%252F66%252F99%252F100829966.jpg-88x88%253Fv%253D1690875618000%26id%3D100829966%26nickname%3D%25E5%25B0%258F%25E9%25BB%2591%25E6%2597%25A0%25E6%2595%258C%25E9%2585%2592%25E9%2587%258F%26e%3D1713599838%26s%3Da3bb14ed41f1e882; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100829966%22%2C%22%24device_id%22%3A%2218b5b8ba0805f0-04e3c9e7dc2dd4-312a764f-1327104-18b5b8ba081fc3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22d2218fe5-9161-4207-98e1-a0b818962beb%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1698048959",
"sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
    }
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)