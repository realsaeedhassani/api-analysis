# Generated by Django 4.1.2 on 2022-10-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_device_browser_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinfo',
            name='device_type',
            field=models.SmallIntegerField(choices=[(1, 'موبایل'), (2, 'تبلت'), (3, 'کامپیوتر'), (4, 'لمسی'), (5, 'بات'), (6, 'نامشخص')], null=True),
        ),
    ]
