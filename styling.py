RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"


def colored_text(text, color, bold=False):
    effect = BOLD if bold else ""
    return f"{effect}{color}{text}{RESET}"