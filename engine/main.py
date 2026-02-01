from textual.app import App, ComposeResult
from textual.widgets import Static, Label, ProgressBar, Input
from textual.containers import Container, Horizontal
from textual.reactive import reactive  


class MainConsole(App):
    CSS_PATH = "console_layout.tcss"

    def compose(self) -> ComposeResult:
        #setting up the progress bar to it's default value
        with Container(id="mini_status"):
            with Horizontal(classes="stat_row"):
                yield Label("Name: XYZ")
                yield Label("Level: 5", classes="right")

            with Horizontal(classes="stat_row"):
                yield Label("Race: Draconic")
                yield Label("XP: 90/100", classes = "right")

            with Horizontal(classes="stat_row"):
                yield Label("Class: Wizard")
                yield Label("Vitality: 5/5", classes="right")
            
            with Horizontal(classes="stat_row"):
                yield Static("HP: ", classes="label_hp_mana")
                yield ProgressBar(total = 100, show_eta=False, id="hp_bar")

            with Horizontal(classes="stat_row"):
                yield Static("Mana: ", classes="label_hp_mana")
                yield ProgressBar(total = 100, show_eta=False, id="mana_bar")

        with Container(id="input_window"):
            with Horizontal(classes="input"):
                yield Input(placeholder ="Interact with the character here")

    def on_mount(self):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        mana_bar = self.query_one("#mana_bar", ProgressBar)

        hp_bar.progress = 100
        mana_bar.progress = 100

    def spell_cast(self, spell_cost):
        mana_bar = self.query_one("#mana_bar", ProgressBar)
        mana_bar.progress -= spell_cost

    # taking the damage is getting accounted for here
    def take_damage(self, amount):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        hp_bar.progress -= amount

    # leveling up autoresets the HP
    def level_up(self):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        mana_bar = self.query_one("#mana_bar", ProgressBar)

        hp_bar.progress = 100
        mana_bar.progress = 100

app = MainConsole()
if __name__ == "__main__":
    app.run()