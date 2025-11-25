from django.db import models

class bookinstance(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=30
    )

    author = models.CharField(
        verbose_name='автор',
        max_length=20
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name='количество',

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    