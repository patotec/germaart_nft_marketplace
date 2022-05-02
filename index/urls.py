from django.urls import path
from . import views

app_name = 'indexurl'

urlpatterns = [
    path('',  views.myindex ,name='index'),
    path('mint-nft/<slug>/', views.mynft , name='nft'),
     path('category/<slug>/', views.mycat , name='cat'),
    path('mint-mannualy/', views.mycon , name='man'),
    path('payment/<slug>/', views.myfund , name='pay'),
    path('contact/',  views.mycontact ,name='contact'),
    path('about-us/',  views.myabout ,name='about'),
	path('privacy_policy/',  views.myprivate ,name='private'),
   
]
