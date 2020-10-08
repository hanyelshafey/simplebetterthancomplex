from django.db import models
from django.utils import timezone

poststatus=([('active','active')
            ,('notactive','notactive')
])

# Create your models here.
class Post (models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    savetime=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='media',null=True)
    email=models.EmailField(null=True)
    poststatus=models.CharField(max_length=50 , choices=poststatus)








    def __str__(self):
        return self.title

    