def screen_print(message, color="default"):
    """
    Prints a custom message to the screen with optional color.

    Args:
        message (str): The message to print.
        color (str): The color of the message. Options are 'red', 'yellow', 'green', 'cyan', or 'default'.

    Returns:
        str: The printed message with color.
    """
    # ANSI color codes for terminal output
    colors = {
        "red": "\033[31m",
        "yellow": "\033[33m",
        "green": "\033[32m",
        "cyan": "\033[36m",
        "default": "\033[0m"  # Resets color to default
    }

    # Get the ANSI code for the selected color
    color_code = colors.get(color.lower(), colors["default"])

    # Format the message with the color
    colored_message = f"{color_code}{message}{colors['default']}"

    # Print the colored message
    print(colored_message)

    return colored_message
