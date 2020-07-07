# Generated by Django 3.0.6 on 2020-06-07 13:27

from django.db import migrations
import django.db.models.deletion
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('oro_plugins', '0003_auto_20200607_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypluginmodel',
            name='folder',
            field=filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.PROTECT, to='filer.Folder'),
        ),
    ]
