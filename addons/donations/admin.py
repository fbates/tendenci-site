from django.contrib import admin
from addons.donations.models import Donation
from addons.donations.forms import DonationAdminForm

class DonationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'donation_amount', 'payment_method']
    form = DonationAdminForm

admin.site.register(Donation, DonationAdmin)
