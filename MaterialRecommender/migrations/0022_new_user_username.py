# Generated by Django 4.0 on 2022-03-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0021_new_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='username',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
