from projects.models import Project
from django.shortcuts import render

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'nbar':'project',
        'projects':projects
    }

    return render(request,'proyectos.html',context)

def project_description(request,pk):
    project=Project.objects.get(pk=pk)
    context = {
        'nbar':'project',
        'project':project
    }

    return render(request,'detalle_proyecto.html',context)