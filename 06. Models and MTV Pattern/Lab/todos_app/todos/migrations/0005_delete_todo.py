# Generated by Django 3.2.4 on 2021-06-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_todo_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
