# Generated by Django 4.2 on 2024-11-28 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_nodetbl_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='no_con',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='myfile',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='no_title',
            new_name='title',
        ),
    ]