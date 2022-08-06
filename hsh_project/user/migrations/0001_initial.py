# Generated by Django 4.0.6 on 2022-08-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='유저이름')),
                ('useremail', models.EmailField(max_length=128, verbose_name='사용자이메일')),
                ('password', models.CharField(max_length=64, verbose_name='패스워드')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'hsh_userinfo',
            },
        ),
    ]
