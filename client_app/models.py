from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='контактный email')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ['id']
