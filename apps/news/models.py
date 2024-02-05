from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class News(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_news",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='news_images/',
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"