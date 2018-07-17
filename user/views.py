from django.http import HttpResponse, JsonResponse
from user.models import User
import hashlib
import datetime

from user.lib import verify_email, generate_verification_code


def index(request):
    return HttpResponse("It's the user module, and it's no ussessione to access this page")


def register(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    code = request.POST.get('code')
    if None in [email, username, password]:
        return JsonResponse({
            'err': 1,
            'msg': 'Something lost'
        })
    password = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
    r = User.objects.filter(username=username)
    if len(r):
        return JsonResponse({
            'err': 1,
            'msg': 'username already exists'
        })
    r = User.objects.filter(email=email)
    if len(r):
        return JsonResponse({
            'err': 1,
            'msg': 'email already exists'
        })
    if not (request.session.get('email_verify') == email and request.session.get('token_verify') == code):
        return JsonResponse({
            'err': 1,
            'msg': 'Verify code error!'
        })
    try:
        User.objects.create(
            email=email,
            username=username,
            password=password
        )
    except Exception:
        return JsonResponse({
            'err': 1,
            'msg': 'Register error'
        })
    return JsonResponse({
        'err': 0
    })


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if None in [email, password]:
        return JsonResponse({
            'err': 1,
            'msg': 'Something lost'
        })
    password = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
    try:
        r = User.objects.get(email=email)
    except Exception:
        return JsonResponse({
            'err': 1,
            'msg': 'email address does not exists'
        })
    if (r.password == password):
        return JsonResponse({
            'err': 0
        })
    return JsonResponse({
        'err': 1,
        'msg': 'password is wrong'
    })


def email_verify(request):
    email = request.POST.get('email')
    if None in [email]:
        return JsonResponse({
            'err': 1,
            'msg': 'emaiml is None'
        })
    r = User.objects.filter(email=email)
    if len(r):
        return JsonResponse({
            'err': 1,
            'msg': 'email already exists!'
        })
    request.session['email_verify'] = email
    request.session['token_verify'] = generate_verification_code(6)
    verify_email(request.session.get('token_verify'), email)
    return JsonResponse({
        'err': 0
    })
