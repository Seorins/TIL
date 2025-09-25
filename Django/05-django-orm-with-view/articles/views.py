from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

# 전체 게시글 조회(1) 후 메인 페이지 응답(2)
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 상세 페이지 응답하는 함수
def detail(request, pk):
    
    # 1. 몇 번 게시글인지 데이터베이스에서 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회한 전체 게시글 데이터를 템플릿과 함께 응담
    context ={
        'article' : article
    }

    return render(request, 'articles/detail.html', context)


# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')


# 1. 사용자로부터 입력 받은 데이터를 추출
# 2. 추출한 데이터를 DB에 저장 
# 3. 저장이 완료되었다는 페이지를 응답
def create(request):
    # 1.
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. DB에 저장
    # 2-1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2-2
    article = Article(title=title, content=content)
    article.save()

    # 2-3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')

    # 클라이언트한테 새로운 주소로 요청을 보내게끔 시켜야 함
    # return redirect('articles:index')

    # redirect 함수를 한 벋 더 실행하게 됨 (총 요청 2번)
    # "POST /articles/create/ HTTP/1.1" 302 0
    # "GET /articles/5/ HTTP/1.1" 200 461 
    return redirect('articles:detail', article.pk)


def delete(request, pk):

    # 1. 어떤 게시글 삭제할 건지 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회한 게시글을 삭제
    article.delete()

    # 3. 메인 페이지 redirect
    return redirect('articles:index')


def edit(request, pk):
    
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)