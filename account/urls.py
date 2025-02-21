from django.urls import path
from .views import createProject, enterTran, Taccount

urlpatterns = [
    path('createproject/', createProject, name = 'createProject'),
    path('projectdetails/', enterTran, name = 'enterTran'),
    path('accounttype/', Taccount, name='Taccount'),
]