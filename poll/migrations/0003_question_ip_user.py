# Generated by Django 4.1.7 on 2023-05-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_alter_question_birth_date_alter_question_since_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ip_user',
            field=models.CharField(default='0.0.0.0', max_length=200),
        ),
    ]
