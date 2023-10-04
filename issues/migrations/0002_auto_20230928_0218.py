# Generated by Django 4.2.5 on 2023-09-28 02:18

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "to do": "an issue for which work has not yet been started",
        "in progress": "an issue that is actively being worked on",
        "done": "an issue for which work has been completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]