from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label

class LabelApp(App):
    CSS = """
    Horizontal {
        height: 1;
        width: 100%;
    }
    #name {
        width: 1fr; /* This label grows to fill all empty space */
    }
    #level {
        width: auto; /* This stays as small as possible on the right */
        text-align: right;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("Name: John Doe", id="name")
            yield Label("Level: 10", id="level")

if __name__ == "__main__":
    LabelApp().run()