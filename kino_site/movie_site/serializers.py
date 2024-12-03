from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']



class DirectorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name','director_bio', 'director_age', 'director_image']


class ActorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class ActorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_bio', 'actor_age', 'actor_image']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieListSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'movie_image', 'status_movie', 'avg_rating']


    def get_avg_rating(self,obj):
        return obj.get_avg_rating()


class MovieMomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class MovieDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    director = DirectorDetailSerializers(many=True)
    actor = ActorDetailSerializers(many=True)
    movie_languages = MovieLanguagesSerializers(many=True, read_only=True)
    movie_moments = MovieMomentsSerializer(many=True, read_only=True)
    comments = RatingSerializers(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'director', 'actor', 'movie_image', 'types',
                  'movie_time', 'description', 'movie_trailer', 'status_movie', 'movie_languages', 'movie_moments',
                  'comments'
]


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'
