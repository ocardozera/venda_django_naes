# Generated by Django 4.0.4 on 2022-09-22 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14)),
                ('cpf', models.CharField(max_length=11)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.estabelecimento')),
                ('produto', models.ManyToManyField(to='cadastros.produto')),
            ],
        ),
    ]
