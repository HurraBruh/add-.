# Generated by Django 4.1.7 on 2023-05-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_alter_question_ip_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ip_user',
            field=models.TextField(default='0.0.0.0', max_length=200),
        ),
    ]