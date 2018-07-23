from django.core.mail import send_mail
import random

message_verify = '''Hello, 

Your verification code is :

%s

DON'T tell it to others!

'''

def verify_email(code, email):
    send_mail(
        '[DOYO] Your doyo verification code',
        message_verify %code,
        'noreply<doyotech@aliyun.com>',
        [email],
        fail_silently=False,
    )


def generate_verification_code(num):
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65, 91):
        code_list.append(chr(i))
    for i in range(97, 123):
        code_list.append(chr(i))

    myslice = random.sample(code_list, num)
    verification_code = ''.join(myslice)
    return verification_code
