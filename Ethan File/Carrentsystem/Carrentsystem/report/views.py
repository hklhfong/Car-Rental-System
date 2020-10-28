from report.models import Report
from django.shortcuts import render
#render_to('report: monthly_report.html')
def report(request):
    num1 = Report.objects.all().order_by('-total_rent_january', 'headline')[:3]
    num2 = Report.objects.all().order_by('-total_rent_february', 'headline')[:3]
    num3 = Report.objects.all().order_by('-total_rent_march', 'headline')[:3]
    num4 = Report.objects.all().order_by('-total_rent_april', 'headline')[:3]
    num5 = Report.objects.all().order_by('-total_rent_may', 'headline')[:3]
    num6 = Report.objects.all().order_by('-total_rent_june', 'headline')[:3]
    num7 = Report.objects.all().order_by('-total_rent_july', 'headline')[:3]
    num8 = Report.objects.all().order_by('-total_rent_august', 'headline')[:3]
    num9 = Report.objects.all().order_by('-total_rent_september', 'headline')[:3]
    num10 = Report.objects.all().order_by('-total_rent_october', 'headline')[:3]
    num11 = Report.objects.all().order_by('-total_rent_november', 'headline')[:3]
    num12 = Report.objects.all().order_by('-total_rent_december', 'headline')[:3]
    return render(request, 'contents/monthly_report.html', {'num1': num1, 'num2' :num2
    ,'num3':num3, 'num4' :num4, 'num5' :num5, 'num6' :num6, 'num7' :num7
    , 'num8': num8, 'num9' :num9, 'num10' :num10, 'num11' :num11, 'num12' :num12})

