from django.urls import path
from .views import createProject, enterTran, Taccount, viewstatement, viewallproject

urlpatterns = [
    path('createproject/', createProject, name = 'createProject'),
    path('projectdetails/<int:project_id>/', enterTran, name='enterTran'),
    path('acctype/', Taccount, name='Taccount'),
    path("viewstatement/", viewstatement, name="viewstatement"),
    path("viewallproject/", viewallproject, name="viewallproject"),
]