import csv
import os
from io import StringIO

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from core.utils import file_exist
from teacher_directory.settings import MEDIA_ROOT
from .models import Teacher, TeacherBulkUpload


@receiver(post_save, sender=TeacherBulkUpload)
def create_bulk_teacher(sender, created, instance, *args, **kwargs):
    if created:
        opened = StringIO(instance.csv_file.read().decode())
        reading = csv.DictReader(opened, delimiter=',')
        creatable_records = []
        for row in reading:
            if 'Email Address' in row and row['Email Address']:
                first_name = row.get('First Name')
                last_name = row.get('Last Name')
                email = row.get('Email Address')
                phone = row.get('Phone Number')
                room_no = row.get('Room Number')
                subject_taught = row.get('Subjects taught')
                avatar = row.get('Profile picture')

                if avatar:
                    avatar_path = f'teachers/avatar/{avatar}'
                    full_avatar_path = os.path.join(MEDIA_ROOT,avatar_path)
                    avatar_path = avatar_path if file_exist(full_avatar_path) else None
                else:
                    avatar_path = None

                if not Teacher.objects.filter(
                        email=email
                ).exists():
                    creatable_records.append(
                        Teacher(
                            email=email,
                            phone=phone,
                            room_no=room_no,
                            avatar=avatar_path,
                            last_name=last_name,
                            first_name=first_name,
                            subject_taught=subject_taught
                        )
                    )

        if creatable_records:
            Teacher.objects.bulk_create(creatable_records)

        instance.csv_file.close()
        instance.delete()


def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=TeacherBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
    if instance.csv_file:
        _delete_file(instance.csv_file.path)
