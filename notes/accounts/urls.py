from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user-registration/',views.registration_view,name="register"),
    path('logout',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login'),
]

