from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

from bugtracker.models import Ticket
from bugtracker.forms import SignInForm, SignUpForm, CreateTicketForm

@login_required
def index(request):
    html = 'index.html'
    new = Ticket.objects.filter(status='New').order_by('-date_created')
    in_progress = Ticket.objects.filter(status='In Progress').order_by('-date_created')
    done = Ticket.objects.filter(status='Done').order_by('-date_created')
    invalid = Ticket.objects.filter(status='Invalid').order_by('-date_created')
    
    return render(request, html, {
        'new': new,
        'in_progress': in_progress,
        'done': done,
        'invalid': invalid
    })

def login_view(request):
    html = 'form.html'
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    else:
        if request.method == 'POST':
            form = SignInForm(data=request.POST)
            if form.is_valid():
                    login(request, form.get_user())
                    return HttpResponseRedirect('/')

        else:
            form = SignInForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'form.html', {'form': form})

@login_required
def ticket_view(request, id):
    html = 'ticket.html'
    ticket = Ticket.objects.filter(pk=id)

    return render(request, html, {
        'ticket': ticket,
        'current_user_id': request.user.id})


@login_required
def create_ticket_view(request):
    html = 'form.html'

    if request.method == 'POST':
        form = CreateTicketForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                status=data['status'],
                submitted_by=request.user,
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateTicketForm()
    return render(request, html, {'form': form})

@login_required
def edit_ticket_view(request, id):
    html = 'form.html'
    instance = Ticket.objects.get(id=id)

    if request.method == 'POST':
        form = CreateTicketForm(
            request.POST,
            instance=instance
            )
        form.save()

        if instance.status == 'New':
            instance.status == 'New'
            instance.completed_by = None
            form.save()
        elif instance.status == 'In Progress':
            instance.assigned_to = None
            instance.assigned_to = instance.submitted_by
            instance.completed_by = None
            form.save()
        elif instance.status == 'Done':
            instance.completed_by = instance.assigned_to
            instance.assigned_to = None
            form.save()
        elif instance.status == 'Invalid':
            instance.assigned_to = None
            instance.completed_by = None
            form.save()
        elif instance.assigned_to is not None:
            instance.status = 'In Progress'
            instance.completed_by = None
            form.save()
        return HttpResponseRedirect(reverse('home'))

    form = CreateTicketForm(instance=instance)
    return render(request, html, {'form': form})



@login_required
def user_view(request,id):
    html = 'user.html'

    user = User.objects.get(pk=id)
    submitted_by = Ticket.objects.filter(submitted_by=user)
    assigned_to = Ticket.objects.filter(assigned_to=user)
    completed_by = Ticket.objects.filter(completed_by=user)

    return render(request, html, {
        'user': user,
        'submitted_by: ': submitted_by,
        'assigned_to: ': assigned_to,
        'completed_by:': completed_by  
    })

class UserProfileView(DetailView):
    model = User
    slug_field = "username"
    template_name = "user.html"
    

def index(request):
    html = 'index.html'
    new = Ticket.objects.filter(status='New').order_by('-date_created')
    in_progress = Ticket.objects.filter(status='In Progress').order_by('-date_created')
    done = Ticket.objects.filter(status='Done').order_by('-date_created')
    invalid = Ticket.objects.filter(status='Invalid').order_by('-date_created')
    
    return render(request, html, {
        'new': new,
        'in_progress': in_progress,
        'done': done,
        'invalid': invalid
    })