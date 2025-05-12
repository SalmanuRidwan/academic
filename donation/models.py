from django.db import models

DONATION_STATUS = [
    ('Pending', 'Pending'),
    ('Transferred', 'Transferred'),
    ('Failed', 'Failed'),
    ('Successful', 'Successful'),
]

FUND_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
)
class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=DONATION_STATUS, default='Pending')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    payment_reference = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Donation from {self.donor_name} - ₦{self.amount}"

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'


class FundRequest(models.Model):
    organization_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    amount_requested = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(help_text="Purpose of the funding")
    status = models.CharField(max_length=10, choices=FUND_STATUS, default='Pending')
    date_requested = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.organization_name} - ₦{self.amount_requested}"
