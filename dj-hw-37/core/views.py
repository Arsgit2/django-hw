from django.shortcuts import render
def index(request):
    return render(request, 'index.html', {'text': 'пример текста', 'number1': 5, 'number2': 3})