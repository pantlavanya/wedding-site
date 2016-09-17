from django.db import models
from soul.models import SoulModel
import uuid
from django.conf import settings
import os

def sort_files_by_extension(self, filename):
    fname, extension = os.path.splitext(filename)
    self.original_name = filename
    self.modified_name = str(uuid.uuid4()) + str(extension)
    return settings.MEDIA_ROOT + "/images/" + self.uses + "/" + self.modified_name


# Create your models here.
class Images(SoulModel):

    uses_choices = (('SLIDER_IMAGE','SLIDER IMAGE'),
                     ('PROFILE_IMAGE','PROFILE IMAGE'),
                     ('ADVERTISEMENT_IMAGE', 'ADVERTISEMENT IMAGE'),
                     ('OTHER_IMAGE','OTHER IMAGE'))

    uses = models.CharField(max_length=50, null=True, choices=uses_choices, db_index=True)
    path = models.ImageField(null=True, upload_to=sort_files_by_extension, max_length=500, verbose_name="Upload")
    original_name = models.CharField(null=True, max_length=200, editable=False)
    modified_name = models.CharField(null=True, max_length=200, unique=True, db_index=True, editable=False)
    type = models.CharField(max_length=50, null=True)
    dimensions = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=False)
    cron_checked = models.BooleanField(default=False)
    cron_comment = models.TextField(null=True)

    class Meta:
        app_label = "images"
        db_table = "images_images"

    def __unicode__(self):
        return self.modified_name

    def save(self, force_insert=False, force_update=False, using=None):
        super(Images, self).save(force_insert, force_update, using)


