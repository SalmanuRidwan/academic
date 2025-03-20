from django.db.models.signals import post_save
from django.dispatch import receiver
from information.models import Report
from volunteer.models import Task

@receiver(post_save, sender=Report)
def create_task_from_report(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(
            title=f"Task for Report: {instance.title}",
            description=instance.description,
            location=instance.location,
            required_skills=", ".join([tag.name for tag in instance.tags.all()]),
            report=instance,
        )
