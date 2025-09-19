import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods) # 랜덤으로 pick함
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)
    pass


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    context = {
        'message' : request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)

def greeting(request):
    pass
