from django import template

register = template.Library()

@register.inclusion_tag("memes/meme_card.html")
def meme_card(meme):
    return {"meme":meme}