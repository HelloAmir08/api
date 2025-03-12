# Generated by Django 5.1.7 on 2025-03-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('stock', models.BooleanField(default=False)),
            ],
        ),
    ]
