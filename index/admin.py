from django.contrib import admin
from .models import *




class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user',  'approve']



admin.site.register(Pay_method)
admin.site.register(Bid)
admin.site.register(Nft)
admin.site.register(Category)
admin.site.register(Creator)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Contact)
admin.site.register(Price_logo)
