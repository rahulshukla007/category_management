from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerRegistration, Customerlogin, CategoryForm, ProductForm
from .models import User, Category, Product
from django.contrib import messages




def userLogin(request):
    if request.method == "POST":
        #print(request.POST)
        fm = Customerlogin(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            #print(email)
            password = fm.cleaned_data['password']
            #print(password)
            try:
                loginData = User.objects.get(email=email, password=password)
                #print(loginData)
                #print(loginData.email)
                
                #adding id in session
                print(loginData.id)
                request.session['login_user'] = loginData.id
                return redirect('category/')

            except User.DoesNotExist:
                return render(request, 'account/login.html', {'form':fm})
    else:
        fm = Customerlogin()
        

    return render(request, 'account/login.html', {'form':fm})

def userRegistrtion(request):
    if request.method == "POST":
        print(request.POST)
        fm = CustomerRegistration(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['firstname']
            #print(fname)
            lname = fm.cleaned_data['lastname']
            #print(lname)
            email = fm.cleaned_data['email']
            #print(email)
            password = fm.cleaned_data['password']
            #print(password)
            re_password = fm.cleaned_data['rpassword']
            #print(re_password)

            try:
                reg = User(fname = fname, lname = lname, email = email, password = password)
                reg.save()
                return redirect('/')

            except Exception as e:
                print(e)
                messages.error(request,'Email already exist')

    else:
       fm = CustomerRegistration()

    return render(request, 'account/registration.html', {'form':fm})


def categoryManagement(request):
    loginUser = request.session.get('login_user')
    print(loginUser)
    if loginUser != None:
        if request.method == "POST":
            #print(request.POST)
            fm = CategoryForm(request.POST)
            if fm.is_valid():
                c_name = fm.cleaned_data['category_name']
                print(77777777777777777)
                print(c_name)
                
                ctgry = Category(category_name = c_name, user_id = loginUser)
                ctgry.save()
        
        fm = CategoryForm()
        cat_obj = Category.objects.filter(user_id=loginUser)
        print(cat_obj)
        
        print(fm)

        return render(request, 'account/categorymanagement.html', {'form':fm, 'cat_obj':cat_obj})
    return redirect('/')

def logout(request):
    try:
        del request.session['login_user']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def deleteCategory(request,id=None):
    #request.GET["id"]
    print(id)
    instance = Category.objects.get(id=id)
    instance.delete()
    return redirect('/category/')


