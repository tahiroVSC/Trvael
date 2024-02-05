from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    description = models.CharField(
        max_length=400,
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"