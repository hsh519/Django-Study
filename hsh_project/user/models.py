from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='유저이름')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='패스워드')
    register_dttm = models.DateTimeField(verbose_name='등록시간', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'hsh_userinfo'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

