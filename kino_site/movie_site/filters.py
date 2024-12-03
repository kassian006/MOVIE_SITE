from django_filters import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['exact'],
            'year': ['gt', 'lt'],
            'genre': ['exact'],
            'status_movie': ['exact'],
            'actor':['exact'],
            'director': ['exact']
        }