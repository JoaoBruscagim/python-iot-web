# Generated by Django 3.2.19 on 2024-09-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0002_auto_20240926_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivos',
            name='chave',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
