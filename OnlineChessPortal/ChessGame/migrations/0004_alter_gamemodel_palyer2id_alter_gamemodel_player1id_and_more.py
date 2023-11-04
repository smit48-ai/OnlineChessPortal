# Generated by Django 4.0 on 2023-10-30 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_groups_alter_user_user_permissions'),
        ('ChessGame', '0003_remove_gamemodel_status_gamemodel_winner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='palyer2Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='users.user'),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='player1Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='users.user'),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='users.user'),
        ),
    ]
