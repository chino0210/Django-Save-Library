# Generated by Django 5.0.4 on 2024-05-23 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrys_save', '0003_remove_tagsmodel_entrys_ids_tagsdetailmodel_entry_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagsmodel',
            name='status',
        ),
    ]