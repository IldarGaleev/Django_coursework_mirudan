from django.contrib import admin

from mailing_app.models import Mailing, MessageMailing


class MessageMailingInline(admin.StackedInline):
    model = MessageMailing
    max_num = 1
    min_num = 1
    can_delete = True


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'finish_time', 'frequency', 'mailing_status']
    search_fields = ['start_time', 'finish_time', 'frequency', 'mailing_status']
    filter_horizontal = ['client']
    inlines = [
        MessageMailingInline,
    ]

# @admin.register(MessageMailing)
# class MessageMailingAdmin(admin.ModelAdmin):
#     list_display = ['subject']
#     search_fields = ['subject']
