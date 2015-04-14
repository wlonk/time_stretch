from django.db import models


class PublicManager(models.Manager):

    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(
            publicity=0  # Terrible hardcoding, but circumvents circular import
        )


class LoginManager(models.Manager):

    def get_queryset(self):
        return super(LoginManager, self).get_queryset().filter(
            publicity__lte=1  # Terrible hardcoding, but circumvents circular import
        )


class PrivateManager(models.Manager):

    def get_queryset(self):
        return super(PrivateManager, self).get_queryset().filter(
            publicity__lte=2  # Terrible hardcoding, but circumvents circular import
        )
