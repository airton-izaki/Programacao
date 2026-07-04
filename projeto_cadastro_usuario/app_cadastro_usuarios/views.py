from django.shortcuts   import render
from app_cadastro_usuarios.models             import Usuario

def home(request):

    # suarios/home.html -> página que iraá exibir a informação de usuários
    return render(request, 'usuarios/home.html')

def usuarios(request):

    # Salvando usuário no banco
    novo_usuario = Usuario()   
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()

    # Exibir os usuários cadastrados
    usuarios = {
        'usuario': Usuario.objects.all()
    }

    # Retornar os ados para a págian de lsitagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
