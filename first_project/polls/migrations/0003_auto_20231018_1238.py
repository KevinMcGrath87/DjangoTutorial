# Generated by Django 2.2.4 on 2023-10-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
