from django.contrib import admin
from .models import Profile, Posting, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Posting)
admin.site.register(Comment)