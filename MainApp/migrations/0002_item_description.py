# Generated by Django 5.0.6 on 2024-05-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='default', max_length=150),
            preserve_default=False,
        ),
    ]
