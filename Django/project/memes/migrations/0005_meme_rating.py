from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0004_meme_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
