from django.shortcuts import render, redirect
from .forms import VolunteerRegistrationForm
from .models import Volunteer
from django.contrib.auth import get_user_model
from information.models import Report
from volunteer.models import Task

User = get_user_model()

def home(request):
    return render(request, "volunteer_home.html")

def volunteer_list(request):
    volunteers = Volunteer.objects.select_related('user').all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})


def match_volunteers_to_task(task):
    report_tags = task.report.tags.all()
    task_required_skills = set(tag.name for tag in report_tags)
    volunteers = Volunteer.objects.filter(is_available=True)

    assigned_volunteers = []
    for volunteer in volunteers:
        volunteer_skills = set(volunteer.skills.split(", "))

        # Check if any of the volunteer's skills match the task's required skills

        # TODO: Location
        # if task_required_skills.intersection(volunteer_skills) and volunteer.location == task.location:
        if task_required_skills.intersection(volunteer_skills):
            assigned_volunteers.append(volunteer)
            task.assigned_volunteers.add(volunteer)
            if len(assigned_volunteers) >= 3:
                break

    task.save()
    return assigned_volunteers

def skill_matching(request):
    if request.method == 'POST':
        reports = Report.objects.filter(status='Open')  # Only open reports
        for report in reports:
            if not Task.objects.filter(report=report).exists():  # Avoid duplicate task creation
                Task.objects.create(
                    title=f"Task for Report: '{report.title}'",
                    description=report.description,
                    location=report.location,
                    required_skills=", ".join([tag.name for tag in report.tags.all()]),
                    report=report,
                )

        # Step 2: Match volunteers to tasks
        tasks = Task.objects.filter(status='Pending')  # Match only pending tasks
        for task in tasks:
            assigned_volunteers = match_volunteers_to_task(task)  # Run matching logic
            if assigned_volunteers:
                task.status = 'In Progress'  # Update task status if volunteers are assigned
            else:
                task.status = 'Pending'  # Task remains pending if no match found
            task.save()

        return render(request, 'skill_success.html')
    else:
        return render(request, 'skill_matching.html')

def chat_room(request):
    return render(request, "chat_room.html")

def task_management(request):
    tasks = Task.objects.all().prefetch_related('assigned_volunteers')  # Prefetch volunteers for efficiency
    return render(request, 'task_management.html', {'tasks': tasks})

def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Try to get or create a user
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': email}
            )

            # If user exists but no Volunteer record, create one
            if not hasattr(user, 'volunteer'):
                volunteer = form.save(commit=False)
                volunteer.user = user
                volunteer.save()
                # # Optional: add a message or redirect
                return redirect('volunteer_thank_you')

            form.add_error(None, 'A volunteer profile already exists for this user.')

    else:
        form = VolunteerRegistrationForm()

    return render(request, 'register_volunteer.html', {'form': form})



def thank_you(request):
    return render(request, 'thank_you.html')

def skill_success(request):
    return render(request, 'skill_success.html')