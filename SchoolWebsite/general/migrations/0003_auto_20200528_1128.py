# Generated by Django 3.0.6 on 2020-05-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20200527_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='contactinfo',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
