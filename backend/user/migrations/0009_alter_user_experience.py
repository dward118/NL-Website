# Generated by Django 4.1.7 on 2023-03-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_experience_alter_user_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.IntegerField(),
        ),
    ]
