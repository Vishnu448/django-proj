# Generated by Django 5.1.7 on 2025-04-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_user_mobile_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_name',
            new_name='username',
        ),
    ]
