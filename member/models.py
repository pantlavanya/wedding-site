from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from soul.models import SoulModel
from soul.services import soul_email
from django.contrib.auth.hashers import make_password

# Create your models here.
class Member(SoulModel):

    gender_choice = (('','Select'),('male', 'Male'), ('female', 'Female'))
    profile_choice = (('','Select'),
                      ('unmarried','Unmarried'),
                      ('widow_or_widower','Widow or Widower'),
                      ('divorcee', 'Divorcee'))
    marital_choice = (('','Select'),
                      ('self','Self'),
                      ('son','Son'),
                      ('daughter', 'Daughter'),
                      ('brother', 'Brother'),
                      ('sister', 'Sister'),
                      ('relative', 'Relative'))

    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.CharField(max_length=100, unique=True, db_index=True)
    contact_number = models.CharField(max_length=15, unique=True, db_index=True)
    password = models.CharField(max_length=128, default=None, null=True)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    middle_name = models.CharField(max_length=20, default=None, verbose_name="Middle Name")
    dob = models.DateField(default=None)
    gender = models.CharField(max_length=10, default=None, choices=gender_choice)
    marital_status = models.CharField(max_length=10, default=None, choices=marital_choice)
    profile_creating_for = models.CharField(max_length=10, default=None, choices=profile_choice)

    class Meta:
        app_label = 'member'
        db_table = 'member_member'


    def __unicode__(self):
        return self.username

    def full_member_name(self):
        full_name = ""
        if self.first_name:
            full_name += str(self.first_name) + " "
        if self.last_name:
            full_name += str(self.last_name) + " "
        if self.middle_name:
            full_name += str(self.middle_name) + " "
        return full_name

    full_member_name.short_description = 'Full Name'

    def save(self, force_insert=False, force_update=False, using=None):
        self.password = make_password(self.password)
        soul_email("Member Registered!",self.email)
        super(Member, self).save(force_insert, force_update, using)







