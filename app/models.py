from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name


class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    Url=models.URLField()

    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=50)

    def __str__(self):
        return self.author