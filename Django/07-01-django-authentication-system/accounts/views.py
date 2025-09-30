from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 일반 form은 첫번째 인자에 request가 추가됨
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 세션을 생성
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        # GET 요청일 때 로그인 페이지를 응답하는 로직
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/login.html', context)