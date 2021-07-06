# Generated by Django 3.2.4 on 2021-07-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0003_remove_loan_interest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='states',
            new_name='state',
        ),
        migrations.AddField(
            model_name='loan',
            name='interest',
            field=models.FloatField(default=7.5),
        ),
        migrations.AlterField(
            model_name='loan',
            name='tenure',
            field=models.IntegerField(default=12),
        ),
    ]
