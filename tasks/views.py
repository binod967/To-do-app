from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task

# Create your views here.
# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    query = request.GET.get('q', '')
    priority = request.GET.get('priority', '')

    tasks = Task.objects.filter(user=request.user)

    if query:
        tasks = tasks.filter(title__icontains=query)

    if priority:
        tasks = tasks.filter(priority=priority)

    pending = tasks.filter(completed=False)
    completed = tasks.filter(completed=True)

    return render(request, 'tasks/dashboard.html', {
        'pending_tasks': pending,
        'completed_tasks': completed,
        'pending_count': pending.count(),
        'completed_count': completed.count(),
        'query': query,
    })

# Add Task view
@login_required
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            category=request.POST.get('category', ''),
            priority=request.POST.get('priority', '')
        )

        return redirect('dashboard')
    return render(request, 'tasks/add_task.html')

# delete Task view
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')

#Toggle satus view
@login_required
def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')



