from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='image_created',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        blank=True,
    )
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='images_liked',
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    # переопределения метода save() для автоматичекого заполнения поля slug
    def save(self, *args, **kwargs):
        if not self.slug:
6
super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title
