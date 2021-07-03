# Generated by Django 3.1.3 on 2021-02-01 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('present_complaint', models.CharField(max_length=4048, verbose_name='present_complaint')),
                ('past_history', models.CharField(max_length=4048, verbose_name='past_history')),
                ('current_medicine', models.CharField(max_length=1024, verbose_name='current_medicine')),
                ('past_medical_history', models.CharField(max_length=4048, verbose_name='past_medical_history')),
                ('past_surgical_history', models.CharField(max_length=4048, verbose_name='past_surgical_history')),
                ('blood_pressure', models.CharField(max_length=256, verbose_name='blood_pressure')),
                ('temperature', models.CharField(max_length=256, verbose_name='temperature')),
                ('height', models.CharField(max_length=256, verbose_name='height')),
                ('weight', models.CharField(max_length=256, verbose_name='weight')),
                ('status', models.CharField(choices=[('unpaid', 'unpaid'), ('open', 'open'), ('assigned', 'assigned'), ('closed', 'closed')], default='unpaid', max_length=128)),
                ('is_archieved', models.BooleanField(default=False)),
                ('is_rated', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('query_type', models.CharField(choices=[('text-note', 'text-note'), ('voice-note', 'voice-note'), ('voice-call', 'voice-call'), ('video-call', 'video-call')], max_length=48)),
                ('notes_from_doctor', models.TextField(blank=True, default=None, null=True)),
                ('amount', models.IntegerField()),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.speciality')),
            ],
            options={
                'verbose_name': 'query',
                'verbose_name_plural': 'queries',
            },
        ),
        migrations.CreateModel(
            name='QueryDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.FileField(upload_to='queries')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.query')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_to_pat_rating', models.IntegerField(default=0, verbose_name='Doctor to patient rating')),
                ('pat_to_doc_rating', models.IntegerField(default=0, verbose_name='Patient to doctor rating')),
                ('doc_to_pat_feedback', models.CharField(max_length=4000, verbose_name='Doctor to patient feedback')),
                ('pat_to_doc_feedback', models.CharField(max_length=4000, verbose_name='Patient to doctor feedback')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('query', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.query')),
            ],
        ),
    ]