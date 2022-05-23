from pydoc import describe
from django.db import models

# Create your models here.


class Faculty(models.Model):
    facultyName = models.CharField(max_length=250)
    facultyImage = models.ImageField(upload_to='facultyimg', null=True)
    facultyDesignation = models.CharField(max_length=250)
    facultyQualification = models.CharField(max_length=250)
    facultyPhone = models.CharField(max_length=250)
    facultyEmail = models.EmailField(max_length=250)
    facultyCv = models.FileField(upload_to='facultycv')
    facultyPublications = models.URLField(max_length=250, null=True)

    def __str__(self):
        return self.facultyName


class Noticeboard(models.Model):
    noticeTitle = models.CharField(max_length=250)
    noticeFile = models.FileField(upload_to='noticeboard')
    noticeTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.noticeTitle


class Tender(models.Model):
    tenderTitle = models.CharField(max_length=250)
    tenderFile = models.FileField(upload_to='tender')
    tenderTime = models.DateField(auto_now=True)

    def __str__(self):
        return self.tenderTitle


class Gallery(models.Model):
    eventName = models.CharField(max_length=250)
    eventDate = models.DateField(auto_now=True)
    gallerUrl = models.URLField(max_length=500, null=True)
    galleryThumbnail = models.FileField(upload_to='gallery')

    def __str__(self):
        return self.eventName


class Convocation(models.Model):
    convocationTitle = models.CharField(max_length=250)
    convocationDate = models.DateField(auto_now=True)
    convocationgallerUrl = models.URLField(max_length=500, null=True)
    convocationgalleryThumbnail = models.FileField(upload_to='convocation')

    def __str__(self):
        return self.convocationTitle
