from django.shortcuts import render
from datetime import datetime
from .models import Noticeboard, Tender, Gallery, Convocation, Faculty, Upcominglectures, Officeorder
# Create your views here.

# ============comman data to sent on the page============ #
notice_board = Noticeboard.objects.all()
current_datetime = datetime.now()
tender_data = Tender.objects.all()
galleryData = Gallery.objects.all()
convocationData = Convocation.objects.all()
facultyData = Faculty.objects.all()
upcomingLect = Upcominglectures.objects.all()
officeOrderData = Officeorder.objects.all()
context = {
    'site_title': 'योजना तथा वास्तुकला विद्यालय विजयवाड़ा | School of Planning And Architecture Vijayawada',
    'current_datetime': current_datetime,
    'notice_board': notice_board,
    'tender_data': tender_data,
    'galleryData': galleryData,
    'convocationData': convocationData,
    'facultyData': facultyData,
    'upcomingLect': upcomingLect,
    'officeOrderData': officeOrderData,
}
# ============comman data to sent on the page============ #


def home(request):
    return render(request, 'home.html', context,)


def noticeboard(request):
    return render(request, 'noticeboard.html', context,)


def tender(request):
    return render(request, 'tender.html', context,)


def gallery(request):
    return render(request, 'gallery.html', context,)


def convocation(request):
    return render(request, 'convocation.html', context,)


def faculty(request):
    return render(request, 'faculty.html', context,)


def upcominglectures(request):
    return render(request, 'upcominglectures.html', context,)


def officeorder(request):
    return render(request, 'officeorder.html', context,)


def courseoffered(request):
    return render(request, 'courseoffered.html', context,)
