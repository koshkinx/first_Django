
from django.shortcuts import render


def courses_page(request):
    return render(request, 'courses_app/courses_page.html')
