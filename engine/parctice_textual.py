from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Welcome, Button, Label
from textual import events

import rich
import questionary

# region Base color changing on button press
class EventApp(App):
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",        
    ]

    # sets the background upon launch to darkblue
    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    # sets the background upon pressing keys from 0-9 to colors stored in the COLORS variable
    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key)]

class MyApp(App):
    pass
# endregion

# region Just a simple welcome text, from the built in feature of the textual library
class WelcomeApp(App):
    # this automatically puts a welcome message to the console
    # def compose(self) -> ComposeResult:
    #     yield Welcome()

    # this puts a welcome message to the console upon a button press
    def on_key(self) -> None:    
        self.mount(Welcome())
    
    def on_button_pressed(self) -> None:
        self.exit()
#endregion

# region Button app
class WelcomeApp_Button(App):
    async def on_key(self) -> None:
        await self.mount(Welcome())
        self.query_one(Button).label = "YES!"

# endregion

# region QuestionApp
class QuestionApp(App[str]):
    def compose(self) -> ComposeResult:
        yield Label("Do you love Textual?")
        yield Button("Yes", id="yes", variant = "primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)

# endregion

#region Vertical layout
class VerticalLayoutExample(App):
    CSS_PATH = "layout.tcss"

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
# endregion

#region Utility container layout
class UtilityContainersExample(App):
    CSS_PATH = "utility_containers.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Static("One"),
                Static("Two"),
                classes = "column",
            ),
            Vertical(
                Static("Three"),
                Static("Four"),
                classes="column",
            ),
        )
# endregion


# region Composing with context managers
class UtilityContextManager(App):
    
    CSS_PATH = "utility_context.tcss"

        
    def compose(self) -> ComposeResult:
            with Horizontal():
                with Vertical(classes="column"):
                    yield Static("One")
                    yield Static("Two")
                with Vertical(classes="column"):
                    yield Static("Three")
                    yield Static("Four")


# endregion

# runs the application
if __name__ == "__main__":
    app = UtilityContextManager()
    app.run()
