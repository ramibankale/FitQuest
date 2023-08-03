# Generated by Django 4.2.3 on 2023-08-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CE', 'Cardiovascular Exercise'), ('ST', 'Strength Training'), ('FS', 'Flexibility and Stretching'), ('BS', 'Balance and Stability'), ('CC', 'Core Conditioning'), ('ET', 'Endurance Training'), ('BT', 'Bodyweight Training'), ('RM', 'Relaxation and Mindfulness')], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='fitness_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main_app.fitnesscategory'),
            preserve_default=False,
        ),
    ]