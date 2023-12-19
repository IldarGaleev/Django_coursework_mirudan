from django.contrib import admin

from mailing_app.models import Mailing, MessageMailing


class MessageMailingInline(admin.StackedInline):
    model = Mailing
    readonly_fields = ['id']
    filter_horizontal = ['client']
    extra = 1
    can_delete = True


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'finish_time', 'frequency', 'mailing_status', 'email']
    search_fields = ['start_time', 'finish_time', 'frequency', 'mailing_status']
    filter_horizontal = ['client']
    inlines = [
        #MessageMailingInline,
    ]

@admin.register(MessageMailing)
class MessageMailingAdmin(admin.ModelAdmin):
    list_display = ['subject']
    search_fields = ['subject']
    inlines = [
         MessageMailingInline,
    ]
