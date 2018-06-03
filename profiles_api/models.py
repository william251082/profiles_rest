from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a "user profile" inside our system. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # TODO make the UserProfileManager() class
    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get the full name. """

        return self.name

    def get_short_name(self):
        """ Used to get the users short name."""

        return self.name

    def __str__(self):
        """ Django uses this when it need to convert the object to string. """

