# Generated by Django 3.2.19 on 2024-08-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0002_alter_acoes_dispositivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='acao',
            field=models.CharField(max_length=45),
        ),
    ]
