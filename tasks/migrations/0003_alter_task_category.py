# Generated by Django 4.0.4 on 2022-04-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('625b2a1865db111253c2706d', 'Maintenance'), ('625b2a260e06ad7c2e514278', 'Research'), ('625b2a2eca30bb145948d4c7', 'Test'), ('625b961941921a01845f7f8e', 'Bug')], max_length=100),
        ),
    ]
