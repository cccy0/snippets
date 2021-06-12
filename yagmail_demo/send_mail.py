# https://github.com/kootenpv/yagmail#install
# it is really easy to send email
import yagmail
yag=yagmail.SMTP(
    user='infomationloss@163.com',
    # 授权码
    password='',
    host='smtp.163.com'
)
contents=[
    'This is the body',
    'You can find attached',
    'dc.PNG'
]
yag.send(
    '2696616968@qq.com',
    'subject',
    contents=contents
)

yag.close()