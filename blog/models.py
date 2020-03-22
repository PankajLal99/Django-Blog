from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Private"),
    (1,"Publish")
)
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover= models.ImageField(upload_to='pictures',default='pictures/DEF.jpg')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title