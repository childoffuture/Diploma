from django.shortcuts import render
from django.views.generic import CreateView
from .models import Video
from .forms import VideoForm


def index(request):
    video = Video.objects.all()
    return render(request, "index.html", {"video": video})


class AddView(CreateView):
    template_name = "add.html"
    form_class = VideoForm

    def post(self, request, *args, **kwargs):
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

        return render(request, "index.html")

