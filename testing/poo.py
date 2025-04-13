BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\003[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
DARK_GRAY = '\033[90m'
LIGHT_RED = '\033[91m'
LIGHT_GREEN = '\033[92m'
LIGHT_YELLOW = '\033[93m'
LIGHT_BLUE = '\033[94m'
LIGHT_MAGENTA = '\033[95m'
LIGHT_CYAN = '\033[96m'
LIGHT_WHITE = '\033[97m'

def main():
    print("testing all colors: ")
    print(f"{BLACK}Black{RESET}")
    print(f"{RED}Red{RESET}")
    print(f"{GREEN}Green{RESET}")
    print(f"{YELLOW}Yellow{RESET}")
    print(f"{BLUE}Blue{RESET}")
    print(f"{MAGENTA}Magenta{RESET}")
    print(f"{CYAN}Cyan{RESET}")
    print(f"{WHITE}White{RESET}")
    print(f"{DARK_GRAY}Dark Gray{RESET}")
    print(f"{LIGHT_RED}Light Red{RESET}")
    print(f"{LIGHT_GREEN}Light Green{RESET}")
    print(f"{LIGHT_YELLOW}Light Yellow{RESET}")
    print(f"{LIGHT_BLUE}Light Blue{RESET}")
    print(f"{LIGHT_MAGENTA}Light Magenta{RESET}")
    print(f"{LIGHT_CYAN}Light Cyan{RESET}")
    print(f"{LIGHT_WHITE}Light White{RESET}")
    print("testing all colors with background: ")
    print(f"{BLACK}Black{RESET}")
    print(f"{RED}Red{RESET}")

if __name__ == "__main__":
    main()