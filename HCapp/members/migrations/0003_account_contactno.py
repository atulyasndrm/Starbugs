# Generated by Django 4.1.7 on 2023-04-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_account_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ContactNo',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]