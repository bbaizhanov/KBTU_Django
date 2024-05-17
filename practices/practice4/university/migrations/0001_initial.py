# Generated by Django 3.2.12 on 2024-02-25 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relevant', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.faculty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('build_year', models.IntegerField()),
                ('popular', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.speciality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.university'),
        ),
    ]