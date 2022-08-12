from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그명')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE) # ForeignKey 는 일대다 관계
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'