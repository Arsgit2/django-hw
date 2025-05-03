
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import add_message
from django.core.signing import Signer, BadSignature
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def custom_message_view(request):
    add_message(request, 50, 'Это пользовательское всплывающее сообщение!')
    return redirect('home')

def signed_data_view(request):
    signer = Signer()
    data = "важные_данные"
    signed_value = signer.sign(data)
    return HttpResponse(f"Подписанные данные: {signed_value}")

def verify_signed_data_view(request, signed_value):
    signer = Signer()
    try:
        original = signer.unsign(signed_value)
        return HttpResponse(f"Оригинальные данные: {original}")
    except BadSignature:
        return HttpResponse("Подпись недействительна!")
