# Generated by Django 2.0.3 on 2019-05-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20190521_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='book_name',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_to',
            field=models.CharField(max_length=30),
        ),
    ]
