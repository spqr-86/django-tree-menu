# Generated by Django 4.1.7 on 2023-02-22 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_rename_name_menuitem_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='title',
            new_name='name',
        ),
    ]