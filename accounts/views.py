from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from accounts.forms import SignupForm


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


'''
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
'''

signup = CreateView.as_view(model=User,
                            form_class=SignupForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')
