from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from videoportal.models import Chat


class ChatView(LoginRequiredMixin, DetailView):
    model = Chat
    template_name = 'chat.html'
    context_object_name = 'chatView'
