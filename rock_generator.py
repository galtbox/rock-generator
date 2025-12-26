#!/usr/bin/env python3
"""
EOS Rock Generator
Combines EOS Rock structure with Dan Sullivan's Impact Filter concept.
Generates formatted rocks for pasting into 90.io.
"""

import textwrap
from datetime import datetime, timedelta


def get_input(prompt: str, multiline: bool = False) -> str:
    """Get input from user, supporting multiline for longer responses."""
    print(f"\n{prompt}")
    if multiline:
        print("(Enter a blank line when done)")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return "\n".join(lines)
    return input("> ").strip()


def get_success_criteria() -> list[str]:
    """Collect success criteria (what will be true when done)."""
    print("\n" + "=" * 60)
    print("SUCCESS CRITERIA: What will be true when this rock is done?")
    print("=" * 60)
    print("Think about specific, measurable outcomes.")
    print("Enter each criterion on its own line. Blank line when done.\n")

    criteria = []
    index = 1
    while True:
        criterion = input(f"{index}. ").strip()
        if criterion == "":
            if criteria:
                break
            print("Please enter at least one success criterion.")
            continue
        criteria.append(criterion)
        index += 1

    return criteria


def format_rock(title: str, owner: str, criteria: list[str]) -> str:
    """Format the rock for 90.io paste."""

    # Build the formatted output
    output = []
    output.append("=" * 60)
    output.append(f"ROCK: {title}")
    output.append("=" * 60)
    output.append("")
    output.append(f"Owner: {owner}")
    output.append("")
    output.append("SUCCESS CRITERIA (What will be true when done):")
    output.append("-" * 40)

    for i, criterion in enumerate(criteria, 1):
        # Wrap long criteria for readability
        wrapped = textwrap.fill(criterion, width=55, subsequent_indent="   ")
        output.append(f"☐ {wrapped}")

    output.append("")
    output.append("=" * 60)

    return "\n".join(output)


def format_rock_simple(title: str, owner: str, criteria: list[str]) -> str:
    """Format the rock in a simpler format for 90.io."""

    output = []
    output.append(f"{title}")
    output.append("")
    output.append("What will be true when done:")

    for criterion in criteria:
        output.append(f"• {criterion}")

    return "\n".join(output)


def main():
    print("\n" + "=" * 60)
    print("  EOS ROCK GENERATOR")
    print("  Powered by Impact Filter thinking")
    print("=" * 60)

    # Gather inputs
    title = get_input("What is the rock? (brief title)")
    owner = get_input("Who owns this rock?")
    criteria = get_success_criteria()

    # Generate output
    print("\n" + "=" * 60)
    print("  YOUR ROCK (copy and paste into 90.io)")
    print("=" * 60 + "\n")

    # Show simple format (better for 90.io)
    rock_output = format_rock_simple(title, owner, criteria)
    print(rock_output)

    print("\n" + "-" * 60)
    print("Rock generated! Copy the text above into 90.io.")
    print("-" * 60 + "\n")

    # Offer to save to file
    save = input("Save to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = title.lower().replace(" ", "_")[:30] + "_rock.txt"
        with open(filename, 'w') as f:
            f.write(rock_output)
        print(f"Saved to: {filename}")


if __name__ == "__main__":
    main()
