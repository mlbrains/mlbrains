# Generated by Django 3.1.3 on 2021-01-10 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210109_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='Allocated_to_User',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.mluser'),
        ),
    ]
