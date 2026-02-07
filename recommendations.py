def get_recommendations(face_shape, skin_tone):
    recommendations = {
        "hairstyles": [],
        "hair_colors": [],
        "clothing_colors": []
    }

    # Hairstyle Recommendations based on Face Shape
    if face_shape == "Oval":
        recommendations["hairstyles"] = ["Bob Cut", "Long Waves", "Shoulder-Length Shag", "Slicked Back"]
        recommendations["tips"] = "Oval faces are balanced, so most styles work well. Avoid heavy bangs that hide your features."
    elif face_shape == "Round":
        recommendations["hairstyles"] = ["Long Bob (Lob)", "Side-Swept Bangs", "High Ponytail", "Layered Cuts"]
        recommendations["tips"] = "Aim for height and volume on top to elongate the face. Avoid chin-length bobs."
    elif face_shape == "Square":
        recommendations["hairstyles"] = ["Soft Waves", "Side Part", "Long Layers", "Textured Pixie"]
        recommendations["tips"] = "Soften the jawline with wispy bangs or layers starting below the chin."
    elif face_shape == "Heart":
        recommendations["hairstyles"] = ["Chin-Length Bob", "Side-Swept Bangs", "Deep Side Part", "Wavy Layers"]
        recommendations["tips"] = "Balance the forehead width with volume around the chin/jawline."
    elif face_shape == "Diamond":
        recommendations["hairstyles"] = ["Chin-Length Bob", "Deep Side Part", "Pulled Back", "Fringes"]
        recommendations["tips"] = "Show off your cheekbones! Avoid styles that add width at the cheeks."
    elif face_shape == "Oblong":
        recommendations["hairstyles"] = ["Blunt Bangs", "Chin-Length Bob", "Wavy Texture", "Low Bun"]
        recommendations["tips"] = "Add width with waves or curls. Avoid excessive volume on top."
    else:
        recommendations["hairstyles"] = ["Classic Bob", "Soft Layers", "Side Part"]
        recommendations["tips"] = "Experiment with styles that frame your face comfortably."

    # Clothing Color Recommendations based on Skin Tone
    tone_category = skin_tone.split(" ")[0] # Fair, Medium, Dark
    undertone = "Neutral"
    if "(" in skin_tone:
        undertone = skin_tone.split("(")[1].strip(")")

    if tone_category == "Fair":
        if undertone == "Cool":
            recommendations["clothing_colors"] = ["Midnight Blue", "Sunset Red", "Silver Gray"]
            recommendations["hair_colors"] = ["Ash Blonde", "Silver Gray", "Champagne"]
        elif undertone == "Warm":
            recommendations["clothing_colors"] = ["Golden Sand", "Peach", "Olive Drab"]
            recommendations["hair_colors"] = ["Honey", "Strawberry Blonde", "Caramel"]
        else: # Neutral
            recommendations["clothing_colors"] = ["Sandstone", "Soft Pink", "Midnight Blue"]
            recommendations["hair_colors"] = ["Champagne", "Light Brown", "Honey"]

    elif tone_category == "Medium":
        if undertone == "Cool":
            recommendations["clothing_colors"] = ["Midnight Blue", "Olive Drab", "Terracotta"]
            recommendations["hair_colors"] = ["Mocha", "Chestnut", "Deep Espresso"]
        elif undertone == "Warm":
            recommendations["clothing_colors"] = ["Copper", "Deep Amber", "Golden Sand"]
            recommendations["hair_colors"] = ["Caramel", "Honey", "Chestnut"]
        else:
             recommendations["clothing_colors"] = ["Terracotta", "Sandstone", "Earth Brown"]
             recommendations["hair_colors"] = ["Chestnut", "Mocha", "Caramel"]

    elif tone_category == "Dark":
        if undertone == "Cool":
            recommendations["clothing_colors"] = ["Sunset Red", "Midnight Blue", "Silver Gray"]
            recommendations["hair_colors"] = ["Deep Espresso", "Jet Black", "Silver Gray"]
        elif undertone == "Warm":
            recommendations["clothing_colors"] = ["Deep Amber", "Copper", "Earth Brown"]
            recommendations["hair_colors"] = ["Deep Espresso", "Mocha", "Honey"]
        else:
            recommendations["clothing_colors"] = ["Earth Brown", "Sandstone", "Olive Drab"]
            recommendations["hair_colors"] = ["Deep Espresso", "Mocha", "Chestnut"]

    return recommendations
