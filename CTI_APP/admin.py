from django.contrib import admin
from .models import CtiLog
from .models import BlackListIP
from .models import BlackListURL




@admin.register(CtiLog)
class CtiLogAdmin(admin.ModelAdmin):
    list_display = ('cve', 'signature', 'description', 'response_measures')


@admin.register(BlackListIP)
class BlackListIP(admin.ModelAdmin):
    list_display = ('ip_source', 'attack_date', 'country_source')

@admin.register(BlackListURL)
class BlackListIP(admin.ModelAdmin):
    list_display = ('url_source', 'attack_date')


