from django.db import models

class BookInstance(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=30
    )

    author = models.ForeignKey(
        'Author',
        on_delete=models.PROTECT,
        
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name='количество',

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Author(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=30,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
