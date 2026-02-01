from textual.app import App, ComposeResult
from textual.widgets import Static, ContentSwitcher, DataTable, Digits, ProgressBar
from textual.containers import Container
from textual.reactive import reactive  

class MainConsole(App):
    CSS_PATH = "console_layout.tcss"

    def compose(self) -> ComposeResult:
        #setting up the progress bar to it's default value
        yield ProgressBar(total = 100, show_eta=False, id="hp_bar")
        yield ProgressBar(total = 100, show_eta=False, id="mana_bar")
    
    def on_mount(self):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        mana_bar = self.query_one("#mana_bar", ProgressBar)

        hp_bar.progress = 100
        mana_bar.progress = 100

    def spell_cast(self, spell_cost):
        mana_bar = self.query_one("#mana_bar", ProgressBar)
        mana_bar -= spell_cost

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