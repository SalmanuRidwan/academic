from django.db import models

DONATION_STATUS = [
    ('Pending', 'Pending'),
    ('Transferred', 'Transferred'),
    ('Failed', 'Failed'),
]


class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=DONATION_STATUS, default='Pending')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    payment_reference = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Donation from {self.donor_name} - ${self.amount}"

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'


class Beneficiary(models.Model):
    name = models.CharField(max_length=255)
    need_description = models.TextField()
    required_funds = models.DecimalField(max_digits=10, decimal_places=2)
    received_funds = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Beneficiaries'

class FundAllocation(models.Model):
    # donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    allocation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.allocated_amount} from {self.donor} to {self.beneficiary}"
