from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from accounts.models import User_Groups, Group_Permissions
from companies.models import Enterprise, Employee

# Define a classe Base que herda de APIView
class Base(APIView):
    # Define o método get_enterprise_user que recebe um user_id como parâmetro
    def get_enterprise_user(self, user_id):
        # Inicializa o dicionário enterprise com is_owner como False e uma lista vazia de permissions
        enterprise = {
            "is_owner": False,
            "permissions": []
        }

        # Verifica se o usuário é proprietário de uma empresa
        enterprise['is_owner'] = Enterprise.objects.filter(user_id=user_id).exists()

        # Se o usuário for proprietário, retorna o dicionário enterprise
        if enterprise['is_owner']: return enterprise

        # Tenta obter o primeiro objeto Employee associado ao user_id
        employee = Employee.objects.filter(user_id=user_id).first()

        # Se não encontrar um funcionário, lança uma exceção APIException
        if not employee: raise APIException("Este usuário não é um funcionário")

        # Obtém todos os grupos aos quais o usuário pertence
        groups = User_Groups.objects.filter(user_id=user_id).all()

        # Itera sobre cada grupo ao qual o usuário pertence
        for g in groups:
            group = g.group

            # Obtém todas as permissões associadas ao grupo
            permissions = Group_Permissions.objects.filter(group_id=group.id).all()

            # Itera sobre cada permissão e adiciona ao dicionário enterprise na lista permissions
            for p in permissions:
                enterprise['permissions'].append({
                    "id": p.permission.id,
                    "label": p.permission.name,
                    "codename": p.permission.codename
                })

        # Retorna o dicionário enterprise com as informações do usuário
        return enterprise
    
   
