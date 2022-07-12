from django.db import models
import uuid

# Create your models here.

class Links(models.Model):
    url_original = models.URLField(unique=True)
    url_curta = models.CharField(max_length=10, unique=True)

    # def __str__(self):
    #     return self.url_original

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.url_curta = uuid.uuid4((self.url_original))
    #     super(Links, self).save(*args, **kwargs)