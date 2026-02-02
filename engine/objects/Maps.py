from textual.widgets import RichLog


class Maps():
    TOWN_MAP = r"""
        [green]
              .           .
            /' \         / \ 
           /   |   _    /   \      [bold white]THE TOWN OF OAKHAVEN[/]
           |   |  | |   |   |
        ___|___|__| |___|___|__________________________
                |  _  |
                | | | |   [bold yellow]THE INN[/]
                | |_| |  (Type 'enter inn')
        ________|_____|________________________________
        [/green]
    """

INN_INTERIOR = r"""
        [yellow]
        _______________________________________________
        |                                             |
        |   [BAR]             [TABLES]                |
        |   (Barkeep)         (Wiz, Stranger)         |
        |                                             |
        |   People here:                              |
        |   1. The Barkeep                            |
        |   2. Drunk Wizard                           |
        |   3. Mysterious Stranger                    |
        |_____________________________________________|
        [/yellow]
        """