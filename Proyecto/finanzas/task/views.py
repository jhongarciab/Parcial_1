from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Esta función representa la vista de la página de inicio de la aplicación de tareas. 
    Renderiza la plantilla 'home.html' y la  devuelve como respuesta.
    """
    return render(request, 'home.html')

def signup(request):
    """
    Esta función maneja tanto la solicitud GET como la solicitud POST para el registro de usuarios. 
    Si la solicitud es GET, renderiza la plantilla 'signup.html' junto con el formulario de registro UserCreationForm. 
    Si la solicitud es POST, verifica que las contraseñas ingresadas coincidan. Si coinciden, crea un nuevo usuario utilizando 
    el modelo User de Django y lo redirige a la vista de tareas ('task'). Si hay un error de integridad, significa que el nombre de 
    usuario ya existe y se renderiza la plantilla 'signup.html' con un mensaje de error. Si las contraseñas no coinciden, se renderiza 
    la plantilla 'signup.html' con un mensaje de error.
    """
    if request.method  == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })
    
def signin(request):
    """
    Esta función maneja tanto la solicitud GET como la solicitud POST para el inicio de sesión de los usuarios. Si la solicitud es GET, 
    renderiza la plantilla 'signin.html' junto con el formulario de inicio de sesión AuthenticationForm. Si la solicitud es POST, autentica 
    al usuario utilizando el nombre de usuario y la contraseña proporcionados. Si la autenticación es exitosa, inicia sesión en la aplicación 
    y redirige al usuario a la vista de tareas ('task'). Si la autenticación falla, se renderiza la plantilla 'signin.html' con un mensaje de error.
    """
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, 
                     username=request.POST['username'],
                     password=request.POST['password'] )
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('task')
    
@login_required    
def task(request):
    """
    Esta función representa la vista de las tareas pendientes del usuario. Recupera las tareas filtradas por el usuario actual y 
    donde la fecha de finalización (datecompleted) sea nula. Las tareas se ordenan en orden descendente según la fecha de finalización. 
    Luego, renderiza la plantilla 'task.html' junto con las tareas recuperadas y las devuelve como respuesta.
    """
    task = Task.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
    return render(request, 'task.html', {
        'task': task
    })

@login_required 
def task_completed(request):
    """
    Esta función representa la vista de las tareas completadas del usuario. Recupera las tareas filtradas por el usuario actual y donde 
    la fecha de finalización (datecompleted) no sea nula. Luego, renderiza la plantilla 'completed_task.html' junto con las tareas recuperadas 
    y las devuelve como respuesta.
    """
    task = Task.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'completed_task.html', {
        'task': task
    })

@login_required 
def create_task(request):
    """
    Esta función maneja tanto la solicitud GET como la solicitud POST para crear una nueva tarea. Si la solicitud es GET, 
    renderiza la plantilla 'create_task.html' junto con el formulario TaskForm vacío. Si la solicitud es POST, valida el 
    formulario enviado y crea una nueva instancia de Task relacionada con el usuario actual. Si la información proporcionada no 
    es válida, se renderiza la plantilla 'create_task.html' con un mensaje de error.
    """
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Información no válida'
            })

@login_required 
def task_detail(request, task_id):
    """
    Esta función maneja tanto la solicitud GET como la solicitud POST para ver y actualizar los detalles de una tarea específica. 
    Si la solicitud es GET, se recupera la tarea correspondiente al task_id proporcionado, verificando que pertenezca al usuario actual. 
    Luego, se crea una instancia de TaskForm con los detalles de la tarea y se renderiza la plantilla 'task_detail.html' junto con la tarea 
    y el formulario. Si la solicitud es POST, se intenta guardar los cambios realizados en el formulario. Si los cambios son válidos, 
    se redirige al usuario a la vista de tareas ('task'). Si hay un error de valor, significa que los datos ingresados no son válidos y 
    se renderiza la plantilla 'task_detail.html' con un mensaje de error.
    """
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': "Error al actualizar tarea"
            })

@login_required 
def complete_task(request, task_id):
    """
    Esta función maneja la solicitud POST para marcar una tarea como completada. Se recupera la tarea correspondiente al task_id proporcionado, 
    verificando que pertenezca al usuario actual. Si la solicitud es POST, se establece la fecha de finalización de la tarea como el tiempo 
    actual utilizando timezone.now() y se guarda la tarea. Luego, se redirige al usuario a la vista de tareas ('task').
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('task')

@login_required 
def delete_task(request, task_id):
    """
    Esta función maneja la solicitud POST para eliminar una tarea. Se recupera la tarea correspondiente al task_id proporcionado, 
    verificando que pertenezca al usuario actual. Si la solicitud es POST, se elimina la tarea y se redirige al usuario a la vista de tareas ('task').
    """
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task')

@login_required 
def signout(request):
    """
    Esta función maneja la solicitud POST para cerrar sesión de un usuario. Cierra la sesión actual utilizando 
    logout(request) y redirige al usuario a la página de inicio ('home').
    """
    logout(request)
    return redirect('home')

