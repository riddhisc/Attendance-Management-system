# Generated by Django 3.2.3 on 2021-07-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPanel', '0003_auto_20210730_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='std_password',
            field=models.CharField(default=2021, max_length=20),
            preserve_default=False,
        ),
    ]
