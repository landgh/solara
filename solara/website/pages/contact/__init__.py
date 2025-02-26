import solara
from solara.website.components.sidebar import Sidebar
from solara.website.components.contact import Contact

Sidebarr = Sidebar


@solara.component
def Page():
    solara.Markdown("""
# Contact

## Business

Solara is developed mostly by Maarten Breddels and Mario Buikhuizen, Founders
of [Widgetti](https://widgetti.io/).

For business inquiries, please reach out using the form below, or send an email to [contact@solara.dev](mailto:contact@solara.dev) regarding Solara, or [info@widgetti.io](mailto:info@widgetti.io) regarding more general Jupyter related matters.
""")
    Contact(
        title="Contact Us", subtitle="Please fill out the form below and we will get back to you as soon as possible.", email_subject="Contact Form Submission"
    )
    solara.Markdown(
        """
## Community

If you want to share your thoughts, share your experiences, or just want to talk
to other people using and developing on Solara, consider using [GitHub discussions](https://github.com/widgetti/solara/discussions) for asynchronous discussions
or consider joining discord for more synchronous discussions.


[![Discord Shield](https://discordapp.com/api/guilds/1106593685241614489/widget.png?style=banner2)](https://discord.gg/dm4GKNDjXN)
"""
    )
