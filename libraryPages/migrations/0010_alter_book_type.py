# Generated by Django 3.2.4 on 2021-07-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryPages', '0009_borrowed_extended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Sceince', 'Science'), ('Drama', 'Drama'), ('Crime', 'Crime')], max_length=50),
        ),
    ]
