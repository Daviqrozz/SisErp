from rest_framework.views import APIView

from companies.models import Entreprise


class Base(APIView):
    def get_enterprise_id(self, user_id):

        enterprise = {
            "is_owner": False,
            "permissions": []
            }

        #Verifica se o ID digitado existe o campo 'is_owner' (FAlSE OU TRUE) associado ao ID
        Entreprise["is_owner"] = Entreprise.objects.filter(user_id=user_id).exists()

        #Se estiver associado como TRUE retorna o nome da empresa
        if enterprise["is_owner"]:
            return enterprise
