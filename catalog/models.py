from django.db import models
from django.urls import reverse


class BookInstance(models.Model):
    """Класс книги, производный от класса Model."""
    name = models.CharField(
        verbose_name='название',
        max_length=30
    )

    author = models.CharField(
        verbose_name='автор',
        max_length=30,
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