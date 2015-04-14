from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from .fields import AutoDatetimeField
from .managers import (
    PublicManager,
    LoginManager,
    PrivateManager,
    )


# Create your models here.
class Entry(models.Model):
    PUBLIC = 0
    LOGIN = 1
    PRIVATE = 2
    PUBLICITIES = (
        (PUBLIC, 'Public'),
        (LOGIN, 'Login'),
        (PRIVATE, 'Private'),
        )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')  # RSS
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = AutoDatetimeField(default=timezone.now)
    publicity = models.IntegerField(choices=PUBLICITIES, default=PRIVATE)

    class Meta:
        verbose_name_plural = 'entries'

    objects = models.Manager()
    public = PublicManager()
    login = LoginManager()
    private = PrivateManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        print self
        return reverse('blog:entry', kwargs={'entry_id': str(self.id)})
