# Generated by Django 5.1.2 on 2024-12-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='id_empleado',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
