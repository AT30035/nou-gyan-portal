# Generated by Django 4.2.4 on 2023-09-14 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_answer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='posteddate',
            new_name='postedate',
        ),
    ]
