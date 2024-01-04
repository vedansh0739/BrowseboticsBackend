from django.urls import path

from . import views

urlpatterns = [

    path("initiator/",views.initiator, name="initiator"),
    path("process/",views.process, name="process"),
    path("test/",views.test, name="test"),
    path("goback/",views.goback, name="goback")

]