# Generated by Django 3.0.8 on 2020-08-06 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_register', '0003_applicationtemplate_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='menu_name',
            field=models.CharField(default='unnamed', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationtemplate',
            name='accepted_registrations',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='applicationtemplate',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='application_pics'),
        ),
        migrations.AlterField(
            model_name='question',
            name='application_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='volunteer_register.ApplicationTemplate'),
        ),
    ]
