# Generated by Django 3.1.3 on 2021-02-01 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('patient', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=4096)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('stripe', 'stripe'), ('paypal', 'paypal')], max_length=24)),
                ('amount', models.IntegerField()),
                ('stripe_payment_id', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('paypal_payment_id', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('unpaid', 'unpaid'), ('paid', 'paid'), ('refunded', 'refunded')], max_length=32)),
                ('product', models.CharField(choices=[('text-note', 'text-note'), ('voice-note', 'voice-note'), ('voice-call', 'voice-call'), ('video-call', 'video-call')], max_length=64)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.query')),
            ],
        ),
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, verbose_name='amount')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('cleared', 'cleared'), ('dispute', 'dispute'), ('refunded', 'refunded')], max_length=128, verbose_name='status')),
                ('commission_paid', models.FloatField(default=10, verbose_name='commision')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='created')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('query', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.query')),
            ],
        ),
    ]