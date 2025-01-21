import solara

import debugpy
debugpy.listen(('localhost', 5678))
debugpy.wait_for_client()
print("debugger attached...")

clicks = solara.reactive(0)


@solara.component
def Page():
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        debugpy.breakpoint()
        clicks.value += 1
        print("clicks", clicks)  # noqa

    solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)
