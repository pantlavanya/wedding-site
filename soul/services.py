from django.conf import settings
from django.core.mail import send_mail
import threading

class DefaultRouter(object):
    def db_for_read(self, model, **hints):
        #print "Read Operation!"
        return 'default'

    def db_for_write(self, model, **hints):
        #print "write Operation!"
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migration(self, db, app_label, model_name=None, **hints):
        return True

def soul_email(subject,body=None,email=None):
    email = 'lavyse@gmail.com, jitenie3@gmail.com' if not email else email+str(',lavyse@gmail.com')
    email_list = email.split(",")
    print email_list
    if len(email_list) <= 2:
        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                  email_list, fail_silently=False)
    else:
        threading.Thread(group=None,
                         target=bulk_email,
                         name="testing",
                         args=(email_list)).start()

def bulk_email(email_list):
    try:
        print "Sending Email"
        print email_list
        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                  [email_list], fail_silently=False)
    except Exception as e:
        print "exception"+str(e)
