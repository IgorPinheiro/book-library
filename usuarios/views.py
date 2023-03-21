from django.shortcuts import render
from django.http import HttpResponse
from . models import Usuario
from django.shortcuts import redirect 
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status}) 
    

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

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
        return redirect('/auth/cadastro/?status=3')
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

def valida_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(password = password)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/book/home/?id_usuario={request.session["usuario"]}')
     
     #return HttpResponse(f'{email= }, {password= }')
def sair(request):
    request.session.flush()
    return redirect('/auth/login/')

   


