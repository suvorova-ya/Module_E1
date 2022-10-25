from django.db import models



class Post(models.Model):

    title = models.CharField(max_length=40, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержание')
    slug = models.SlugField(max_length=250,unique=True, db_index=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')


    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email