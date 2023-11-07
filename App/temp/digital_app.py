import time
from h2o_wave import site, ui

# Grab a reference to the page at route '/hello'
page = site['/hello']

# Add a markdown card to the page.
page['quote'] = ui.markdown_card(
    box='1 1 2 2',
    title='This is digital app !!!',
    content='"The Internet? Is that thing still around?" - *Homer Simpson*',
)

page = site['/beer']

beer_card = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='99 Bottles of Beer',
    content='',
))

for i in range(99, 0, -1):
    beer_card.content = f"""
{i} bottles of beer on the wall, {i} bottles of beer.

Take one down, pass it around, {i - 1} bottles of beer on the wall...
"""
    page.save()
    time.sleep(1)
