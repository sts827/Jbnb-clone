# Generated by Django 2.2.5 on 2020-08-30 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20200830_0323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodCategory',
            new_name='FoodType',
        ),
        migrations.AlterModelOptions(
            name='foodtype',
            options={'verbose_name': 'Food Type'},
        ),
    ]