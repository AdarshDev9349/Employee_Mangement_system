# Generated by Django 4.2.6 on 2023-10-28 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_ID', models.CharField(max_length=12)),
                ('Department_name', models.CharField(max_length=13)),
                ('Department_location', models.CharField(max_length=13)),
                ('Manager_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.employee')),
            ],
        ),
    ]
