# Generated by Django 3.1.4 on 2021-12-19 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0005_auto_20210129_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodechefContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contestId', models.CharField(db_index=True, max_length=10)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('startTime', models.DateTimeField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodechefContestProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codechef.codechefcontest')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
            ],
        ),
    ]
