# Generated by Django 3.1.7 on 2021-04-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210422_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
    ]
