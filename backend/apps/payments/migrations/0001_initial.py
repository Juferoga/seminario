# Generated by Django 4.2.2 on 2023-09-25 00:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('b_status', models.BooleanField(auto_created=True, default=True, verbose_name='Estado del pago')),
                ('pk_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Llave primaria pago')),
                ('n_type', models.IntegerField(choices=[(0, 'Tarjeta de crédito'), (1, 'Tarjeta de débito'), (2, 'Efectivo'), (3, 'Otros')], default=3, verbose_name='Tipo de pago')),
                ('d_created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación del registro')),
                ('fk_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.customer', verbose_name='Llave foránea cliente')),
            ],
            options={
                'verbose_name': 'Medio de pago',
                'verbose_name_plural': 'Medios de pagos',
            },
        ),
    ]
