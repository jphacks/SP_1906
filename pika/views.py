from django.shortcuts import render
import json
from django.http.response import JsonResponse, HttpResponse
from django.http import QueryDict, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
# Create your views here.


def index(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",
        }
        return render(request, "index.html", params)


def table(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "posttest",
        }
        return render(request, "table.html", params)

def canvas(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "posttest",
        }
        return render(request, "canvasing.html", params)

def posttest(request):
    if request.method == 'GET':
        return HttpResponse("you've http getted to this page")
    if request.method =='POST':
        print("posted")
        aa = "<style>body{margin:100px;}</style>"
        aa+="your data is :<br><small>"
        for i in range(len(request.POST)-1):
            aaa = request.POST[str(i)]
            color = aaa.replace("rgb","")
            aa+="<br>"
            aa+=str(i)+": "
            aa+=color
        #ここにJSONを整えてDBにいれとく
        #成功したよ。か、失敗したよ。を返す。
        #aa=json.dumps(aa)
            #json_lines = [ json.loads(s) for s in str(request.body) if s != "" ]
        aa+="</small>"
        return HttpResponse(aa)

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



