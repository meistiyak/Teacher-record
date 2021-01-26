from django.db import models
from django.urls import reverse

from core.models import BaseModel


class Teacher(BaseModel):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=128,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=128,
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        verbose_name='Profile picture',
        blank=True,
        upload_to='teachers/avatar/'
    )
    email = models.EmailField(
        verbose_name='Email',
        null=True,
        blank=True,
        unique=True
    )
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=16,
        null=True,
        blank=True
    )
    room_no = models.CharField(
        verbose_name='Room number',
        max_length=10,
        null=True,
        blank=True
    )
    subject_taught = models.CharField(
        verbose_name='Subject Taught',
        max_length=512,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'pk': self.pk})


class TeacherBulkUpload(BaseModel):
    csv_file = models.FileField(upload_to='teachers/bulkupload/')
