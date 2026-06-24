"""
garden_advice.py
================
A gardening advice application for enthusiasts around the world.

This module provides:
- Dynamic detection of the current month using Python's datetime module
- Season detection based on the current month
- Monthly gardening tips tailored to each month of the year
- Season-based gardening advice

Author: Charlotte Hill
Last Updated: June 2026
"""

import datetime


def get_current_month():
    """
    Detect and return the current month as a full month name.

    Returns:
        str: The full name of the current month (e.g., 'June').

    Example:
        >>> get_current_month()
        'June'
    """
    return datetime.datetime.now().strftime("%B")


def get_season(month):
    """
    Determine the season based on the provided month name.

    Args:
        month (str): The full name of a month (e.g., 'June').

    Returns:
        str: The season name — 'Spring', 'Summer', 'Autumn', or 'Winter'.

    Example:
        >>> get_season('June')
        'Summer'
    """
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    autumn = ["September", "October", "November"]

    if month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    elif month in autumn:
        return "Autumn"
    else:
        return "Winter"


def get_monthly_tip(month):
    """
    Retrieve a gardening tip for the specified month.

    Args:
        month (str): The full name of the month (e.g., 'June').

    Returns:
        str: A gardening tip relevant to the given month.
             Returns 'No tip available.' if the month is not found.

    Example:
        >>> get_monthly_tip('June')
        'Harvest early crops and deadhead flowers.'
    """
    tips = {
        "January": "Prune roses and plan your spring garden.",
        "February": "Start seeds indoors for early spring planting.",
        "March": "Begin planting cold-hardy vegetables.",
        "April": "Plant flowers and start composting.",
        "May": "Watch for pests and water regularly.",
        "June": "Harvest early crops and deadhead flowers.",
        "July": "Water deeply and mulch to retain moisture.",
        "August": "Plant autumn crops like kale and broccoli.",
        "September": "Collect seeds and prepare beds for winter.",
        "October": "Plant bulbs for spring blooming.",
        "November": "Protect tender plants from frost.",
        "December": "Rest, plan, and order seed catalogues."
    }
    return tips.get(month, "No tip available.")


def get_season_advice(season):
    """
    Retrieve general gardening advice for the specified season.

    Args:
        season (str): The name of the season (e.g., 'Summer').

    Returns:
        str: General advice relevant to the given season.
             Returns 'No advice available.' if the season is not found.

    Example:
        >>> get_season_advice('Summer')
        'Focus on watering and pest control.'
    """
    advice = {
        "Spring": "Great time to plant and fertilise.",
        "Summer": "Focus on watering and pest control.",
        "Autumn": "Harvest and prepare for cooler months.",
        "Winter": "Plan next year's garden and rest the soil."
    }
    return advice.get(season, "No advice available.")


def display_advice():
    """
    Display the current month's gardening tip and season advice.

    Calls get_current_month() and get_season() to dynamically determine
    the current month and season, then prints the relevant tip and advice.
    """
    month = get_current_month()
    season = get_season(month)
    print(f"Month: {month}")
    print(f"Tip: {get_monthly_tip(month)}")
    print(f"Season: {season}")
    print(f"Season Advice: {get_season_advice(season)}")


# --- Main execution ---
display_advice()
