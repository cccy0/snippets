from Crypto.Cipher import PKCS1_OAEP

private_key = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKL9Zo15Eg1B7/omsPWlpD1hOdRok/dVnMK6DHBL2hmpQg+X0RPjLvTkYsSflbncSH4pY/D76cnHnb0SjSbCRNBiumn555YdZGGTuO82gUx7sXBTqyQY4chnF4GCfUvzxqo9i1gf309gIQkA69SvNMW1G3fHP7cHRIxSelZUGxQrAgMBAAECgYBnpTIwppvHGHYNIcuH+hRN/+SxYOsu7h8oaPz98A46ITrkBYur1N0IV69DD6Q7s4vZxmJKXTdW2/w/vmtKCWGOCHM+bM/pcqyAwOZW0P+EgkTPnXnyBjkDTHTC3lMbBemwr9TLyGLNFiCzrr73TFkPI7NPUBlx9y1t7j35+x8B4QJBAOatW4ki3XuH/8ACpyLl1qiE1EfggeK4n14MQ12akUslN5y/dsic4J0AbbMbhtgzNRCZ7O4oYGOUWgvCWdAvLXsCQQC04dlS2E2C0l3mODo8H3iwUXXz9dUqMcaAnNMOftO9Uj7N8u6lHZRLhEGAAiiU//Vw2URoBczok7fETugiDH0RAkBlJ9JDIeHkIPBbAA7Q898dCRqZ5m6uwG1KbbBA5N4gCNMJTsDFGl45Gw4AA+su9c2oWQeYLGaQZGbUT0bZT0bvAkAhFvPfwOwlE4DT/dNBbmxwrOZME9vEFUj//DBsBW2Mw7/zgw5/LDMVwYMN/NcZst1eoJBwCyeaIHPMuLaki+5RAkEAzesKVoabkO21AEBXwX82/GfGjrmcvpq5N4u+5gstdI1zlGK//fCRt42UesT8MjMIt/Oo1xBS7qdmL0nqHJRfJw=="
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode

private_key="-----BEGIN RSA PRIVATE KEY-----\n{}\n-----END RSA PRIVATE KEY-----".format(private_key)
# private_key = b64decode(private_key)
rsa_key = RSA.importKey(private_key)
cipher = PKCS1_OAEP.new(rsa_key)
c_msg = "hOP4k3GvlbKte6qv4ggiPW9ayrI6xJHgSq1pYzNMzFHY0GewTGQsFFP1cTr/OTtc/M+mWqoviJMYJBi0CFY82XzO3+r/Oq+h/JPjlBBoTDCUqPmd5ILULXQJyVia2KFZ1x5XnWkU7fWOfhUybpbVBQR6g4qIG89zQdIV2trUCvA="
c_msg = b64decode(c_msg)
cipher.decrypt(c_msg)

# raw_cipher_data = b64decode('')
# cipher = PKCS1_v1_5.new(rsa_key)
# phn = rsa_key.decrypt(raw_cipher_data, )
