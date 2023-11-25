# Generated by Django 4.2.7 on 2023-11-25 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя стола')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Размер стола (количество мест)')),
                ('table_type', models.CharField(choices=[('simple_table', 'Обычный стол'), ('bar_table', 'Барный стол')], max_length=256, verbose_name='Тип стола')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='cafe.cafe', verbose_name='В кафе')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
                'ordering': ('cafe', 'quantity'),
            },
        ),
        migrations.CreateModel(
            name='ReservationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата бронирования')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.table', verbose_name='Стол')),
            ],
            options={
                'verbose_name': 'Бронь стола',
                'verbose_name_plural': 'Брони стола',
            },
        ),
    ]
