from django.contrib import admin
from .models import Post, About, Travel, Author, Food
# Register your models here.



# class TravelInline(admin.TabularInline):
#     model = Post.travel_category.through

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    # inlines = [
    #     TravelInline,
    # ]
    pass
    #exclude = ('destination', 'destination_title', 'created_date', 'destination_description')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

    #exclude = ('members',)

# @admin.register(Travel)
# class TravelAdmin(admin.ModelAdmin):
#   pass
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#   inlines = [TravelInline, ]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
  pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass

#
# admin.site.register(Post, PostAdmin)
# admin.site.register(About, AboutAdmin)
# #admin.site.register(Travel)
# admin.site.register(Author, AuthorAdmin)
#
# admin.site.register(Travel, TravelAdmin)


