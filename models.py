class Report(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Message(models.Model):
	sender = models.ForeignKey()
	receiver = models.ForeignKey()
	message = models.TextField() #store encrypted text in this textfield