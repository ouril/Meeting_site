import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


def make_upload_path(instance, filename, prefix=False):
    """Create unqiue name for Image
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    index = parts[-1]
    filename = new_name + '.' + index
    return filename


class UserAccount(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    SEX = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]
    user = models.OneToOneField(
        User,
        related_name='user'
    )
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(
        max_length=190,
        verbose_name='first_name'
    )
    last_name = models.CharField(
        max_length=190,
        verbose_name='last_name'
    )
    sex = models.CharField(
        max_length=6,
        choices=SEX,
        default='male'
    )
    age = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to=make_upload_path,
        default='',
        blank=True
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

