# Generated by Django 3.2.9 on 2022-03-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20220315_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='activo',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='activo',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='nota',
            name='activo',
            field=models.CharField(default=1, max_length=1),
        ),
    ]
