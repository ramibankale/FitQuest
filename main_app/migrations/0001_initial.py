# Generated by Django 4.2.3 on 2023-08-02 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CE', 'Cardiovascular Exercise'), ('ST', 'Strength Training'), ('FS', 'Flexibility and Stretching'), ('BS', 'Balance and Stability'), ('CC', 'Core Conditioning'), ('ET', 'Endurance Training'), ('BT', 'Bodyweight Training'), ('RM', 'Relaxation and Mindfulness')], max_length=100, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
