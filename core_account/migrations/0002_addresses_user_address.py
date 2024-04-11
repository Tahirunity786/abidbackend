# Generated by Django 5.0.3 on 2024-03-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_text', models.TextField(db_index=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ManyToManyField(db_index=True, to='core_account.addresses'),
        ),
    ]
