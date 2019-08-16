
from django.shortcuts import render,redirect
from .form import PokemonForm
from .models import Pokemon
from .form import UserInfoForm
from django.contrib.auth import authenticate,login




# Create your views here.


def Tatti(request):
    return render(request,'index.html')


def poki (request):
    if request.method == "GET":
        form = PokemonForm()
        return render(request, 'pokipost.html', {'form': form})
    else:
       if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
           try:
               form.save()
               return redirect('/show')
           except:
             pass



def shows(request):
    pokemons = Pokemon.objects.all()
    return render(request,'show.html',{'pokemons':pokemons})



def sudhaar(request,id):
    if request.method == "GET":
      pokemons = Pokemon.objects.get(id=id)
      return render(request,'edit.html',{'Pokemons':pokemons})


def update(request,id):
    pokemons = Pokemon.objects.get(id=id)
    form = PokemonForm(request.POST, instance=pokemons)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'pokemons': pokemons})


def destroy(request, id):
    pokemons = Pokemon.objects.get(id=id)
    pokemons.delete()
    return redirect("/show")



def about(request):
    return render(request,'other.html')



def contact(request):
    return render(request,'relative_url_template.html')


def register(request):
    if request.method == "GET":
        form = UserInfoForm()
        return render(request, 'registration.html', {'form': form})
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
           try:
               form.save()
           except:
             pass
        return render(request,'registration.html')




def user_login(request):
    if request.method =='GET':
        form = UserInfoForm()
        return render(request,'login.html',{'form':form})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(username=username, password=password, email=email)
        print(username,password,email)
        if user:
                login(request,user)
                return render(request, 'index.html')




