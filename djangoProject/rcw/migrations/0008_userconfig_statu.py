# Generated by Django 2.2.10 on 2021-01-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcw', '0007_auto_20210105_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='statu',
            field=models.CharField(max_length=30, null=True),
        ),
    ]