"""
garden_advice.py
A gardening advice app that provides tips based on the current month and season.
"""

import datetime


def get_current_month():
    """Returns the name of the current month."""
    return datetime.datetime.now().strftime("%B")


def get_season(month):
    """Returns the season based on the given month name."""
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
    """Returns a gardening tip for the given month."""
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
    """Returns general advice based on the current season."""
    advice = {
        "Spring": "Great time to plant and fertilise.",
        "Summer": "Focus on watering and pest control.",
        "Autumn": "Harvest and prepare for cooler months.",
        "Winter": "Plan next year's garden and rest the soil."
    }
    return advice.get(season, "No advice available.")


def display_advice():
    """Displays the current month's gardening tip and season advice."""
    month = get_current_month()
    season = get_season(month)
    print(f"Month: {month}")
    print(f"Tip: {get_monthly_tip(month)}")
    print(f"Season: {season}")
    print(f"Season Advice: {get_season_advice(season)}")


# --- Main execution ---
display_advice()
