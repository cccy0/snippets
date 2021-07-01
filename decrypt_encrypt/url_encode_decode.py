# https://blog.csdn.net/ruanxingzi123/article/details/83017575
# url中通常只能包含ascii字符 所以要把一些特殊字符例如汉字 进行编码转化为ascii格式 就是代%的16进制格式
from urllib.parse import urlencode

# 把字典转换成url的参数 同时最中文编码
data = {
    'name': '青春',
    'a':'美好'
}
params = urlencode(data)
print(params)

# 对一个字符进行url编码

from urllib.parse import quote

encode_value = quote('青春')
print(encode_value)

# 解码 解析查询参数

from urllib.parse import unquote

decode_param = unquote(params)
decode_value = unquote(encode_value)
print(decode_param)
print(decode_value)

# 查询参数解析成字典
from urllib.parse import parse_qsl, parse_qs

decode_param_dict_list_value = dict(parse_qs(decode_param))
decode_param_dict_str_value = dict(parse_qsl(decode_param))

print(decode_param_dict_list_value)
print(decode_param_dict_str_value)
