from django.db import models

class News(models.Model):
   title=models.CharField(max_length=50,verbose_name='наименование')
   content=models.TextField(blank=True,verbose_name='описание')
   created_at=models.DateTimeField(auto_now_add=True,verbose_name='дата публкации')
   photo=models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='фото',blank=True)
   is_published=models.BooleanField(default=True,verbose_name='опубликовано')

   class Meta:
      verbose_name='новость'
      verbose_name_plural = 'новости'
      ordering=['-created_at']


# Create your models here.
