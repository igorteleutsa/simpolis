
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

from .forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
