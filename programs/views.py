from django.shortcuts import render, redirect
from .models import ProgrammingLanguage

def program_list(request):
    programs = ProgrammingLanguage.objects.all()
    return render(request, 'programs/program-list.html', {'programs': programs})

def program_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            ProgrammingLanguage.objects.create(title=title, description=description)
            return redirect('programs:program_list')
    return render(request, 'programs/program-form.html')
