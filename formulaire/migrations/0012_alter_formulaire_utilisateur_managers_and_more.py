# Generated by Django 4.1.10 on 2023-08-30 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0011_alter_resetlink_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='formulaire_utilisateur',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='formulaire_utilisateur',
            name='username',
        ),
    ]
