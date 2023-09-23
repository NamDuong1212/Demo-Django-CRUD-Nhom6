from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length = 300)
    
class Meta:
    db_table = 'Blog'
