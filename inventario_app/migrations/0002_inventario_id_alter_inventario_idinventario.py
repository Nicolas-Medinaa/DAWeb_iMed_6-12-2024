# Generated by Django 5.1.2 on 2024-12-06 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventario',
            name='idinventario',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]