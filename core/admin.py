from django.contrib import admin
from .models import Movie, Profile, CustomUser, Video

admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Video)

