# Generated by Django 4.2.11 on 2024-08-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0005_accesstoken_users_freeserver_users_sshconfig_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesstoken',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='freeserver',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sshconfig',
            old_name='users',
            new_name='user',
        ),
    ]
