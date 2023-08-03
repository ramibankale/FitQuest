# Generated by Django 4.2.3 on 2023-08-02 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_activity_fitness_category_goal_activities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='activities',
        ),
        migrations.AddField(
            model_name='activity',
            name='fitness_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main_app.fitnesscategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fitnesscategory',
            name='name',
            field=models.CharField(choices=[('CE', 'Cardiovascular Exercise'), ('ST', 'Strength Training'), ('FS', 'Flexibility and Stretching'), ('BS', 'Balance and Stability'), ('CC', 'Core Conditioning'), ('ET', 'Endurance Training'), ('BT', 'Bodyweight Training'), ('RM', 'Relaxation and Mindfulness')], default='CE', max_length=100),
        ),
    ]
