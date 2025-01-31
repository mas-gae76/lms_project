# Generated by Django 4.0 on 2023-06-08 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название курса')),
                ('description', models.TextField(max_length=200, verbose_name='Описание курса')),
                ('start_date', models.DateField(verbose_name='Старт курса')),
                ('duration', models.PositiveIntegerField(verbose_name='Продолжительность')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='Цена')),
                ('count_lessons', models.PositiveIntegerField(verbose_name='Кол-во уроков')),
                ('authors', models.ManyToManyField(db_table='course_authors', related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Автор курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['title'],
                'permissions': (('modify_course', 'Can modify course content'),),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название урока')),
                ('preview', models.TextField(max_length=200, verbose_name='Описание урока')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='learning.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['course'],
                'permissions': (('modify_lesson', 'Can modify lesson content'),),
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.BooleanField(default=None, verbose_name='Пройден?')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='learning.lesson', verbose_name='Урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user', verbose_name='Ученик')),
            ],
            options={
                'ordering': ['-user'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250, unique_for_year='sent_date', verbose_name='Текст отзыва')),
                ('sent_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки отзыва')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.course', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user', verbose_name='Ученик')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-sent_date',),
                'unique_together': {('user', 'course')},
            },
        ),
    ]
