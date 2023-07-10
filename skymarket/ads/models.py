from django.conf import settings
from django.db import models



class Ad(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to="images/",
        verbose_name="изображение",
        help_text="Загрузите изображение для объявления",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return self.text