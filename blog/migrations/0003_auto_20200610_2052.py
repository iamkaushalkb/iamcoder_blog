# Generated by Django 3.0.6 on 2020-06-10 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200610_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
