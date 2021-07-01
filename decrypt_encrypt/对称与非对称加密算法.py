# 加密库
# pycryptodome linux
# import Crypto

# pip install pycryptodomex
# import Cryptodome
# ======================================================DES===========================================================

# 要指定 key 密钥 mode加密方式 例如ecb 填充方式  偏移量
from Cryptodome.Cipher import DES


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


# key为8个字节
key = '12345678'.encode()
des = DES.new(key=key, mode=DES.MODE_ECB)
text = 'encrypt me using des'
padded_text = pad(text)
print(padded_text)
encrypted_text = des.encrypt(padded_text.encode("utf-8"))

print('encrypted message using des：', encrypted_text)
plain_text=des.decrypt(encrypted_text).decode().rstrip()
print('plain text',plain_text)

# =========================================================aes=================================================
key='1234567890123456'.encode()
# 必须16位字节
data='加密的密文 用aes'
from Cryptodome import Random
from Cryptodome.Cipher import AES
# 生成长度等于AES 块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)
mycipher = AES.new(key, AES.MODE_CFB, iv)

# 加密的明文长度必须为16的倍数， 如果长度不为16的倍数， 则需要补足为16的倍数

# https://blog.csdn.net/ruanxingzi123/article/details/83017575/
