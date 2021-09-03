# Generated by Django 3.2.3 on 2021-07-30 04:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserPanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='std_reg',
            field=models.CharField(default=django.utils.timezone.now, max_length=5, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('att_id', models.AutoField(primary_key=True, serialize=False)),
                ('att_date', models.DateField()),
                ('att_status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present'), ('L', 'Leave')], max_length=1)),
                ('std_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserPanel.student')),
            ],
        ),
    ]
