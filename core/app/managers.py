from django.db import models

class AccountQuerySet(models.QuerySet):
    def rich(self):
        return self.filter(balance__gte=100000)

    def poor(self):
        return self.filter(balance__lt=1000)

class AccountManager(models.Manager):
    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    def rich(self):
        return self.get_queryset().rich()

    def poor(self):
        return self.get_queryset().poor()
