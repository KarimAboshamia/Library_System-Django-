# Generated by Django 3.2.5 on 2021-07-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryPages', '0008_auto_20210715_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='extended',
            field=models.BooleanField(default=False),
        ),
    ]
