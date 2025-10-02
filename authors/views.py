from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm


# Create your views here.
def register_view(request):

    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    context = {'form': form, 'form_action': reverse('authors:register_create')}
    return render(request, 'authors/register_view.html', context)



def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    if form.is_valid():
        #1. pegar os dados do form para uma variável caso queira alterar....
        user = form.save(commit = False)
        # a senha pracisa ser criptografada, pego a senha do form e criptografo com a funcao set_password
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário criado com sucesso')
        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect(reverse('authors:register'))


def login_view(request):
    form = LoginForm()
    context = {'form': form, 'form_action': reverse('authors:login_execute') }
    return render(request, 'authors/login.html', context)

def login_execute(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    #request.session['register_form_data'] = POST
    form = LoginForm(POST)
    if form.is_valid():
        auth_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', ''),
        )

        if auth_user:
            messages.success(request, 'loged in!')
            login(request, user=auth_user)
        else:
            messages.error(request, 'Login Inválido')
    else:
        messages.error(request, 'Dados inválidos')

    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    # se o conteúdo do POST username for diferente do username logado
    if request.POST.get('username', '') != request.user.username:
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))
