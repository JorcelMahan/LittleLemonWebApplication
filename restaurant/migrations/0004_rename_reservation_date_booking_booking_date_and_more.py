# Generated by Django 4.2.6 on 2023-10-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_date',
            new_name='booking_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_slot',
            new_name='number_of_guests',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
