from django.shortcuts import render

def main_page(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'main_page.html')
