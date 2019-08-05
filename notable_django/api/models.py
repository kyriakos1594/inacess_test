from django.db import models
import uuid

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = MyUUIDModel()

def __str__(self):
        return '%s %s %s %s' % (self.title, self.body,self.created_at, self.unique_id)

