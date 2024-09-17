from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'Index.html', {'title': title})

def about(request):
    return render(request, 'About.html')

def Hello(request, username):
    return HttpResponse("<h2>Hello %s </h2>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, 'projects/Projects.html', {'projects': projects})

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/Tasks.html', {'tasks': tasks})

def taskJson(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {'project': project, 'tasks': tasks})