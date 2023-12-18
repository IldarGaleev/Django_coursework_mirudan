from django.db import models

from client_app.models import Client


class Mailing(models.Model):
    FREQUENCY_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    )

    MAILING_STATUS = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
    )

    start_time = models.DateField(verbose_name='начало рассылки')
    finish_time = models.DateField(verbose_name='окончание рассылки')
    frequency = models.CharField(max_length=255, choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    mailing_status = models.CharField(max_length=255, choices=MAILING_STATUS, verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, verbose_name='получатели')


def __str__(self):
    return f'{self.start_time} - {self.finish_time}'


class Meta:
    verbose_name = 'рассылку'
    verbose_name_plural = 'рассылки'
    ordering = ('start_time',)


class MessageMailing(models.Model):
    subject = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='email')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['id']
