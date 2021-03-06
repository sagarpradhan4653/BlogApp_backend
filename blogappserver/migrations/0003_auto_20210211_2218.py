# Generated by Django 3.1.5 on 2021-02-11 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogappserver', '0002_blogger_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='picture',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
