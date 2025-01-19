from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    first_name = models.CharField(blank=False, max_length=150,
                                  verbose_name=_('First Name'))
    last_name = models.CharField(blank=False, max_length=150,
                                 verbose_name=_('Last Name'))
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
