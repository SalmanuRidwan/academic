from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportForm
from .models import Media, Report


def home(request):
    return render(request, "information_home.html")

def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        files = request.FILES.getlist('file')

        if form.is_valid():
            report = form.save()
            for f in files:
                Media.objects.create(report=report, file=f)
            return redirect('report_success')
    else:
        form = ReportForm()
    return render(request, 'submit_report.html', {'form': form})

def report_success(request):
    return render(request, 'report_success.html')

def reports(request):
    reports = Report.objects.order_by('-created_at')
    return render(request, 'reports.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_detail.html', {'report': report})
