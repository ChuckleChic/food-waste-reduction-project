# Generated by Django 4.2.6 on 2024-03-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='mobile',
            field=models.CharField(max_length=122),
        ),
    ]
