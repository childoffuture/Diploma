from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import redirect
from .models import Video, Subscription
from .forms import VideoForm
from .filters import VideoFilter


class BaseView(ListView):
    model = Video
    template_name = "index.html"
    context_object_name = 'videos'
    ordering = ['-created']
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VideoFilter(self.request.GET, queryset=self.init_queryset())
        return context

    def init_queryset(self):
        return self.get_queryset()


class SubscriptionView(LoginRequiredMixin, BaseView):
    def init_queryset(self):
        return Video.objects.filter(id_category__in=Subscription.objects.filter(id_user=self.request.user).values('id_category'))


class RecommendView(LoginRequiredMixin, BaseView):
    def init_queryset(self):
        return Video.objects.filter(pk__in=Video.objects.all().order_by('-created').values('pk')[:5])


class MyVideoView(LoginRequiredMixin, BaseView):
    def init_queryset(self):
        return Video.objects.filter(id_author=self.request.user)


class AddView(LoginRequiredMixin, CreateView):
    template_name = "add.html"
    form_class = VideoForm

    def post(self, request, *args, **kwargs):
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.id_author = request.user
            video.save()

        return redirect("/")


class VideoView(DetailView):
    pass
