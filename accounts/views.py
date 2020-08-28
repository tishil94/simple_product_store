from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product
from .forms import ProductForm



# Create your views here.
def enter(request):
 return render(request, 'index.html')

def index(request):
 return render(request, 'index.html')

def home(request):
 products = Product.objects.all()
 return render(request, 'home.html', {'products': products})

def supuser(request):
 products = Product.objects.all()
 return render(request, 'admin.html',  {'products': products})


def register(request):
     if request.method == 'POST':  
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password0']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username = username, password = password1, email = email)
                user.save();
                print('User created')
                return redirect('enter')
                
        else:
            print('password not matching')
            return redirect('register')
        return redirect('signin')

     else:
        return render(request, 'register.html')
#  return render(request, 'register.html')

def signin(request):
    #if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['Password']

        user = auth.authenticate(username = username, password = password)
        if user.is_superuser:
            auth.login(request, user)
            return redirect('supuser')
        elif user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid details')
            return render(request, 'index.html')
    #else:
        #return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

    # product actions

def create_product(request):
     form = ProductForm(request.POST or None)

     if form.is_valid():
         form.save()
         return redirect('supuser')
    
     return render(request, 'products_form.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect ('supuser')
    return render(request, 'products_form.html', {'form': form, 'product':product})

def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect ('supuser')
    return render(request, 'prod_delete_confirm.html', {'product':product})
    
def admin_search(request):
     if request.method == 'POST':
         num = request.POST.get('id')
         products = Product.objects.filter(id = num)
         return render(request, 'admin.html', {'products':products})
     else:
         return render(request, 'admin.html')