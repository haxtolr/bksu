from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_approved', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)



class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    rank = models.CharField(max_length=50, default='사원')
    login_time = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    day_time = models.DateTimeField(null=True, blank=True)
    week_time = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def login(self):
        self.login_time = timezone.now()
        self.save()

    def logout(self):
        if self.login_time:
            duration = timezone.now() - self.login_time
            self.day_time = duration if self.day_time is None else self.day_time + duration
            self.week_time = duration if self.week_time is None else self.week_time + duration
            self.logout_time = timezone.now()
            self.save()

    def approve(self):
        self.is_approved = True
        self.save()

    def get_online_duration(self):
        if self.login_time:
            return timezone.now() - self.login_time
        else:
            return None
        
@receiver(pre_save, sender=User)
def reset_week_time(sender, instance, **kwargs):
    if timezone.now().weekday() == 0 and timezone.now().hour == 0:
        instance.week_time = timezone.now()

def reset_day_time(sender, instance, **kwargs):
    if timezone.now().hour == 0:
        instance.day_time = timezone.now()