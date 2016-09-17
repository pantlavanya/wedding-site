from django.db import models
from soul.models import SoulModel

# Create your models here.
class Config(SoulModel):
    key = models.CharField(max_length=50, unique=True, db_index=True)
    value = models.TextField(null=True)

    class Meta:
        app_label = "config"
        db_table = "config_config"

    def __unicode__(self):
        return self.key

    def save(self, force_insert=False, force_update=False, using=None):
        self.key = self.key.upper().replace(" ","")
        super(Config, self).save(force_insert, force_update, using)