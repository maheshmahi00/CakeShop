# Generated by Django 3.2.18 on 2023-04-28 07:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shape', models.CharField(choices=[('round', 'round'), ('square', 'square'), ('triangle', 'triangle')], max_length=100, null=True)),
                ('layers', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('weight', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakes', to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('shipped', 'shipped'), ('in-cart', 'in-cart'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('return', 'return')], default='order-placed', max_length=100)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('in-cart', 'in-cart'), ('order-placed', 'order-placed')], default='in-cart', max_length=100)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
