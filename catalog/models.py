from django.db import models
from django.urls import reverse


class BookInstance(models.Model):
    """Класс книги, производный от класса Model."""
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

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ["name"]

    # Methods
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
     
    def __str__(self):
        return self.name




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
        ordering = ["name"]
