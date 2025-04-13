# Generated by Django 5.1.7 on 2025-04-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
