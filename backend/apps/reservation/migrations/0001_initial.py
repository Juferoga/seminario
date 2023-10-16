# Generated by Django 4.2.2 on 2023-10-16 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authuser', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('b_status', models.BooleanField(auto_created=True, default=True, verbose_name='Estado del pago')),
                ('pk_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Llave primaria pago')),
                ('d_reservation', models.DateTimeField(null=True, verbose_name='Fecha de creación del registro')),
                ('d_created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación del registro')),
                ('fk_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.customer', verbose_name='Llave foránea cliente')),
                ('fk_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.employee', verbose_name='Llave foránea empleado')),
                ('fk_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.payment', verbose_name='Llave foránea Pago')),
                ('fk_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.student', verbose_name='Llave foránea estudiante')),
            ],
            options={
                'verbose_name': 'Medio de pago',
                'verbose_name_plural': 'Medios de pagos',
            },
        ),
    ]
