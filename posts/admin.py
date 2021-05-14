from django.contrib import admin
from .models import PostComment,PostLike,Post
# Register your models here.


admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(Post)
