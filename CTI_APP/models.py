from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class CtiLog(models.Model):
    id = models.AutoField(primary_key=True)  # ID поля автоматически создается для каждой записи
    cve = models.CharField("CVE", max_length=50, null=True, blank=True)
    signature = models.CharField("Сигнатура", max_length=100, blank=True, null=True)
    description = models.TextField("Описание атаки")
    response_measures = models.TextField("Меры реагирования")

    class Meta:
        verbose_name = "CTI запись"
        verbose_name_plural = "CTI записи"

    def __str__(self):
        return f"{self.cve} - {self.id}"


class BlackListIP(models.Model):
    ip_source = models.GenericIPAddressField("IP Источника", null=False, blank=False)
    attack_date = models.IntegerField(
        "Год появления атаки",  # Обновили название для отображения только года
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        help_text="Введите год, когда была обнаружена атака"
    )  # Убрали лишнюю запятую
    country_source = models.CharField("Страна источник", max_length=50)

    class Meta:
        verbose_name = "Black List IP"
        verbose_name_plural = "Black List IP"

    def __str__(self):
        return f"{self.ip_source} - {self.attack_date}"

class BlackListURL(models.Model):
    url_source = models.TextField("URL Источника", null=False, blank=False)
    attack_date = models.IntegerField(
        "Год появления URL",  # Обновили название для отображения только года
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        help_text="Введите год, когда была обнаружена вредносная ПО"
    )  # Убрали лишнюю запятую

    class Meta:
        verbose_name = "Black List URL"
        verbose_name_plural = "Black List URL"

    def __str__(self):
        return f"{self.url_source} - {self.attack_date}"