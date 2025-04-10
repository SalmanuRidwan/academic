from django.contrib import admin
from .models import Beneficiary, FundAllocation

admin.site.register(Beneficiary)
admin.site.register(FundAllocation)
