from django.shortcuts import render, redirect
from .models import UserInput
from django.http import HttpResponse


def input_page(request):
    if request.method == 'POST':
        user_input_text = request.POST.get('user_input', '')
        UserInput.objects.create(input_text=user_input_text)
        return redirect('display_page')
    else:
        return render(request, 'members_app/input_page.html')


def save_input(request):
    # Код для обробки введених даних і збереження їх у базу даних
    return HttpResponse("Дані успішно збережено")


# def display_page(request):
#     user_inputs = UserInput.objects.all()
#     return render(request, 'members_app/display_page.html', {'user_inputs': user_inputs})


def display_page(request):
    # Отримати дані введені користувачем з сесії
    user_input_text = request.session.get('user_input', '')
    # Створити об'єкт UserInput і зберегти введений текст
    UserInput.objects.create(input_text=user_input_text)
    # Отримати всі введені дані з бази даних
    user_inputs = UserInput.objects.all()
    return render(request, 'members_app/display_page.html', {'user_inputs': user_inputs})


def session_page(request):
    return render(request, 'members_app/session_page.html')
