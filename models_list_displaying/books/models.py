# coding=utf-8
from django.urls import reverse
from django.db import models

# register_converter(converters.DateConverter, 'date')

class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации',  )
   
    

    def __str__(self):
        return self.name + " " + self.author

    def get_absolute_url(self):
        # date=self.pub_date.strftime("%Y-%m-%d")
        return reverse('books', kwargs={'p_date':self.pub_date})