import requests

cookies = {
    # 'acw_tc': '76b20f4516223129546774340e9a82fb4e68b3bd94ad000b57fbba2886e9c1',
    # 'appCode': 'pamir',
    # 'UM_distinctid': '179b96332152d5-0adfd1994ae664-2363163-144000-179b96332162ec',
    # 'CNZZDATA1277224060': '19650971-1622310944-%7C1622310944',
    # 'cna': '/HU5GbucIn4CASQFoh/pAMM4',
    # 'xlly_s': '1',
    # 'isg': 'BCcnBHxvC4zNno8Abjm9MYWDtlvxrPuOvf7xhPmWFLb-6FOqFX9l3GvqDuD2ANMG',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'style': 'ldefault',
    'cert': '245eaa2bbaf4fb4d7bb19cdc76a209326071441e391141803bedddb04487c9293f2f66beee48a8904ab7e6f4fec37d90d8c669deed2ed8046836f077b3b75eee5047ba08e34936582e740b2897a99b1fbf315062697402defe3979d76dae9fe1df7bd5fb4246d4673e04cbd948f719441cf5c6960af18d2ce086f8043cda7385898554b5ed389f4b493ffb87982ce09e9d9d0a4bca5ffd797f50929a39eee77184e9c103ec852e61638ec060e907af619f091707fd204b7f71c72f6b172c60f2',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sessionid': 'N9GsGDxVow6xSyPK4vgiBnxD_NHhLgaszjRbdLzElgH682PMQWjloTNpI5HnZUk8',
    'type': 'BASIC_IMG',
    # 'token': '07c3e32d12ac04a910176bf0fcd81b163f3387980b2c5a255bf74127eda2301fc798282f6fe6afbcb74f770da3413146eb6ede979873a74e315bfe6addc2c451ca80b6fd84b4107e0e0abc1be5c50bbf0e2d92a8721a292d12c07f91a0ca2f5bf4df0ce69115feb563ec76c3bb9bae7f0aedfe5a51dcf9bf8ad4fec83c1fd09c533d320c6bed5ee1ba658d200fa8c6607f3bc72de22dbe2841a69bd4fca878cc4a31eafcc374cdf0d9037405a9495d57796910fc047dd72fe42cfa90eba40a91',
    'appkey': 'lassen',
    'Origin': 'https://www.netcourt.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.netcourt.gov.cn/',
    'Accept-Language': 'zh',
}
for i in range(3):
    b=i*100
    data = {
      'filterMap': '{"key":"","beginTime":"2021-05-30","endTime":"2021-06-29","page":{"begin":%s,"length":100}}'%(b,)
    }

    response = requests.post('https://www.netcourt.gov.cn/portal/indexRpc/queryCourtTrialVos.json', headers=headers, cookies=cookies, data=data)
    a=response.json()
    print(a)