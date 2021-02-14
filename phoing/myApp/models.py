from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .utils import uuid_name_upload_to, save_image_from_url
from django.utils.translation import ugettext_lazy as _

from django.dispatch import receiver
from allauth.account.signals import user_signed_up
import urllib

from django.shortcuts import redirect
from user.models import User



class Contact(models.Model): 
    #common field
    user = models.ForeignKey(
        to=User, related_name="contacts", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=uuid_name_upload_to)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    save_users = models.ManyToManyField(
        to=User, related_name='contact_save_users', blank=True)
    desc = models.TextField()

    #specific field
    file_attach = models.FileField()
    location = models.TextField()
    pay = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_closed = models.BooleanField(default=False)


class Portfolio(models.Model):
    #common field
    user = models.ForeignKey(
        to=User, related_name="portfolios", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=uuid_name_upload_to)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    save_users = models.ManyToManyField(
        to=User, related_name='portfolio_save_users', blank=True)
    desc = models.TextField()

    #specific field
    like_users = models.ManyToManyField(
        to=User, related_name='portfolio_like_users', blank=True)
    view_count = models.PositiveIntegerField(default=0)


     


class Comment(models.Model):
    contact = models.ForeignKey(
        to=Contact, null=True, blank=True, related_name='contact_comments', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        to=Portfolio, null=True, blank=True, related_name='portfolio_comments', on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    contact = models.ForeignKey(
        to=Contact, null=True, blank=True, related_name='contact_tags', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        to=Portfolio, null=True, blank=True, related_name='portfolio_tags', on_delete=models.CASCADE)

    tag = models.CharField(max_length=30)


class Image(models.Model):
    contact = models.ForeignKey(
        to=Contact, null=True, blank=True, related_name='contact_images', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        to=Portfolio, null=True, blank=True, related_name='portfolio_images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to=uuid_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Reference():

    # NOTE: 변수 이름  self.desc/self.tags로 가정하고 add_tags 함수 만듬!
    
    def add_tags(self):
        # NOTE: self.desc 말고 TAG FIELD 따로 만들까?
        tags = re.findall(r'#(\w+)\b', self.desc)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  



# class Post(models.Model):
#     user = models.ForeignKey(
#         to=User, related_name="posts", on_delete=models.CASCADE)
#     thumbnail = models.ImageField(upload_to=uuid_name_upload_to)
#     title = models.CharField(max_length=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     save_users = models.ManyToManyField(
#         to=User, related_name='save_users', blank=True)
#     desc = models.TextField()

#     def __str__(self):
#         return self.title


# class Place(models.Model):
#     #common field
#     user = models.ForeignKey(
#         to=User, related_name="posts", on_delete=models.CASCADE)
#     thumbnail = models.ImageField(upload_to=uuid_name_upload_to)
#     title = models.CharField(max_length=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     save_users = models.ManyToManyField(
#         to=User, related_name='save_users', blank=True)
#     desc = models.TextField()

#     #specific field
#     like_users = models.ManyToManyField(
#         to=User, related_name='like_users', blank=True)
#     location = models.TextField()
#     pay = models.PositiveIntegerField()



# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""

#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         if not user.username:
#             user.username = email.split('@')[0]
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     CATEGORY_PHOTOGRAPHER = 'photographer'
#     CATEGORY_MODEL = 'model'
#     CATEGORY_HM = 'HairMakeup'
#     CATEGORY_STYLIST = 'stylist'
#     CATEGORY_OTHER = 'other use'

#     CATEGORY = (
#         ('photographer', CATEGORY_PHOTOGRAPHER),
#         ('model', CATEGORY_MODEL),
#         ('HairMakeup', CATEGORY_HM),
#         ('stylist', CATEGORY_STYLIST),
#         ('other use', CATEGORY_OTHER),
#     )

#     username = models.CharField(max_length=20, blank=True)
#     email = models.EmailField(_('email address'), unique=True)
#     category = models.CharField(
#         max_length=20, choices=CATEGORY)
#     image = models.ImageField(
#         upload_to=uuid_name_upload_to, blank=True, default='user.png')
#     desc = models.TextField(blank=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""

#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         if not user.username:
#             user.username = email.split('@')[0]
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     CATEGORY_PHOTOGRAPHER = 'photographer'
#     CATEGORY_MODEL = 'model'
#     CATEGORY_HM = 'HairMakeup'
#     CATEGORY_STYLIST = 'stylist'
#     CATEGORY_OTHERS = 'otheruse'

#     CATEGORY = (
#         ('photographer', CATEGORY_PHOTOGRAPHER),
#         ('model', CATEGORY_MODEL),
#         ('HairMakeup', CATEGORY_HM),
#         ('stylist', CATEGORY_STYLIST),
#         ('otheruse', CATEGORY_OTHERS),
#     )

#     username = models.CharField(max_length=20, blank=True)
#     email = models.EmailField(_('email address'), unique=True)
#     category = models.CharField(
#         max_length=20, choices=CATEGORY)
#     image = models.ImageField(
#         upload_to=uuid_name_upload_to, blank=True, )
#     desc = models.TextField(blank=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []



# @receiver(user_signed_up)
# def populate_profile(user, sociallogin=None, **kwargs):

#     if sociallogin.account.provider == 'naver':
#         user_data = user.socialaccount_set.filter(provider='naver')[
#             0].extra_data
#         picture_url = user_data["profile_image"]
#         username = user_data["nickname"]
#         # first_name = user_data['first_name']

#     if sociallogin.account.provider == 'kakao':
#         user_data = user.socialaccount_set.filter(provider='kakao')[
#             0].extra_data
#         picture_url = user_data["properties"]["profile_image"]
#         username = user_data["properties"]["nickname"]

#     if sociallogin.account.provider == 'google':
#         user_data = user.socialaccount_set.filter(
#             provider='google')[0].extra_data
#         picture_url = user_data["picture"]
#         username = user_data["name"]

#     user.username = username
#     save_image_from_url(user, picture_url)
#     user.save()
