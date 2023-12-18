import datetime

from mailing_app.models import Mailing

current_date = datetime.datetime.now()

mailing_list = Mailing.objects.filter(mailing_status='created', start_time__lt=current_date,
                                      finish_time__gt=current_date)

if mailing_list.exists():
    for mail in mailing_list:
        mail.mailing_status = Mailing.MAILING_STATUS[2]
        mail.save()



# def schedule_job():
#     print('test')
