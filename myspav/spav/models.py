from django.db import models

# Create your models here.


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
