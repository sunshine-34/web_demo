from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_view_func(request):
    # 返回一个响应
    return HttpResponse('<h1>hello world</h1>')