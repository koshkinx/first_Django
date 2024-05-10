from django.shortcuts import render, redirect
from django.contrib import messages


def input_page(request):
    if request.method == 'POST':
        return redirect('display_page')
    else:
        return render(request, 'members_app/input_page.html')


def display_page(request):
    return render(request, 'members_app/display_page.html')


def session_page(request):
    return render(request, 'members_app/session_page.html')
