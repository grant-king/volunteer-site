# Generated by Django 3.0.8 on 2020-07-17 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('application_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer_register.ApplicationTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer_register.Question')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('application_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer_register.ApplicationTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('application_submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer_register.ApplicationSubmission')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer_register.Question')),
            ],
        ),
    ]