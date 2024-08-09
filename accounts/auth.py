# Bilbioteca de exceções
from rest_framework.exceptions import AuthenticationFailed, APIException

# Biblioteca de criptografias
from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User
from companies.models import Enterprise,Employee

# Logicas de autenticação
class Authentication:

    def signin(self, email=None, password=None) -> User:
        
        # Verifica se existe um usuário com o email fornecido
        user_exists = User.objects.filter(email=email).exists()
        
        exception_auth = AuthenticationFailed("Email ou senha estão incorretos")

        # Se o usuário não existir ou a senha estiver incorreta, lança uma exceção
        if not user_exists or not check_password(password):
            raise exception_auth

        # Recupera a primeira instância de User com o email fornecido
        user = User.objects.filter(email=email).first()

        # Verifica se a senha fornecida está correta comparando com a senha armazenada do usuário
        if not check_password(password, user.password):
            raise exception_auth

        # Retorna o usuário se a autenticação for bem-sucedida
        return user

    # Metodo de cadastro
    def signup(self, email, name, password, type_account="owner", company_id=False):
        #Condição de nome vazio
        if not name or name == "":
            raise APIException("Nome nao pode ser nulo")
        #Condição de email vazio
        if not email or email == "":
            raise APIException("Email nao pode ser nulo")
        #Condição de senha vazio
        if not password or password == "":
            raise APIException("A senha nao pode ser nulo")
        
        #Verifica se o campo de id da empresa esta preenchido,se o tipo de usuario selecionado for dono
        if type_account and not company_id:
            raise APIException("O id da empresa precisa ser definido") 
            

        user = User

        #Verifica de o email ja existe
        if user.objects.filter(email=email).exists():
            raise APIException("O email ja esta cadastrado na plataforma")
        
        password_hashed = make_password(password)

        #Metodo de criar usuario
        created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            #Verifica de o usuario que sera criado sera um funcionario ou dono
            is_owner=0 if type_account == 'employee' else 1
        )

        #Metodo de criar usuario tipo dono
        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name='Nome da empresa',
                user_id=created_user.id
            )
        
        #Metodo de criar usuario tipo funcionario
        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id=company_id or created_enterprise.id,
                user_id=created_user.id
            )
            
        return created_user
            
