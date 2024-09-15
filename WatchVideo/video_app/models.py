from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='video/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Subtitle(models.Model):
    video = models.ForeignKey(Video, related_name='subtitle', on_delete=models.CASCADE)
    language = models.CharField(max_length=10)
    content = models.TextField()
    