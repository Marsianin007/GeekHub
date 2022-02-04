from django.db import models


CATEGORY_CHOICES = (
        ('newstories', 'newstories'),
        ('jobstories', 'jobstories'),
        ('showstories', 'showstories'),
        ('askstories', 'askstories'),
    )


class MyModel(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='none')

    def __str__(self):
        return self.category


class AskModel(models.Model):

    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    kids = models.TextField()
    score = models.CharField(max_length=200)
    text = models.TextField()
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.post_id}'


class ShowModel(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    kids = models.TextField()
    score = models.CharField(max_length=200)
    text = models.TextField()
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.post_id}'


class JobModel(models.Model):
    by = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    text = models.TextField()
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.post_id}'


class NewsModel(models.Model):
    by = models.CharField(max_length=200)
    descendants = models.CharField(max_length=200)
    post_id = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.TextField()
    kids = models.TextField()

    def __str__(self):
        return f'{self.post_id}'
