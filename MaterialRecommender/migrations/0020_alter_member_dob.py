# Generated by Django 4.0 on 2022-03-12 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0019_alter_member_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]