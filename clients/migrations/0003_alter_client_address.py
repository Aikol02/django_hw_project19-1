# Generated by Django 4.1 on 2022-08-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_photo_alter_client_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
