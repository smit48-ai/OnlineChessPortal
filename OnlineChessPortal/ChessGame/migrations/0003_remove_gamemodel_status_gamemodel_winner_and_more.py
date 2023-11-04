# Generated by Django 4.0 on 2023-10-30 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_rating'),
        ('ChessGame', '0002_remove_gamemodel_moves_remove_gamemodel_winner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='status',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='winner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='users.user', to_field='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='palyer2Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='users.user', to_field='username'),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='player1Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='users.user', to_field='username'),
        ),
    ]