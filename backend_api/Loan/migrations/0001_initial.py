# Generated by Django 3.2.4 on 2021-07-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenure', models.IntegerField()),
                ('interest', models.IntegerField()),
                ('states', models.CharField(choices=[('NEW', 'New Loan'), ('REJECTED', 'Rejected Loan'), ('APPROVED', 'Approved Loan')], max_length=8)),
            ],
        ),
    ]
