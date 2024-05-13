from django.shortcuts import render, redirect
from .models import UserInput
from django.http import HttpResponse


def input_page(request):
    if request.method == 'POST':
        user_input_text = request.POST.get('user_input', '')
        request.session['user_input'] = user_input_text
        return redirect('display_page')
    else:
        return render(request, 'members_app/input_page.html')


def save_input(request):
    if request.method == 'POST':
        user_input_text = request.POST.get('user_input', '')
        UserInput.objects.create(input_text=user_input_text)
        return HttpResponse("Дані успішно збережено")
    else:
        return HttpResponse("Метод запроса не поддерживается")


def display_page(request):
    user_input_text = request.session.get('user_input', '')
    UserInput.objects.create(input_text=user_input_text)
    user_inputs = UserInput.objects.all()
    return render(request, 'members_app/display_page.html', {'user_inputs': user_inputs})


def session_page(request):
    user_input_text = request.session.get('user_input', '')
    return render(request, 'members_app/session_page.html', {'user_input_text': user_input_text})
