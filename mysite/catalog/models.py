from django.db import models

# Create your models here.

class Questionnaire(models.Model):
    genderOptions=(
        ('不透露', '不透露'),
        ('男', '男'),
        ('女', '女')
        )
    userName = models.CharField(max_length=10,help_text='請輸入姓名')
    gender = models.CharField(max_length=3, choices=genderOptions, default='n', help_text='請輸入性別')
    favoriteCity = models.CharField(max_length=50, help_text='請輸入最喜歡的城市 (最多50字')
    reason = models.TextField(max_length=300, help_text='請輸入喜歡該城市的理由 (最多300字)')
    submitTime = models.DateTimeField(auto_now=True)
    class Meta:
        def __str__(self):
            return self.name
