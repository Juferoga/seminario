# Generated by Django 4.2.2 on 2023-09-25 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_fk_payment'),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='fk_reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation', verbose_name='Llave foránea reservación'),
        ),
    ]
