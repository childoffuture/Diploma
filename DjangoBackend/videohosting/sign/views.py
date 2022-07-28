from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import RegisterForm

import urllib.request


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        #get_url = urllib.request.urlopen('https://dimp89@mail.ru:JJORe3EbVcsN2tgQAY8lVX775F77@gate.smsaero.ru/v2/sms/send?number=79000000000&text=Hello&sign=MyTube')
        #print("Response Status: " + str(get_url.getcode()))
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect("/sign/login/")
