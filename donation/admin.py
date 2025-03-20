from django.contrib import admin
from .models import Donor, Beneficiary, FundAllocation

admin.site.register(Donor)
admin.site.register(Beneficiary)
admin.site.register(FundAllocation)
