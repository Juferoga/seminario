# Generated by Django 4.2.2 on 2023-07-11 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theater', '0002_theater_fk_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('pk_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_state', models.BooleanField(default=False)),
                ('fk_theater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.theater')),
            ],
        ),
    ]
