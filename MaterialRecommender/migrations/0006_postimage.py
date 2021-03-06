# Generated by Django 4.0.2 on 2022-03-03 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0005_alter_material_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='static/images')),
                ('mat', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MaterialRecommender.material')),
            ],
        ),
    ]
