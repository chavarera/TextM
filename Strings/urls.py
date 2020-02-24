from . import views
from django.urls import path
print("File Called")
urlpatterns=[
    path("",views.index,name='Index'),
    path("Methods/<obj>",views.Methods,name="Methods"),
    path("Details/<btn_id>",views.Details,name="Details"),
]