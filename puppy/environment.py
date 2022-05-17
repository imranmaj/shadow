from puppy.config import Config
from puppy.static import CONFIG_FILENAME

config = Config()


def print_info():
    print(f"Puppy")
    print("-------")
    print("Options:")
    if config.is_new:
        print(f"Created a config file ({CONFIG_FILENAME})")
    print(f"Patch reversion {'enabled' if config.revert_patch else 'disabled'}")
    if config.backend == "ugg":
        print(f"Backend is U.GG")
    elif config.backend == "mobalytics":
        print(f"Backend is Mobalytics")
    print(f"Flash on {'F' if config.flash_on_f else 'D'}", end="\n\n")
