# Generated by Django 3.0.8 on 2020-07-29 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationtemplate',
            old_name='registrations',
            new_name='accepted_registrations',
        ),
        migrations.AddField(
            model_name='applicationtemplate',
            name='max_registrations',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='categorytag',
            name='label',
            field=models.CharField(max_length=18),
        ),
    ]
