from django.db import models


class PublicManager(models.Manager):

    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(
            publicity=0  # Terrible hardcoding, but circumvents circular import
        )
