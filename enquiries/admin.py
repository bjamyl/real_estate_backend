from django.contrib import admin
from .models import Enquirie

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing','inquiry_date', 'email')
    list_display_links = ('id', 'listing')
    search_fields = ('listing',)


admin.site.register(Enquirie,InquiryAdmin)
