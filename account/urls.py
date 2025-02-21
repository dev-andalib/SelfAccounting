from django.urls import path
from .views import createProject, enterTran, Taccount, viewstatement, viewallproject, view_inv

urlpatterns = [
    path('createproject/', createProject, name = 'createProject'),
    path('projectdetails/', enterTran, name = 'enterTran'),
    path('acctype/', Taccount, name='Taccount'),
    path("viewstatement/", viewstatement, name="viewstatement"),
    path("viewallproject/", viewallproject, name="viewallproject"),
    path("view_inv/", view_inv, name="view_inv"),
]