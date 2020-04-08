from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    path('destination/Mumbai',views.destinationMumbai,name ='destinationMumbai'),
    path('destination/Hyderabad',views.destinationHyderabad,name ='destinationHyderabad'),
    path('destination/Chennai',views.destinationChennai,name ='destinationChennai'),
    path('destination/Pune',views.destinationPune,name ='destinationPune'),
    path('destination/Bangalore',views.destinationBangalore,name ='destinationBamgalore'),
]