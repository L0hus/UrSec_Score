# Generated by Django 4.2.13 on 2024-05-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activName', models.TextField(max_length=100, verbose_name='Имя')),
                ('activDate', models.DurationField(verbose_name='Дата')),
                ('activLink', models.TextField(verbose_name='Ссылка')),
                ('activPlace', models.IntegerField(verbose_name='Место')),
                ('activCertif', models.FileField(upload_to='media/user_cert', verbose_name='Сертификат')),
                ('activOther', models.TextField(verbose_name='Иное подтверждение')),
                ('activAddit', models.TextField(verbose_name='Допоплнительная информация')),
            ],
        ),
    ]
