from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('signup/',views.SignUpPage,name='signup'),
    #path('signup/home',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('homepage/',views.predictor,name='predictor'),
    path('homepage/result/',views.result,name='result'),
    path('enquiry',views.Enquirys,name='enquiry'),
    path('sample',views.display,name='sample'),
    path('about',views.AboutPage,name='about'),
    path('howtouse',views.HowToUse,name='howtouse')
    #path('user',views.users),
    #path('admin/', admin.site.urls),
]
