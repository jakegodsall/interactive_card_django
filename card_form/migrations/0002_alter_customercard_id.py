# Generated by Django 4.1.3 on 2022-11-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercard',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
