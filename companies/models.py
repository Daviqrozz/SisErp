from django.db import models

#Cadastro de empresas
class Enterprise(models.Model):
    name = models.CharField(max_length=175)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
#Cadastro de funcionario 
class Employee(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise,on_delete=models.CASCADE)

