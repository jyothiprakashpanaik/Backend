# Generated by Django 3.1.4 on 2021-12-27 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_enrolled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='enroll_list',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='enroll_list',
                to='lists.list'),
        ),
    ]
