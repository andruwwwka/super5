from django.contrib import admin
from blogs.models import Post


class PostAdmin(admin.ModelAdmin):

    exclude = ['author', ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
