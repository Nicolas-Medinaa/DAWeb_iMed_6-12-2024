# Generated by Django 5.1.2 on 2024-12-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='id_proveedor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
