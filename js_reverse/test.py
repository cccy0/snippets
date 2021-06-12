import requests

cookies = {
    'ncCookie': 'Fgw9UG4gPoS3AcN0a1xidhUn4oWGmi48c-1ZPIyYaNJERBBQgHDBUZo325MTwNPK0zBnzO5fbnKj76rWnDZ5jjHcwJTM4JvqDn8Xd-HiwrxuA_EOC3Yf8XGWXQacUejN',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': '*/*',
    'Origin': 'https://www.netcourt.gov.cn',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.netcourt.gov.cn/',
    'Accept-Language': 'zh,zh-CN;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,ko;q=0.5,ar;q=0.4,en-US;q=0.3,en;q=0.2',
}

params = (
    ('ai', 'MDExAAoAYAALAPIADAAAAF00AAUCAAQAAACwAQIABgAQAJC2XBUCAAgAABCXHlNUNwQCAAYgACAQkwMWAgAg8RNjIyOTgxMDAzODUyMD4oMDk0NjkxOTQwMDk0MzMyMXAgAYIAAAADFmV-Y2R5b25oKSAregAgICAgICEAIAAQATAgAUAAEAADaGJ_bWVqPy8uZWd0cWJvIGAgAoAAAAAAAAAAAAAGAAAAAgYQAAYAAAADAGAABgAAAAMIMAAGAAAAAwgwcCAAQAAAAAAgIAEBAAIECCAAAQlx5zlBsgI0MYAgAhAjMTZoNjgxaTA1YjEzNTI2YTJlZzk4NjUzM2E2MjZpMj'),
    ('ak', 'lassen'),
    ('token', '16229810038520.8094691940094332'),
)

response = requests.get('https://hemera.gdapi.cn/api/aethernc/analyze', headers=headers, params=params, cookies=cookies)
print(response.json())