from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import ReportForm
from .models import Report, Media

def home(request):
    return render(request, "information_home.html")

def twitter(request):
    return render(request, 'twitter.html')

def geolocation(request):
    return render(request, 'geolocation.html')

def user_content(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        media_files = request.FILES.getlist('file')

        if form.is_valid():
            report = form.save(commit=False)
            report.save()

            for file in media_files:
                Media.objects.create(report=report, file=file)

            return redirect('reports')
    else:
        form = ReportForm()

    return render(request, 'user_content.html', {'form': form})

def reports(request):
    reports = Report.objects.all()
    return render(request, 'reports.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_detail.html', {'report': report})

def ai_analysis(request):
    return render(request, 'ai_analysis.html')