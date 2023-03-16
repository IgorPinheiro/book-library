from django.shortcuts import render
from django.http import HttpResponse
from . models import Usuario
from django.shortcuts import redirect 
from hashlib import sha256

def login(requst):
    return HttpResponse('Login')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    password = request.POST.get('password')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(password) < 8:
        return redirect('/auth/cadastro/?status=2') 

    if len(usuario) > 0:
        return redirect('/auth/cadastro/status=3')
    try:
        password = sha256(password.encode()).hexdigest()
        usuario = Usuario(nome = nome, 
                          email = email, 
                          password = password)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

    # return HttpResponse(f'{nome=} {email=} {password=}')

