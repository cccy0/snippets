# base64就是用64位字符串表示任意二进制数据
# 原理就是先把字符串转换为ascii码
# ascii码转化为二进制数据
# 再将二进制分组 最后转换成十进制
# 从bs64编码表获取十进制对应的base64编码

import base64

wx_number = '110'
wx_number_bs64 = base64.b64encode(wx_number.encode())
wx_number_bs64 = wx_number_bs64.decode()
print(wx_number_bs64)

wx_number_plain = base64.b64decode(wx_number_bs64)
wx_number_plain = wx_number_plain.decode()
print(wx_number_plain)

# =============================================== MD5 ==========================================================

# 信息摘要算法又叫hash算法

# 他是把任意长度的数据转换为一个长度固定的数据

# 特点
# 1 不可逆
# 2 原信息相同 hash值相同 这个特征可以用来去重或者做签名 防止数据被篡改
# 3 hash值不同可能原信息也相同 这个可以通过进一步比较原信息来解决
# 4 md5还可以用来计算文件md5 用来防止文件被篡改 保证完整传输
import hashlib

user_id = '100000000'
md5_obj = hashlib.md5()
md5_obj.update(
    user_id.encode()
)
print(md5_obj.hexdigest())

import hashlib


def get_file_md5(f):
    m = hashlib.md5()

    while True:
        data = f.read(10240)
        if not data:
            break

        m.update(data)
    return m.hexdigest()


YOUR_FILE = 'jsencrypt.js'

with open(YOUR_FILE, 'rb') as f:
    file_md5 = get_file_md5(f)
    print('jsencrypt.js文件的md5码:',
          file_md5)

# hmac算法就是加盐的hash算法 为的是防止根据hash值反推原始信息
import hmac

key = b'i am a salt'
message = b'wo de mi ma'
h = hmac.new(key, message, digestmod=hashlib.md5)

print('加salt的md5值：{}'.format(h.hexdigest()))

h = hmac.new(key, message, digestmod=hashlib.sha1)

print('加salt的sha1值：{}'.format(h.hexdigest()))

# =======================================  sha1 =============================================================
# 比md5更长 更安全 计算时间也更长

