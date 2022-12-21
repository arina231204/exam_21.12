# Generated by Django 4.1.4 on 2022-12-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('date_started', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('month_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('work_study_place', models.CharField(blank=True, max_length=20, null=True)),
                ('has_own_notebook', models.BooleanField(default=False)),
                ('preferred_os', models.CharField(choices=[('mac', 'MacOS'), ('windows', 'Windows'), ('linux', 'Linux')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('main_work', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.DateField()),
                ('student', models.ManyToManyField(related_name='students', through='users.Courses', to='users.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mentor'),
        ),
        migrations.AddField(
            model_name='courses',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
    ]
