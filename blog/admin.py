from django.contrib import admin
from .models import About, Author,Contribute, Blog, UserComment
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
  pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass


@admin.register(Contribute)
class ContributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    pass


