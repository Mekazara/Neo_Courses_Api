# Generated by Django 4.0.2 on 2022-02-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_tpe_contact_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
