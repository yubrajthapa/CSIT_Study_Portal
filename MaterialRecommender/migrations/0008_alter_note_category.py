# Generated by Django 4.0.2 on 2022-03-06 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0007_delete_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]
