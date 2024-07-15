from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  exit,iniciosesion, registro
urlpatterns = [
    path('logout/', exit, name='logout'),
    path('login/', iniciosesion, name='login'),
    path('registro/', registro, name='registro'),
   path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
