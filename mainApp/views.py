from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'index.html')


def study(request):
    return render(request, 'study.html')


def work(request):
    return render(request, 'work.html')
