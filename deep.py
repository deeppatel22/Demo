def how_are_you_deep():
    """Return a deep, thoughtful response about how 'deep' feels."""
    depth_levels = [
        "On the surface, I am calm like still water.",
        "A little deeper, thoughts flow like a gentle current.",
        "Deeper still, ideas swirl like an underwater vortex.",
        "At my core, I am vast, silent, and endlessly deep.",
        "Like the ocean floor — quiet, dark, and full of mystery.",
    ]

    print("How are you, Deep?\n")
    for i, level in enumerate(depth_levels, start=1):
        print(f"Level {i}: {level}")

    print("\nI am deep... beyond what words can fully reach.")


if __name__ == "__main__":
    how_are_you_deep()
