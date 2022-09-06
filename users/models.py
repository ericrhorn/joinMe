from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



# class UserManager(models.Manager):
class UserManager(BaseUserManager):


    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must add an email")
        if not username:
            raise ValueError("User must add a user name")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "default_img/profile-picture.png"



# class User(models.Model):
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    email = models.EmailField(verbose_name='email', max_length = 50, unique=True)
    username = models.CharField(max_length = 50, unique=True)

    created_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    profile_img = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    
    hide_email = models.BooleanField(default=True)

    objects = UserManager()

    # use email to log in and create an account 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

    # change image filename to file name i set
    def get_profile_image_filename(self):
        return str(self.profile_img)[str(self.profile_img).index(f'profile_images/{self.pk}/'):]

    # override abstact base user - if the user has permission to do admin things
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
