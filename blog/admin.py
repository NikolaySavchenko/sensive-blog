from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author',)
    raw_id_fields = ('post',)

admin.site.register(Post)
admin.site.register(Tag)
