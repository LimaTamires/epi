from django.shortcuts import render, redirect
from nucleo.models import Colaborador, Setor

def home(req):
    colaboradores = Colaborador.objects.all()
    return render(req, 'nucleo/index.html', {
        'colaboradores': colaboradores,
    })

def tela_criar(req):
    if req.method == 'GET':
        return render(req, 'nucleo/forms/criar.html')
    elif req.method == 'POST':
        nome = req.POST.get('nome')
        cpf = req.POST.get('cpf')

        colaborador = Colaborador(
            nome=nome,
            cpf=cpf,
        )

        colaborador.save()

        return redirect('nucleo-inicial')

def setor(req):
    if req.method=='GET':
        return render(req, 'nucleo/forms/setor.html')
    elif req.method=='POST':
        setor = req.POST.get('setor')

        setor=Setor(
            nome = setor,
        )

        setor.save()

        return redirect('nucleo-inicial')

   
