# Import `Site` and the `ui` module from the `h2o_wave` package
from h2o_wave import site, ui

# Get the web page at route '/demo'.
# If you're running this example on your local machine,
# this page will refer to http://localhost:10101/demo.
page = site['/70802ec7-7923-4481-978e-26989851d8bb']

# Add a Markdown card named `hello` to the page.
page['hello'] = ui.markdown_card(
    box='1 1 2 2',
    title='Hello World!',
    content='And now for something completely different!',
)

# Finally, sync the page to send our changes to the server.
page.save()