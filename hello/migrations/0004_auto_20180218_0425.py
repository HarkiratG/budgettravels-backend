# Generated by Django 2.0.2 on 2018-02-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20180218_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='photoURL',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='destinations',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]