# Generated by Django 4.0.4 on 2022-04-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('issue', 'Issue'), ('bug', 'Bug'), ('task', 'Task')], max_length=100),
        ),
    ]
