
from django.shortcuts import render, redirect
#from django.http import HttpRequest
from django.http import HttpResponse
#from django.template import RequestContext
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . import models
User=''
def index(request):
    template = loader.get_template('findWork/index.html')
    context={}
    return HttpResponse(template.render(context,request))
    #assert isinstance(request, HttpRequest)
    #return render(request,'index.html')

def post(request):
    if request.method == 'POST':
       nuevo2=models.User.objects.filter(Username=request.POST['userN']).exists()
       if(not nuevo2):
            nuevo= models.User()
            nuevo.FirstName=request.POST['firstN']
            nuevo.LastName=request.POST['lastN']
            nuevo.Password=request.POST['pass']
            nuevo.Username=request.POST['userN']
            nuevo.Phone=request.POST['conta']
            request.session['member_id']=nuevo.id
            request.session['password']=nuevo.Password
            request.session['username']=nuevo.Username
            nuevo.save()
            template = loader.get_template('findWork/User.html')
            context={}
            return HttpResponse(template.render(context,request))

       else:
            messages.warning(request, 'User already exist')
            template = loader.get_template('findWork/index.html')
            context={}

            return redirect('/findWork/home/')


def postWork(request):


    if request.method == 'POST':
        nuevo= models.Works()
        auxiliar=models.User.objects.filter(id=request.session['member_id']).first()
        nuevo.Description=request.POST['description']
        nuevo.Type=request.POST['work']
        nuevo.StartDate=request.POST['startdate']
        nuevo.Finaldate=request.POST['finaldate']
        nuevo.Price=request.POST['price']
        nuevo.Address=request.POST['address']
        nuevo.UserBoss=auxiliar
        nuevo.UserEmployee=auxiliar

        nuevo.save()
    nuev3=models.User.objects.filter(Username=request.session['username'])
    template = loader.get_template('findWork/postWork.html')
    context={'userName2':nuev3}
    return HttpResponse(template.render(context,request))

def postLogIn(request):
    if request.method == 'POST':
      if("username" in request.session):
          data=models.Works.objects.filter(UserBoss=request.session['member_id'])
          template = loader.get_template('findWork/User.html')
          nuevo=models.User.objects.filter(Username=request.session['username'])
          context={'userName2':nuevo,'data':data}
          return HttpResponse(template.render(context,request))
      else:
         nuevo=models.User.objects.filter(Username=request.POST['userNa'],Password=request.POST['passw']).first()
         if(nuevo is not None):
            if (nuevo.Password ==request.POST['passw']):
                request.session['member_id']=nuevo.id
                request.session['password']=nuevo.Password
                request.session['username']=nuevo.Username
                data=models.Works.objects.filter(UserBoss=request.session['member_id'])
                template = loader.get_template('findWork/User.html')
                nuevo=models.User.objects.filter(Username=request.session['username'])
                context={'userName2':nuevo,'data':data}
                return HttpResponse(template.render(context,request))
         else:
            messages.warning(request, 'Wrong User')
            return redirect('/findWork/home/')



    #template = loader.get_template('findWork/index.html')
    #context={}
    #return HttpResponse(template.render(context,request))

def PublicWorks(request):
    print(request.session['member_id'])
    if request.method == 'POST':
       nuevo= models.Works()
       auxiliar=models.User.objects.filter(id=request.session['member_id']).first()
       nuevo.Description=request.POST['description']
       nuevo.Type=request.POST['work']
       nuevo.StartDate=request.POST['startdate']
       nuevo.Finaldate=request.POST['finaldate']
       nuevo.Price=request.POST['price']
       nuevo.Address=request.POST['address']
       nuevo.UserBoss=auxiliar
       nuevo.UserEmployee=auxiliar

       nuevo.save()

    template = loader.get_template('findWork/User.html')
    context={}
    return HttpResponse(template.render(context,request))

def ShowWorks(request):
    nuev3=models.User.objects.filter(Username=request.session['username'])
    if(request.method=='GET'):
        if(request.GET.get('filtro') is None):
            data=models.Works.objects.raw("SELECT * FROM findwork_works WHERE UserBoss_id!= %s AND UserBoss_id=UserEmployee_id",[request.session['member_id']])
            w=models.Works.objects.raw("SELECT id,Type FROM findwork_works GROUP BY id,Type")
            template = loader.get_template('findWork/ShowWorks.html')
            nuev3=models.User.objects.filter(Username=request.session['username'])
            context={'data':data,'ejemplo':w,'userName2':nuev3}
            return HttpResponse(template.render(context,request))
        if(request.GET.get('filtro')!=('filter')):
            nuevo2=models.Works.objects.raw("SELECT * FROM findwork_works WHERE Type=%s  AND UserBoss_id!=%s",[request.GET.get('filtro'),request.session['member_id']])
        else:

            nuevo2=models.Works.objects.all()

        w=models.Works.objects.raw("SELECT id,Type FROM findwork_works GROUP BY id,Type")
        template = loader.get_template('findWork/showWorks.html')

        context={'data':nuevo2,'ejemplo':w,'userName2':nuev3}
        return HttpResponse(template.render(context,request))
    elif(request.method=='POST'):

        query1='%'+request.POST['query']+'%'
        print(query1)
        w2=models.Works.objects.raw("SELECT * FROM findwork_works WHERE  UserBoss_id!= %s AND Description LIKE %s",[request.session['member_id'],query1])
        w=models.Works.objects.raw("SELECT id,Type FROM findwork_works GROUP BY id,Type")
        sw=0;
        for x in w2:
            sw=1;
        if(sw==0):
            context={'data':0,'ejemplo':w,'userName2':nuev3}
        else:
            context={'data':w2,'ejemplo':w,'userName2':nuev3}
        template = loader.get_template('findWork/showWorks.html')
        return HttpResponse(template.render(context,request))

    else:
        data=models.Works.objects.raw("SELECT * FROM findwork_works WHERE UserBoss_id!= %s AND UserBoss_id=UserEmployee_id",[request.session['member_id']])


def logOut(request):
    del request.session['member_id']
    del request.session['username']
    del request.session['password']
    return redirect('/findWork/home/')

def User(request):
    nuevo2=models.Works.objects.filter(UserBoss=request.session['member_id'])
    template = loader.get_template('findWork/User.html')
    nuev3=models.User.objects.filter(Username=request.session['username'])
    context={'data':nuevo2,'userName2':nuev3}
    return HttpResponse(template.render(context,request))

def queryfilters(request):
    nuev3=models.User.objects.filter(Username=request.session['username'])
    if(request.method=='GET'):

        if(request.GET.get('filtro')!=('filter')):
            nuevo2=models.Works.objects.raw("SELECT * FROM findwork_works WHERE Type=%s  AND UserBoss_id!=%s",[request.GET.get('filtro'),request.session['member_id']])
        else:
            nuevo2=models.Works.objects.all()

        w=models.Works.objects.raw("SELECT id,Type FROM findwork_works GROUP BY id,Type")
        template = loader.get_template('findWork/showWorksFilter.html')

        context={'data':nuevo2,'ejemplo':w,'userName2':nuev3}
        return HttpResponse(template.render(context,request))
    if(request.method=='POST'):
        query1='%'+request.POST['query']+'%'
        print(query1)
        w2=models.Works.objects.raw("SELECT * FROM findwork_works WHERE  UserBoss_id!= %s AND Description LIKE %s",[request.session['member_id'],query1])
        w=models.Works.objects.raw("SELECT id,Type FROM findwork_works GROUP BY id,Type")
        sw=0;
        for x in w2:
            sw=1;
        if(sw==0):
            context={'data':0,'ejemplo':w,'userName2':nuev3}
        else:
            context={'data':w2,'ejemplo':w,'userName2':nuev3}
        template = loader.get_template('findWork/showWorksFilter.html')
        return HttpResponse(template.render(context,request))
    context={}
    template = loader.get_template('findWork/ShowWorks.html')
    return HttpResponse(template.render(context,request))


def workDetails(request,id):
    s=str(id)
    nuev3=models.User.objects.filter(Username=request.session['username'])

    w2=models.Works.objects.raw("SELECT * FROM findwork_works,findwork_user=d WHERE findwork_works.id = %s AND d.id=findwork_works.UserBoss_id",[s])
    if(request.method=='POST'):
        nuev=models.Works.objects.filter(id=id).first()
        work=models.applicant()
        work.UserBoss1=nuev.UserBoss
        work.UserEmployee1=nuev.UserEmployee
        work.WorkID=nuev

        work.save()

                ## hacer update aqui
        #UserEmployee con el requestsession.id

        context={'data':w2,'sw':0,'userName2':nuev3}

    else:
        context={'data':w2,'sw':1,'userName2':nuev3}
    template = loader.get_template('findWork/workDetails.html')
    return HttpResponse(template.render(context,request))

def delete(request):
    #if request.method == 'POST':
    data=models.Works.objects.filter(UserBoss=request.session['member_id'])
    models.Works.objects.filter(id=request.POST['delete']).delete()
    template = loader.get_template('findWork/User.html')
    context={'data':data,'username':request.session['username']}
    return HttpResponse(template.render(context,request))

def sendToUpdateView(request):
    work = models.Works.objects.filter(id=request.POST['update'])
    template = loader.get_template('findWork/updateWork.html')
    context={'username':request.session['username'],'work':work}
    return HttpResponse(template.render(context,request))

def updateWork(request):
    work = work = models.Works.objects.filter(id=request.POST['update']).update(Type=request.POST['type'] ,Description = request.POST['description'],StartDate = request.POST['startDate'],Finaldate = request.POST['startDate'],Price = request.POST['price'])

    data=models.Works.objects.filter(UserBoss=request.session['member_id'])
    print(data)
    template = loader.get_template('findWork/User.html')
    context={'username':request.session['username'],'data':data}
    return HttpResponse(template.render(context,request))


def Applicant(request,id):
    s=str(id)
    nuev3=models.User.objects.filter(Username=request.session['username'])

    w2=models.Works.objects.raw("SELECT * FROM findwork_works,findwork_user=d WHERE findwork_works.id = %s AND d.id=findwork_works.UserBoss_id",[s])
    work=models.Works.objects.raw("SELECT * FROM findwork_applicant,findwork_user=s WHERE UserEmployee1_id=s.id AND WorkID_id=%s",[str(id)])
    template = loader.get_template('findWork/myWorkDetail.html')
    context={'data':w2,'userName2':nuev3,'User':work}
    return HttpResponse(template.render(context,request))
