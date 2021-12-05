# Generated by Django 3.1.4 on 2021-11-12 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codeforces', '0009_auto_20210929_1435'),
        ('problem', '0005_auto_20210129_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeforcesContest',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(blank=True,
                                          default='',
                                          max_length=63)),
                ('duration', models.IntegerField(default=7200)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('owner',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='codeforces_contest_user',
                                   to='codeforces.user')),
            ],
        ),
        migrations.CreateModel(
            name='CodeforcesContestProblem',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('index', models.IntegerField()),
                ('codeforcesContest',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='contest.codeforcescontest')),
                ('problem',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='problem.problem')),
            ],
        ),
        migrations.AddField(
            model_name='codeforcescontest',
            name='problem',
            field=models.ManyToManyField(
                related_name='codeforces_contest_problem',
                through='contest.CodeforcesContestProblem',
                to='problem.Problem'),
        ),
    ]
