from PIL import Image, ImageDraw, ImageChops, ImageFilter, ImageFont
import requests
from io import BytesIO


def generate_rank_image(avatar_url, level, xp):
    next_level_xp = (level + 1) * 100
    progress_percentage = xp / next_level_xp

    width, height = 500, 200
    background_color = (60, 60, 60)

    try:
        response = requests.get(avatar_url)
        if response.status_code == 200:
            avatar = Image.open(BytesIO(response.content))
            avatar = circle(avatar, (100, 100), background_color)
        else:
            print(f"Erreur lors du téléchargement de l'avatar: {response.status_code}")
            return
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'avatar: {str(e)}")
        return

    # Créer l'image de fond
    background = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(background)

    # Ajouter l'avatar à l'image de fond
    background.paste(avatar, (20, 50))

    # Charger la police
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()

    # Ajouter le niveau
    draw.text((150, 50), f"Niveau: {level}", font=font, fill=(255, 255, 255))

    # Ajouter la barre de progression
    bar_width = 300
    bar_height = 30
    bar_x = 150
    bar_y = 100
    progress_width = int(bar_width * progress_percentage)

    # Dessiner la barre de progression (fond)
    draw.rectangle((bar_x, bar_y, bar_x + bar_width, bar_y + bar_height), outline=(255, 255, 255), width=2)

    # Dessiner la barre de progression (progression)
    draw.rectangle((bar_x, bar_y, bar_x + progress_width, bar_y + bar_height), fill=(0, 255, 0))

    # Ajouter le texte de progression
    draw.text((bar_x, bar_y - 25), f"XP: {xp} / {next_level_xp}", font=font, fill=(255, 255, 255))

    # Sauvegarder l'image
    image_path = "assets/rank/rank_image.png"
    background.save(image_path)

    return image_path


def circle(pfp, size=(215, 215), background_color=(0, 0, 0)):
    # Charger l'image pfp si elle n'est pas déjà une instance Image.Image
    if not isinstance(pfp, Image.Image):
        image = Image.open(pfp).convert("RGBA")
    else:
        image = pfp.convert("RGBA")

    # Redimensionner l'image à la taille spécifiée
    image = image.resize(size, Image.LANCZOS)

    # Créer un masque circulaire
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    # Créer une image RGBA avec fond transparent et appliquer le masque
    result = Image.new('RGBA', size, background_color)
    result.paste(image, (0, 0), mask)

    # Appliquer le masque comme canal alpha pour rendre l'image circulaire
    result.putalpha(mask)

    return result