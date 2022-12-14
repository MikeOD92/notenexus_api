# Generated by Django 4.1.2 on 2022-10-13 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=10000)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='notesapp.node')),
            ],
        ),
    ]
