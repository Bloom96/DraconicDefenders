from textual.app import App, ComposeResult
from textual.widgets import Static, Label, ProgressBar, Input, RichLog
from textual.containers import Container, Horizontal, Vertical, VerticalScroll 


# This is the main class that runs your application.
# It inherits from 'App', which gives it all the standard Textual functionality.

class MyCharacters:
    def __init__(self, name, hp, mp, level, char_class, char_race):
        self.Name = name
        self.HP = hp
        self.MP = mp
        self.Level = level
        self.Char_class = char_class
        self.Char_race = char_race
    
    # CHANGE: Only do math here. Do not try to touch the UI.
    def take_damage(self, amount):
        self.HP -= amount
        if self.HP < 0: 
            self.HP = 0 # Prevent negative HP
class MainConsole(App):
    
    # Link to the CSS file that controls the look (colors, sizes, layout).
    CSS_PATH = "console_layout.tcss"

    def __init__(self):
        super().__init__()
        self.player_char = MyCharacters("Reinhard", 100, 100, 4, "Wizard", "Human")
        self.target_char = MyCharacters("Bo'hsa", 100, 0, 2, "Rouge", "ELf")

    # --------------------------------------------------------------------------
    # COMPOSE: This is where you build the UI structure (The Skeleton)
    # --------------------------------------------------------------------------
    def compose(self) -> ComposeResult:
        """
        The compose method is called automatically when the app starts.
        You 'yield' widgets here to put them on the screen.
        """


        # --- LEFT COLUMN ---
        # We wrap the entire left side in a Vertical container so boxes stack top-to-bottom.
        with Vertical(id="left_column"):
            
            # BOX 1: Status
            # 'id' is unique (used for logic), 'classes' allows shared styling (green borders).
            with Container(id="mini_status", classes="box"):
                # Title of the box
                yield Label("--- STATUS ---", classes="box_title")
                
                # Row 1: Name and Level
                # We use Horizontal so "Name" is on the left and "Level" is on the right.
                with Horizontal(classes="stat_row"):
                    yield Label(f"Name: {self.player_char.Name}")
                    yield Label(f"Lvl: {self.player_char.Level}", classes="right") # 'right' class aligns text to the right
                
                # Row 2: Race and XP
                with Horizontal(classes="stat_row"):
                    yield Label(f"Race: {self.player_char.Char_race}")
                    yield Label("XP: 90", classes = "right")
                
                # Row 3: Class and Vitality
                with Horizontal(classes="stat_row"):
                    yield Label(f"Class: {self.player_char.Char_class}")
                    yield Label("Vit: 5/5", classes="right")
                
                # Row 4: HP Bar
                with Horizontal(classes="stat_row"):
                    yield Static("HP: ", classes="label_hp_mana")
                    # 'total=100' sets the max value. 'show_eta=False' hides the time remaining.
                    yield ProgressBar(total=self.player_char.HP, show_eta=False, id="hp_bar")

                # Row 5: Mana Bar
                with Horizontal(classes="stat_row"):
                    yield Static("MP: ", classes="label_hp_mana")
                    yield ProgressBar(total=self.player_char.MP, show_eta=False, id="mana_bar")
                
                yield Label("Current location: Helmuth")

            # BOX 2: Inventory (Middle Box)
            # HOW TO ADD ITEMS: Simply yield more Labels here.
            with Container(id="inventory_box", classes="box"):
                yield Label("--- INVENTORY ---", classes="box_title")
                yield Label("- Staff of Fire")
                yield Label("- Potion (x3)")
                yield Label("- Old Map")

            # BOX 3: Quests (Bottom Box)
            with Container(id="quest_box", classes="box"):
                yield Label("--- QUESTS ---", classes="box_title")
                yield Label("1. Find the lost cat")
                yield Label("2. Slay the slime")
            
            with Container(id="target_box", classes="box"):

                yield Label("--- TARGET ---", classes="box_title")
                yield Label("Target: Hesht (Lvl 4)")
                yield Label("Attitude: Neutral")
                yield Label("Target class: Warrior")

                with Horizontal(classes="stat_row"):
                    yield Static("HP: ", classes="tar_label_hp_mana")
                    # 'total=100' sets the max value. 'show_eta=False' hides the time remaining.
                    yield ProgressBar(total=self.target_char.HP, show_eta=False, id="tar_hp_bar")

                # Row 5: Mana Bar
                with Horizontal(classes="stat_row"):
                    yield Static("MP: ", classes="tar_label_hp_mana")
                    yield ProgressBar(total=self.target_char.MP, show_eta=False, id="tar_mana_bar")
        # --- RIGHT COLUMN ---
        # This holds the interactive console.
        with Container(id="right_column"):
            # RichLog is a special widget that acts like a terminal history.
            # wrap=True means if a line is too long, it continues on the next line.
            yield RichLog(id="game_log", wrap=True)
            
            # The input box for user commands.
            yield Input(placeholder="Enter command...", id="console_input")

    # --------------------------------------------------------------------------
    # ON_MOUNT: Setup logic right after the app starts
    # --------------------------------------------------------------------------
    def on_mount(self):
        """
        This runs once, immediately after the UI is drawn.
        Use this to set initial values or print welcome messages.
        """
        # Find the progress bars by ID and set them to full (100%)
        self.query_one("#hp_bar", ProgressBar).progress = 100        
        self.query_one("#tar_hp_bar", ProgressBar).progress = 100

        self.query_one("#mana_bar", ProgressBar).progress = 100
        self.query_one("#tar_mana_bar", ProgressBar).progress = 0
        
        # Get the log widget and print the welcome message
        log = self.query_one("#game_log", RichLog)
        log.write("Welcome to the game console.")
        log.write("Type a command and press Enter.\n")

    # --------------------------------------------------------------------------
    # EVENT HANDLER: When user presses ENTER in the input box
    # --------------------------------------------------------------------------
    def update_bars(self):
        """
        Helper function to sync the UI bars with the Data objects.
        """
        # 1. Update Player Bars
        self.query_one("#hp_bar", ProgressBar).progress = self.player_char.HP
        self.query_one("#mana_bar", ProgressBar).progress = self.player_char.MP
        
        # 2. Update Target Bars
        self.query_one("#tar_hp_bar", ProgressBar).progress = self.target_char.HP
        self.query_one("#tar_mana_bar", ProgressBar).progress = self.target_char.MP


    def on_input_submitted(self, event: Input.Submitted) -> None:
        """
        Textual automatically calls this when an Input widget submits data.
        'event.value' holds the text the user typed.
        """
        user_text = event.value
        
        # 1. Grab the log widget so we can write to it
        log = self.query_one("#game_log", RichLog)
        
        # 2. Echo the user's command to the screen (styled in yellow)
        # Textual supports 'Rich' styling tags like [color]text[/color]
        log.write(f"[yellow]> {user_text}[/yellow]")

        # 3. GAME LOGIC: Check what the user typed
        # .lower() makes it case-insensitive (Heal, heal, HEAL all work)
        if user_text.lower() == "heal":
            self.player_char.HP = 100 
            log.write("[green]You cast heal! HP restored.[/green]")
            # Visual: Update screen
            self.update_bars()
        
        elif user_text.lower() == "get hit":
            self.player_char.take_damage(10) # Call our custom helper function below
            log.write("[red]You took damage![/red]")
            # Visual: Update screen
            self.update_bars()

        elif user_text.lower() == "hit":
            self.target_char.take_damage(10) # Call our custom helper function below
            log.write("[cyan]You hit the target![/cyan]")
            # Visual: Update screen
            self.update_bars()
        
        elif user_text.lower() == "reset":
            self.target_char.HP = 100
            self.player_char.HP = 100
            self.update_bars()

        elif user_text.lower() == "interact":
            log.write("talk\n")
            log.write("leave\n")
            log.write("attack\n")

        elif user_text.lower() == "help":
            log.write("[bold]Available commands:[/bold] heal, hit, get hit, reset, help")

        else:
            # If command isn't recognized
            log.write(f"System: Unknown command '{user_text}'")

        # 4. Clear the input box so it's ready for the next command
        event.input.value = ""

    # --------------------------------------------------------------------------
    # HELPER FUNCTIONS: Custom game logic
    # --------------------------------------------------------------------------


if __name__ == "__main__":
    app = MainConsole()
    app.run()