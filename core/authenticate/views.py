from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView

# Create your views here.


class LoginInterfaceView(LoginView):
    template_name = 'authenticate/sign-in.html'

    def get_success_url(self):
        return super().get_success_url()
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')  # Reemplaza 'home' con la URL a la que deseas redirigir al usuario después de iniciar sesión
        return super().dispatch(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'authenticate/sign-out.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/account/login')
        return super().dispatch(request, *args, **kwargs)


class Authorized(LoginRequiredMixin, TemplateView):
    template_name = 'authenticate/authorized.html'
    
    