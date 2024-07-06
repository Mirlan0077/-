from django.db import models
from django.utils import timezone

class GuestBookEntry(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    author_name = models.CharField(max_length=255, verbose_name="Имя автора записи", blank=False)
    author_email = models.EmailField(verbose_name="Почта автора записи", blank=False)
    entry_text = models.TextField(verbose_name="Текст записи", blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Статус", blank=False)

    def __str__(self):
        return f"{self.author_name} - {self.get_status_display()}"
