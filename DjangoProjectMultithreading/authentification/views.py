from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def add_error(self, field, error):
        if field == '__all__':
            error = "Неправильний логін або пароль"
        super().add_error(field, error)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Реєстрація пройшла успішно!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentification/register.html', {'form': form})
'''
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вітаємо, {username}!")
                return redirect('index')
            else:
                messages.error(request, "Неправильний логін або пароль")
        else:
            messages.error(request, "Неправильний логін або пароль")
    form = AuthenticationForm()
    return render(request, 'authentification/login.html', {'form': form})
'''
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вітаємо, {username}!")
                return redirect('/representation/menu')
        else:
            messages.error(request, "Неправильний логін або пароль")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentification/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Ви вийшли з системи.")
    return redirect('login')
