from django.contrib import admin
from .models import Post

# Register your models here.
## 관리자페이지에 추가되는 것입니다.
admin.site.register(Post)