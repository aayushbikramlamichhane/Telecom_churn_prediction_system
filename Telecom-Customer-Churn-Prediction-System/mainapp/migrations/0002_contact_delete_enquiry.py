# Generated by Django 4.1.4 on 2023-02-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('emailadd', models.EmailField(max_length=254)),
                ('num', models.IntegerField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
    ]