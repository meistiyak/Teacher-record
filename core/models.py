from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False,
        db_index=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
