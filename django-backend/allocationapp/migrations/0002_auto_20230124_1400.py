# Generated by Django 3.1.6 on 2023-01-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='assigned_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='allocationapp.team'),
        ),
    ]
