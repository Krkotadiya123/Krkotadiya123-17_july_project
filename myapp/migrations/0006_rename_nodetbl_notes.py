# Generated by Django 4.2 on 2024-11-28 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_note_tbl_nodetbl_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='nodetbl',
            new_name='notes',
        ),
    ]