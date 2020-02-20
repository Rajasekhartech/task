from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
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
