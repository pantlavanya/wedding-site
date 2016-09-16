from django.db import models
from django.contrib.auth.models import User
from custom_middleware.current_user import get_current_user
from django.utils import timezone

# Create your models here.
class SoulModel(models.Model):
    created_by = models.ForeignKey(User, editable=False, default=None, blank=True, null=True, related_name="%(class)s_created_by", db_index=True)
    updated_by = models.ForeignKey(User, editable=False, default=None, null=True, blank=True, related_name="%(class)s_updated_by")
    created_at = models.DateTimeField(editable=False, default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        abstract = True
        get_latest_by = 'created_at'

    def save(self, force_insert=False, force_update=False, using=None):
        if getattr(self, 'id', None):
            self.updated_by = get_current_user()
        else:
            self.created_by = get_current_user()
        super(SoulModel, self).save(force_insert, force_update, using)
