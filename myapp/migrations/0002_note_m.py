# Generated by Django 4.2 on 2024-11-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='note_m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crated', models.DateTimeField(auto_now_add=True)),
                ('no_title', models.CharField(max_length=100)),
                ('no_con', models.CharField(max_length=300)),
                ('myfile', models.FileField(upload_to='MyNotes')),
            ],
        ),
    ]
