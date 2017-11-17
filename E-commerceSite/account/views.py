from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from account.forms import RegistrationForm,EditProfileForm
from account.models import UserProfile,User

class HomeView(TemplateView):
    template_name = 'account/home.html'

    def get(self, request):
        return render(request,self.template_name)

@login_required
def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/home')
        else:
            return redirect('/account/change-password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'account/change_password.html',args)

@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'account/view_profile.html',args)

class Register(TemplateView):
    template_name = 'account/register.html'
    def get(self, request):
        form=RegistrationForm()
        args={'form':form}
        return render(request,self.template_name,args)

    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/home')

@login_required
def edit_profile(request):
    get_user = get_object_or_404(User, id=request.user.id)
    instance=get_object_or_404(UserProfile, user=get_user)
    form = EditProfileForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request,'account/view_profile.html',{"user":request.user})
    else:
        return render(request, 'account/edit_profile.html', {'form': form})