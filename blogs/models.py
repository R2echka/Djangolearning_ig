from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Содержимое')
    preview = models.ImageField('Превью', upload_to='blogs/photo', blank=True, null=True)
    created_at = models.DateField('Дата создания', blank=True, null=True, default=None)
    is_publicated = models.BooleanField('Признак публикации', default=True)
    views = models.IntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'