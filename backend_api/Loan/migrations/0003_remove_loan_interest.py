# Generated by Django 3.2.4 on 2021-07-04 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0002_alter_loan_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='interest',
        ),
    ]
