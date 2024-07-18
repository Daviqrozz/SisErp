from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from companies.models import Entreprise

# Dados do usuario
class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


# Logica de Permissao
# Grupo das empresas(Representa o cargo da empresa)
class Group(models.Model):
    name = models.CharField(max_length=150)
    enterprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)


# Logica das permissões que cada grupo de empresa tera
class Group_Permissions(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


# Logica das permissoes de funcionario()
class User_Groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Group, on_delete=models.CASCADE)
