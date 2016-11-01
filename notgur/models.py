from django.db import models

# Create your models here.
class Image(models.Model):
    created_user = models.ForeignKey("auth.User")
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()

    def comments(self):
        return Comment.objects.filter(image=self)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url

class Comment(models.Model):
    created_user = models.ForeignKey("auth.User")
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image)
