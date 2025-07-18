# Generated by Django 5.2.4 on 2025-07-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='Укажите тему сообщения', max_length=100, verbose_name='Тема сообщения')),
                ('links', models.TextField(help_text='Добавьте текст сообщения', verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания продукта', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата последнего изменения продукта', verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщенния',
            },
        ),
    ]
