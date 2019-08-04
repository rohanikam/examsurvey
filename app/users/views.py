from django.shortcuts import render
from .forms import RegisterForm


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views, decorators
from django.contrib.messages.views import SuccessMessageMixin


from django.contrib.auth.mixins import UserPassesTestMixin



from users.models import CustomUser

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views.generic import DeleteView

                      


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages




@login_required
def profile(request):
    if request.method == 'POST':         
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        
    }
    
    return render(request,'profile.html',context)





class LoginView(SuccessMessageMixin,UserPassesTestMixin, views.LoginView):
  template_name = "users/login.html"
  success_message = "You are successfully logged in."

  def test_func(self):
    try:
      if self.request.user.is_authenticated:
        return False
    except:
      pass
    return True




class RegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"
    success_message = "You have been successfully registered," \
                      " login with your email and password."

    def get(self, request, *args, **kwargs):

        # Prevent already logged in user from this page
        if self.request.user.is_authenticated:
            return redirect("/")
        
        return super(RegisterView, self).get(request, *args, **kwargs)


class PasswordChangeView(SuccessMessageMixin, views.PasswordChangeView):
    success_message = "Your password has been successfully changed."


class PasswordResetConfirmView(SuccessMessageMixin,
                               views.PasswordResetConfirmView):
    success_message = "Your new password has been set," \
                      " login with email and new password."
