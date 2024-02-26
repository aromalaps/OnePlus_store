from django.urls import path
from .import views

app_name='User'
urlpatterns = [
   
    path('user/',views.register,name='Register'),
    path('login/',views.login,name='Login'),
    path('logout/',views.logout,name='Logout'),
    path('profile/<int:id>',views.UserProfile,name='profile')

]
# url 'User:profile'