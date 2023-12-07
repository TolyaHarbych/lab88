# Generated by Django 4.2.7 on 2023-12-07 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('bonus_percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('funding_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExecution',
            fields=[
                ('execution_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.department')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.project')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.position')),
            ],
        ),
    ]
