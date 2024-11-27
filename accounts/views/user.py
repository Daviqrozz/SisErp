from accounts.views.base import Base
from accounts.models import User
from accounts.serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetUser(Base):
    permision_classes = [IsAuthenticated]

    def get(self,request) -> Response:

        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response({"error": "Usuário não encontrado"}, status=404)

        enterprise = self.get_enterprise_user(user.id)

        serializer = UserSerializer(user)

        return Response({
            "user":serializer.data,
            "enterprise":enterprise,
        })