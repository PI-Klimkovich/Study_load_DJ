import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Notice(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(max_length=255, verbose_name="Ваше сообщение", help_text="Не более 255 символов")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    mod_time = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name="Дата изменения")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Создатель")

    objects = models.Manager()  # Он подключается к базе.

    class Meta:
        db_table = 'notice'  # Название таблицы в базе.
        # ordering = ['-created_at']  # Дефис это означает DESC сортировку (обратную).
        ordering = ['-mod_time']  # Сортировка по умолчанию.

    def __str__(self):
        return f"Объявление: \"{self.message}\""
