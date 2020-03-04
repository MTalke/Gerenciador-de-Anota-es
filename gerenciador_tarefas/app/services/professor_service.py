from ..models import Professor

def cadastrar_professor(professor):

    Professor.objects.create(
        nome = professor.nome,
        senha = professor.senha,
        confirmarSenha = professor.confirmarSenha
    )