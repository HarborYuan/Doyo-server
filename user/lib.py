from django.core.mail import send_mail


def verify_email(code, email):
    send_mail(
        'Verification code',
        'Your verification code is : ' + code,
        '1027832731@qq.com',
        [email],
        fail_silently=False,
    )
