from accounts.views.signup import Signup
from accounts.views.signin import Signin

from django.urls import path

urlpatterns = [
    path('Signin',Signin.as_view()),
    path('Signup',Signup.as_view())
]
