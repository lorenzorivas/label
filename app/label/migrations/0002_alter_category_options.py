# Generated by Django 3.2.5 on 2021-07-10 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Categoria'},
        ),
    ]