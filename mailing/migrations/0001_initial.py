# Generated by Django 4.2.5 on 2023-09-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog')),
                ('views', models.PositiveIntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'статья блога',
                'verbose_name_plural': 'статьи блога',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='DeliveryAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='время')),
                ('status', models.CharField(max_length=255, verbose_name='статус')),
                ('response', models.TextField(verbose_name='ответ')),
            ],
            options={
                'verbose_name': 'попытка доставки',
                'verbose_name_plural': 'попытки доставки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='тема')),
                ('body', models.TextField(verbose_name='тело')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(choices=[('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], max_length=5, verbose_name='время начала')),
                ('frequency', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=255, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('completed', 'Завершено'), ('created', 'Создано'), ('started', 'Запущено')], max_length=255, verbose_name='статус')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='клиенты')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]
