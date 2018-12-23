from django.contrib import messages
from ..forms import UserRegistrationForm

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic.edit import FormView


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, 'Successfully registered.')
        return redirect('home')
