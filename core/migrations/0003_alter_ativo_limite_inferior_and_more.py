# Generated by Django 5.1.4 on 2025-01-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_ativo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='limite_inferior',
            field=models.DecimalField(decimal_places=2, help_text='Limite inferior do túnel de preço', max_digits=10),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='limite_superior',
            field=models.DecimalField(decimal_places=2, help_text='Limite superior do túnel de preço', max_digits=10),
        ),
        migrations.AlterField(
            model_name='cotacao',
            name='preco',
            field=models.DecimalField(decimal_places=2, help_text='Preço registrado do ativo', max_digits=10),
        ),
    ]
