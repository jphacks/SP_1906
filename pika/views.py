from django.shortcuts import render
import json
from django.http.response import JsonResponse, HttpResponse
from django.http import QueryDict, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Tree

@ensure_csrf_cookie
# Create your views here.
#index
#tree
#about
#post
#waitinglist

def tree(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"tree.html",params)

def about(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"about.html",params)

def post(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"post.html",params)

def waitinglist(request):
    params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",}
    return render(request,"waitinglist.html",params)


def index(request):
    if request.method=="GET":
        params={
            "title":"ddtree",
            "goto": "table",
            "goto2": "canvas",
        }
        return render(request, "index.html", params)
    else:
        return HttpResponse("please get to this page")



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
        aa=""
        print(request.POST[str(0)])
        for i in range(93):
            aaa = request.POST[str(i)]
            color = aaa.replace("rgb","")
            color = aaa.replace("#","0x")
            aa+="\r"
            aa+=color
        if len(aa)!=837:
            return HttpResponse("data unproperly sent. please post it again.")
        else:
            name = request.POST["name"]
            category = request.POST["category"]
            treedata = Tree(data=aa, name=name, look=category)
            treedata.save()
            print("record has created!")
            print(str(request.POST["name"]))
            print(str(request.POST["category"]))
            return HttpResponse("楽しみだね！")





def posted(request):
    if request.method =="POST":
        a="aa"
        
        params={a:1}
        return render(request, "done.html", params)

def esp(request):
    if request.method == "GET":
        #params={a:1,b:2}
        #ret={"1":"#ffff00","2":"#ffa500"}
        ret=""
        for j in range(93):
            ret+="000"
            ret+='\r'
            ret+="255"
            ret+='\r'
            ret+="000"
            ret+='\r'
        print(ret)
        #ret="#ff0000"+"\r"+"#123456"+"\r"+"#098123"+"\r"+"#098654"
        return  HttpResponse(ret)   

def stats(request):
    if request.method == "GET":
        return render(request, "stats.html")



