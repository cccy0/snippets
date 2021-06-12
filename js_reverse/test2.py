import requests

cookies = {
    # 'appCode': 'pamir',
    # 'UM_distinctid': '179dbb6df6c1a9-08fbabccffe802-2363163-144000-179dbb6df6d2bd',
    # 'cna': 'p9J/F2iaPDgCAdpPcNzndFk5',
    # '_bl_uid': 'LhkRspLLjLksnzz51s8z69qaCCne',
    # 'acw_tc': '781bad3616229814183537052e0c6f3c516b90dd9910676af35f25da3f04ae',
    # 'CNZZDATA1277224060': '889909891-1622887133-https%253A%252F%252Fwww.baidu.com%252F%7C1622978421',
    # 'xlly_s': '1',
    # 'isg': 'BFxc6R4CUNOJWiSIt-_1GIvlLXoO1QD_ageaRTZdFcclgf4LX-crjsB75OF5eThX',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'style': 'RECAPTCHA',
    'cert': '4ad93fc21ee114b3cd03f7a9f7aab959008d9e0b7af9bf8ba0faf36e4468587db7efc73af22e6f2021f94738ea08a15c21b45b4f61565d8dcb11067365563b76af324cf9d6e003e9b5c303bb86674b7db0bde5fdcbb04e6b5327dc821640aaef366a72bb540bc1d358a60975bfca02dc8e401f2067990ec053ae549b281d26bb53d1511d786c26a07aa0a7ee3428b637eac28b9bbb1afd140f0841d7e677ab9e65ad1ad3fa499f1947400472fb65613bedb68bed59bf285231faa24c0945c003',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sessionid': 'N9GsGDxVow6xSyPK4vgiBnxD_NHhLgaszjRbdLzElgHxO8vkJUnr0Aj-jQeaOCVt',
    'type': 'RECAPTCHA',
    'token': 'undefined',
    'appkey': 'lassen',
    'Origin': 'https://www.netcourt.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.netcourt.gov.cn/',
    'Accept-Language': 'zh,zh-CN;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,ko;q=0.5,ar;q=0.4,en-US;q=0.3,en;q=0.2',
}

data = {
  'filterMap': '{"key":"","beginTime":"2021-06-06","endTime":"2021-07-05","page":{"begin":30,"length":10}}'
}

response = requests.post('https://www.netcourt.gov.cn/portal/indexRpc/queryCourtTrialVos.json', headers=headers, cookies=cookies, data=data)
print(response.text)