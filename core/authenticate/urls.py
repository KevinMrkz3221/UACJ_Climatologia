from django.urls import path

from .views import LoginInterfaceView, LogoutInterfaceView, Authorized

urlpatterns = [
    path('sign-in/', LoginInterfaceView.as_view(), name='sign-in'),
    path('sign-out/', LogoutInterfaceView.as_view(), name='sign-out'),
    path('authorized/', Authorized.as_view(), name='authorized')
]