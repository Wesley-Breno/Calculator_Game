# Generated by Django 3.2.5 on 2023-03-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pontuacoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=3)),
                ('pontos', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pontuacoes',
        ),
    ]
