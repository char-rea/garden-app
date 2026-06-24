# Garden.py - a simple gardening advice platform

# Get season and plant type from the user
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()

# Dictionary storing gardening advice
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers."
}

plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

# Function to generate gardening advice
def get_advice(season, plant_type):
    advice = ""

    # Determine advice based on season
    advice += season_advice.get(season, "No advice for this season.") + "\n"

    # Determine advice based on plant type
    advice += plant_advice.get(plant_type, "No advice for this type of plant.")

    return advice

# Recommend plants based on season
if season == "summer":
    recommendation = "Recommended plants: Sunflowers, Marigolds"
elif season == "winter":
    recommendation = "Recommended plants: Pansies, Kale"
else:
    recommendation = "No plant recommendations available."

# Print the generated advice and recommendations
print("\nGardening Advice:")
print(get_advice(season, plant_type))

print("\n" + recommendation)