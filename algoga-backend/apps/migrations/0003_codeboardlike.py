# Generated by Django 3.1.7 on 2021-04-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBoardLike',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('user_seq', models.IntegerField()),
                ('code_board_seq', models.IntegerField()),
            ],
            options={
                'db_table': 'code_board_like',
                'managed': False,
            },
        ),
    ]
