# Generated by Django 3.0.7 on 2020-08-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_issue_queue_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='queue_order',
        ),
        migrations.AddField(
            model_name='lab',
            name='queue_order',
            field=models.TextField(default=''),
        ),
    ]
