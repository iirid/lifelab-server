# Generated by Django 3.0.7 on 2020-08-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200701_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='queue_order',
            field=models.TextField(default=''),
        ),
    ]
