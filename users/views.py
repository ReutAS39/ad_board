from django.contrib import messages
from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView

from ads.utils import DataMixin
from users.forms import RegisterUserForm, LoginUserForm
from users.tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Спасибо за подтверждение email.')
        return redirect('login')
    else:
        messages.error('Ссылка для активации не верна.')

    return redirect('post_list')

def activateEmail(request, user, to_email):
    mail_subject = 'Подтверждение регистрации'
    message = render_to_string('email.html', {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'<b>{user.username}</b>, проверь свой e-mail и нажми на ссылку для активации и  \
                завершения регистрации')
    else:
        messages.error(request, f'Письмо на {to_email} не отправлено.')


class UserRegister(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active=False
        user.save()
        #login(self.request, user)
        activateEmail(self.request, user, form.cleaned_data.get('email'))
        return redirect('post_list')

class UserLogin(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')