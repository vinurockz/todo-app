from django.shortcuts import render,redirect
from .forms import create,UpdateTodoForm,Registration_Form,Login_form
from .models import todoitem
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login_require(func):
    def wrapper(req,*args,**kwargs):
        if not req.user.is_authenticated:
            return redirect("log")
        else:
            return func(req,*args,**kwargs)
    return wrapper

@login_require
def create_view(req,*args,**kwargs):

        context = {}
        f = create(initial={"users":req.user})
        context["f"]=f
        if req.method=="POST":
            f=create(req.POST)
            if f.is_valid():
                t_name=f.cleaned_data.get("task_name")
                s=f.cleaned_data.get("status")
                u=f.cleaned_data.get("users")
                print(t_name,f,u)
                users=todoitem(task_name=t_name,status=s,users=u)
                users.save()
                return redirect("list")

        return render(req,"create.html",context)


@login_require
def list_view(req,*args,**kwargs):

        todos=todoitem.objects.filter(users=req.user)
        context={}
        context["todo"]=todos
        return render(req,"list.html",context)

@login_require
def delete_view(req,*args,**kwargs):
    id = kwargs.get("id")
    todo=todoitem.objects.get(id=id)
    todo.delete()
    return redirect("list")
@login_require
def update_view(req,*args,**kwargs):
    id=kwargs.get("id")
    Todo=todoitem.objects.get(id=id)
    form=UpdateTodoForm(instance=Todo)
    context={}
    context["form"]=form
    if req.method=="POST":
        form=UpdateTodoForm(instance=Todo,data=req.POST)
        if form.is_valid():
            form.save()
        return redirect("list")
    return render(req,"update.html",context)

def registration_view(req):
    form=Registration_Form()
    context={}
    context["form"]=form
    if req.method=="POST":
        form=Registration_Form(req.POST)
        if form.is_valid():
            form.save()
            print("Reister New User")
            return redirect("log")
        else:
            print("Error")
    return render(req,"registration.html",context)

def Login_Page(req):
    form=Login_form()
    context={}
    context["form"]=form
    if req.method=="POST":
        form=Login_form(req.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(req,username=username,password=password)
            if user:
                login(req,user)
                return redirect("home")
            else:
                return redirect("log")

    return render(req, "login.html", context)

def Logout_page(req):
    logout(req)
    return redirect("log")

def Home_Page(req):
    return render(req,"home.html")
