# Generated by Django 3.2 on 2022-08-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='post/'),
        ),
    ]
