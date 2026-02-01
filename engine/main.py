from textual.app import App, ComposeResult
from textual.widgets import Static, ContentSwitcher, DataTable, Digits, ProgressBar
from textual.containers import Container
from textual.reactive import reactive  

class MainConsole(App):
    CSS_PATH = "console_layout.tcss"

    def compose(self) -> ComposeResult:
        yield ProgressBar(total = 100, progress=100, show_eta=False, id="hp_bar")
    
    def take_damage(self, amount):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        hp_bar.progress -= amount

    def level_up(self):
        hp_bar = self.query_one("#hp_bar", ProgressBar)
        hp_bar.progress = 100


app = MainConsole()
if __name__ == "__main__":
    app.run()