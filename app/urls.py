from .views import indexView,aboutMe,saveDataView,deleteView,updateViewPage
from django.urls import path 


urlpatterns =[
path("",indexView,name="index"),
path("about-python",aboutMe,name="about"),
path("save-data",saveDataView,name="save-data"),
path("delete-note/<int:id>",deleteView,name="deleteView"),
path("update-note/<int:id>",updateViewPage,name="updateViewPage")
             ]
 
