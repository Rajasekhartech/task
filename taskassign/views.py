from django.shortcuts import render
from .models import tasks
from django.http import Http404 , HttpResponseRedirect
from django.views.generic import View
from .forms import TaskForm


# Create your views here.
def home(request):
    context ={}
    task = tasks.objects.all()
    context['task'] = task
    context['title'] = 'tasks'
    return render(request, "home.html", context)

def task_detail(request, id = None):
    context = {}
    try:
        task = tasks.objects.get(id = id)
    except:
        raise Http404
    context['task'] = task
    return render(request, "task/task_detail.html" , context)

class TaskView(View):
    def get(self,request):
        task_form = TaskForm(instance=tasks())
        template ="task/new_task.html"
        context ={'task_form' : task_form}
        return render(request,template,context)

    def post(self,request):
        task_form = TaskForm(request.POST ,instance=tasks())
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.created_by = request.user
            new_task.save()
            return HttpResponseRedirect("/")
        context = {"task_form" : task_form}
        return render(request, 'task/new_task.html', context)





