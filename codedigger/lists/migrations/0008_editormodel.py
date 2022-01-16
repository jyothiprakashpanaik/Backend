# Generated by Django 3.2.8 on 2022-01-14 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0007_auto_20211227_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorModel',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('editor_list',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='editor_list',
                                   to='lists.list')),
                ('editor_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='editor_user',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
