from django.core.mail import send_mail
from django.db.models.functions import datetime

from mailing_app.models import Mailing


def prepair_mailing():
    current_date = datetime.datetime.now().date()
    mailing_list = Mailing.objects.filter(mailing_status="created", start_time__lte=current_date,
                                          finish_time__gte=current_date)
    mailing_end = Mailing.objects.filter(mailing_status='launched', finish_time__lt=current_date)
    #print(f'mailing_list - {mailing_list}: mailing_end - {mailing_end} .!.')
    if mailing_list.exists():
        for mail in mailing_list:
            mail.mailing_status = Mailing.MAILING_STATUS[2][0]
            mail.save()

    if mailing_end.exists():
        for mail in mailing_end:
            mail.mailing_status = Mailing.MAILING_STATUS[0][0]
            mail.save()


def get_mailing():
    mailing_list = Mailing.objects.filter(mailing_status="launched")
    return mailing_list


def schedule(frequency):
    def wrap():
        prepair_mailing()
        mailing_dail = get_mailing().filter(frequency=frequency)
        #print(f'hi {mailing_dail}')
        for mail in mailing_dail:
            send_mail(subject=mail.email.subject, message=mail.email.body, from_email=None,
                      recipient_list=[client.email for client in mail.client.all()])

    return wrap


def schedule_daily():
    """Еженедельный CRON"""
    schedule('daily')()


def schedule_weekly():
    """Еженедельный CRON"""
    schedule('weekly')()


def schedule_monthly():
    """Ежемесячный CRON"""
    schedule('monthly')()
