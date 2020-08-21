from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

