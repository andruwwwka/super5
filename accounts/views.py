from django.contrib import auth
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from pinax.notifications.models import send
from rest_framework import generics, permissions

from accounts.forms import (
    RegistrationForm, LoginForm
)
from .serializations import UserSerializer


class RegisterView(TemplateView):

    template_name = "register.html"

    def __init__(self):
        super(RegisterView, self).__init__()
        self.form = RegistrationForm()

    def get_context(self, request, *args, **kwargs):
        context = {
            'form': self.form
        }
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context(request))

    def post(self, request, *args, **kwargs):
        self.form = RegistrationForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            user = auth.authenticate(username=self.form.user.email, password=self.form.str_password)
            auth.login(request, user)
            send([user], 'registration')
            return HttpResponseRedirect("/accounts/personal-data-master/")
        return self.render_to_response(self.get_context(request))


class LoginView(TemplateView):
    template_name = "signin.html"

    def __init__(self):
        super(LoginView, self).__init__()
        self.form = LoginForm()

    def get_context(self, request, *args, **kwargs):
        context = {
            'form': self.form
        }
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context(request))

    def post(self, request, *args, **kwargs):
        self.form = LoginForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            user = auth.authenticate(
                email=self.form.user.email,
                password=self.form.str_password
            )
            auth.login(request, user)
            del request.POST['email']
            del request.POST['password']
            return redirect('index_page')
        else:
            return self.render_to_response(self.get_context(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return auth.get_user_model().objects.filter(id=user.id)
