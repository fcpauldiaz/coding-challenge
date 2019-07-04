from django.db import models

# Create your models here.
class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.content