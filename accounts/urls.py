from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', creation_page, name='log_reg_page'),
    path('Registration/', create_account, name='Registration'),
    path('login_url/', login_url, name='login'),
    path('logout/', logout_user, name='logout'),
    path('my_profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('user_profile/<int:pk>', user_profile, name='user_profile'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),

]
