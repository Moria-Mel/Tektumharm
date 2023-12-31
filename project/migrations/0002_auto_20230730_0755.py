# Generated by Django 3.2.5 on 2023-07-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='photo_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='short_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='portfoliomodel',
            name='url_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
