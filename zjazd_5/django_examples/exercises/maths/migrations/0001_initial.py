# Generated by Django 2.1.3 on 2018-12-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oper', models.CharField(max_length=1)),
                ('l1', models.IntegerField()),
                ('l2', models.IntegerField()),
            ],
        ),
    ]
