# Generated by Django 3.0.5 on 2020-04-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_program_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='career_prospectus',
            field=models.TextField(null=True),
        ),
    ]