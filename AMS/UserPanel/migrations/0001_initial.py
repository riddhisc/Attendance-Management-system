# Generated by Django 3.2.3 on 2021-07-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=150)),
                ('std_email', models.EmailField(max_length=254)),
                ('std_cnic', models.CharField(max_length=150)),
                ('std_image', models.ImageField(upload_to='static/upload/')),
            ],
        ),
    ]