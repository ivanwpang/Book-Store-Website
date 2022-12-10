# Generated by Django 4.1.3 on 2022-12-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covebooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]