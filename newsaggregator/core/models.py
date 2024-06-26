from django.db import models
from django.conf import settings

class Headline(models.Model):
  title = models.CharField(max_length=200)#title char(200)
  image = models.URLField(null=True, blank=True)#image
  url = models.TextField()
  def __str__(self):
    return self.title
  
class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.headline.title}"
