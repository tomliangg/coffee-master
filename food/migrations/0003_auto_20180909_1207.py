# Generated by Django 2.0.5 on 2018-09-09 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20180909_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodinstance',
            options={'permissions': (('can_order', 'Can order the drinks'), ('can_serve', 'Can prepare and serve the drinks'))},
        ),
    ]