# Generated by Django 5.1.dev20240304192623 on 2024-04-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disco', '0002_alter_bandas_options_rename_nome_bandas_banda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albuns',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='musicas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]