# Generated by Django 3.1.3 on 2021-02-01 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatIntent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_msg', models.CharField(blank=True, max_length=255, null=True)),
                ('chatType', models.CharField(choices=[('text-note', 'text-note'), ('voice-note', 'voice-note'), ('voice-call', 'voice-call'), ('video-call', 'video-call')], max_length=32)),
                ('status', models.CharField(choices=[('active', 'active'), ('expired', 'expired')], max_length=24)),
                ('expired_at', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('unread_patient', models.IntegerField(default=0)),
                ('unread_doctor', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('expired', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('query', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.query')),
            ],
        ),
        migrations.CreateModel(
            name='VoiceMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4000096)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('chat_intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatintent')),
                ('who', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text-note', 'text-note'), ('voice-note', 'voice-note')], default='text-note', max_length=24)),
                ('voice_note', models.CharField(max_length=10485759, null=True)),
                ('message', models.CharField(max_length=12000, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('chat_intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatintent')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
