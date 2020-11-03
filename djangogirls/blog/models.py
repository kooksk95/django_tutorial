from django.db import models
from django.conf import settings
from django.utils import timezone

#모델을 정의
class Post(models.Model):
	# 각 필드의 데이터타입
	## ForeignKey: 다른 모델에 대한 링크
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #
    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def __str__(self):
    	return self.title
