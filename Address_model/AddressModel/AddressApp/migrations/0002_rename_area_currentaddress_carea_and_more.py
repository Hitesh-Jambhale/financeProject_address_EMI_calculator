# Generated by Django 4.0.1 on 2022-01-12 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AddressApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentaddress',
            old_name='area',
            new_name='Carea',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='city',
            new_name='Ccity',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='country',
            new_name='Ccountry',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='district',
            new_name='Cdistrict',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='flat_no',
            new_name='Cflat_no',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='landmark',
            new_name='Clandmark',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='pincode',
            new_name='Cpincode',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='state',
            new_name='Cstate',
        ),
        migrations.RenameField(
            model_name='currentaddress',
            old_name='street_name',
            new_name='Cstreet_name',
        ),
    ]
