import django_filters
from django_filters import FilterSet
from .models import Video, Category


class VideoFilter(FilterSet):
    id_category = django_filters.ModelChoiceFilter(label="Категория", queryset=Category.objects.all())
    name = django_filters.CharFilter(label="")

    class Meta:
        model = Video
        fields = ('id_category', 'name')
