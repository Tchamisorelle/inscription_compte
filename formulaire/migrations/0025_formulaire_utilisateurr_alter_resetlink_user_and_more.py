# Generated by Django 4.1.10 on 2023-08-30 03:05

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('formulaire', '0024_remove_formulaire_utilisateur_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='formulaire_utilisateurr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('sexe', models.CharField(choices=[('homme', 'Homme'), ('femme', 'Femme')], max_length=6)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('qualification_chercheur', models.BooleanField(default=False)),
                ('qualification_mentor', models.BooleanField(default=False)),
                ('pays', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(blank=True, related_name='utilisateur', to='auth.group', verbose_name='Groupes')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='utilisateur', to='auth.permission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='resetlink',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulaire.formulaire_utilisateurr'),
        ),
        migrations.DeleteModel(
            name='formulaire_utilisateur',
        ),
    ]
