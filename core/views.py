from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render
from .forms import UsersForm

def aboutme(request):
    return HttpResponse("Welcome to My SSHHI")

def courseD(request,shid):
    return HttpResponse(shid)

def htmlv(request):
    # data={
    #     'list':['hello','mam','you'],
    #     'numbers':[],
    #     'std_d':[
    #         {'name':'sharif','phone':'0172'},
    #         {'name':'rahim','phone':'1223'}
            
    #     ]}
    
    return render(request,"index.html")

def shoesId(request):
    if request.method=="GET":
        output=request.GET['output']
        

    return render(request,"shoes.html",{'output':output})


def userForm(request):
    finalans=0
   
    fn=UsersForm()
    data={'form':fn}
    try:
        if request.method=='POST':
            n3=int(request.POST['num1'])
            n4=int(request.POST['num2'])
            finalans=n3+n4
            data={
                'form':fn,
                'output':finalans
            }
            url="/shoes/?output={}".format(finalans)
            return  HttpResponseRedirect(url)
            
    except:
        pass    
        
    return render(request,'index1.html',data)


def submitForm(request):
    return HttpResponse(request)

def calculator(request):
    c=''
    try:
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            
            if opr=="+":
                c=n1+2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="invalid opr>>>"
    print(c)        
    return render(request,'calculator.html',{'output':c})