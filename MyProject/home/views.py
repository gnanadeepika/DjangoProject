from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from home.models import Post,Friend
from home.forms import HomeForm

class Homeview(TemplateView):
    template_name = "home/home.html"

    def get(self,request):
        form=HomeForm()
        posts=Post.objects.all().order_by('-created')
        users=User.objects.exclude(id=request.user.id)
        friend=Friend.objects.get(current_user=request.user)
        friends=friend.users.all()
        args={'form':form,'posts':posts,'users':users,'friends':friends}
        return render(request,self.template_name,args)

    def post(self,request):
        form=HomeForm(request.POST)

        if form.is_valid():
            text=form.cleaned_data['post']
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            form=HomeForm()
            posts=Post.objects.all()
            args={'form':form,'posts':posts}
        #args={'form':form}
        return render(request,self.template_name,args)

def change_friend(request,operator,pk):
    new_friend=User.objects.get(pk=pk)
    if operator == "add":
        Friend.make_friend(request.user,new_friend)
    elif operator == "remove":
        Friend.lose_friend(request.user,new_friend)
    return redirect('home:home')