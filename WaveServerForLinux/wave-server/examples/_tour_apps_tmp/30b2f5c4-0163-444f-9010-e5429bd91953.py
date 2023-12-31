# Import `Site` and the `ui` module from the `h2o_wave` package
from h2o_wave import site, ui

# Get the web page at route '/demo'.
# If you're running this example on your local machine,
# this page will refer to http://localhost:10101/demo.
page = site['/30b2f5c4-0163-444f-9010-e5429bd91953']

# Add a Markdown card named `hello` to the page.
page['hello'] = ui.markdown_card(
    box='1 1 2 2',
    title='Hello World!',
    content='And now for something completely different!',
)

# Finally, sync the page to send our changes to the server.
page.save()