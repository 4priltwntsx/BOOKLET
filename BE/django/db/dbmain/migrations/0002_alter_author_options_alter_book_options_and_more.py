# Generated by Django 4.0 on 2023-04-01 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bookcover',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bookgenre',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='booklikes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hashtag',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='paragraph',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='scrap',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='userhashtag',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='userimage',
            options={'managed': False},
        ),
    ]
