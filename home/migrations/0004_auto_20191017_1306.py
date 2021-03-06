# Generated by Django 2.2.5 on 2019-10-17 13:06

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191017_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='leftcolumn',
            new_name='arriendos_contrato',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='midcolumn',
            new_name='arriendos_documentos',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='rightcolumn',
            new_name='arriendos_subsidios',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='title_leftcolumn',
            new_name='info_subsidios',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='title_midcolumn',
            new_name='ventas_contado',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='title_rightcolumn',
            new_name='ventas_credito',
        ),
        migrations.AddField(
            model_name='homepage',
            name='ventas_mixto',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='ventas_subsidio',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
