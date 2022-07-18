from django.views.generic import ListView, DetailView
from .models import TestTable
from .filters import TestFilter


class TestListView(ListView):
    model = TestTable
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-number']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TestFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TestDetailView(DetailView):
    model = TestTable
    template_name = 'post.html'
    context_object_name = 'post'
