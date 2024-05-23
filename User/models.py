from django.db import models

class Report(models.Model):
    activName = models.TextField(
        verbose_name="Имя", 
        max_length=100,
        blank = False,
    )
    activDate = models.DateField(
        verbose_name="Дата",
        blank = False,
    )
    activLink = models.TextField(
        verbose_name="Ссылка",
        blank = True,
        default = "",
    )
    activPlace = models.IntegerField(
        verbose_name="Место",
        blank = True,
        default = 0,
    )
    activCertif = models.FileField(
        verbose_name="Сертификат", 
        upload_to="media/user_cert",
        blank = True,
        default = "",
    )
    activOther = models.TextField(
        verbose_name="Иное подтверждение",
        blank = True,
        default = "",
    )
    activAddit = models.TextField(
        verbose_name="Допоплнительная информация",
        blank = True,
        default = "",
    )