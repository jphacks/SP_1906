from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
# Create your views here.


def index(request):
    if request.method=="GET":
        params={"title":"ddtree"}
        return render(request, "index.html", params)

def posted(request):
    if request.method =="POST":
        #ここにJSONを整えてDBにいれとく
        #成功したよ。か、失敗したよ。を返す。
        a="aa"
        
        params={a:1}
        return render(request, "done.html", params)

def from_arduino(request):
    if request.method == "GET":
        #DBにあるか見てテキトーに返す。
        #params={a:1,b:2}
        ret={"data":"1"}
        return  JsonResponse(ret)   

def stats(request):
    if request.method == "GET":
        return render(request, "stats.html")



