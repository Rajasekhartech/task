from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from .models import Profile
import sys
# Create your views here.

def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'employees/index.html',context)

def employee_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id = id)
    return render(request,'employees/details.html',context)


class MyProfile(DetailView):
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('home_page'))



        else:
            context['error'] = "Provide valid credentials !!!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

def employee_add(request):
    context = {}
    print("jksadfkjnas", request.POST)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",user.profle)
            user.profile.depatments_in_organization = user_form.cleaned_data.get('depatment_in_organization')
            user.save()
            print("sjadhfkjhdsasdfgsdfasdf",user.profile.depatments_in_organization)
            # profile_id = Profile.objects.latest("id")
            # print("DDDDDDDDDDDDDDDDDDDDDDDDDD.........",profile_id)
            # Profile.objects.filter(id=profile_id).update(depatments_in_organization=request.POST.depatments_in_organization)
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employees/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'employees/add.html',context)