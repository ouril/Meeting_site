from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


def make_upload_path(instance, filename, prefix=False):
    """Create unqiue name for Image
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    index = parts[-1]
    filename = new_name + '.' + index
    return "{0}/{1}".format(settings.MEDIA_ROOT, filename)


class UserAccount(models.Model):
    SEX = 'male', 'female'
    user = models.OneToOneField(
        User,
        related_name='user'
    )
    created = models.DataTimeField(auto_now_add=True)
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
        defauslt='male'
    )
    birth_date = models.DataTimeField()
    image = models.ImageField(
        upload_to=make_upload_path,
        default='',
        blank=True
    )

    def _str_(self):
        return self.first_name + ' ' + self.last_name

    @property
    def age(self):
        now = datetime.today()
        return now.year - self.birth_date.year
