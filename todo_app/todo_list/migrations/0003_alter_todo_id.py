# Generated by Django 5.1.5 on 2025-01-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_remove_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
