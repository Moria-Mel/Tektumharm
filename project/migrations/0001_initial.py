# Generated by Django 3.2.5 on 2023-07-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Имя не задано', max_length=200)),
                ('short_description', models.TextField(default='Описание не задано')),
                ('photo_id', models.IntegerField(default=0)),
                ('url_id', models.IntegerField(default=0)),
            ],
        ),
    ]
