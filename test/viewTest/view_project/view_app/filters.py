from django_filters import FilterSet
from .models import TestTable


class TestFilter(FilterSet):
    class Meta:
        model = TestTable
        fields = ('name', 'number')
