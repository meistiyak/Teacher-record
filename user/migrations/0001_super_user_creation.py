from django.db import migrations
from django.contrib.auth.models import User


def default_user_creation(apps, schema_editor):
    """ Default site configurations """

    User.objects.create_superuser('admin', 'admin@domain.com', 'admin123')


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunPython(default_user_creation),
    ]
