import requests
import random
import os

# API Configurations (Inhe GitHub Secrets mein daalna hai)
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
AYRSHARE_API_KEY = os.getenv('AYRSHARE_API_KEY')

def get_nature_image():
    url = "https://api.pexels.com/v1/search?query=nature&per_page=50"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers).json()
    image = random.choice(response['photos'])
    return image['src']['large'], image['alt']

def post_to_telegram(img_url, caption):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    data = {"chat_id": TELEGRAM_CHAT_ID, "photo": img_url, "caption": caption}
    requests.post(url, data=data)

def post_to_ayrshare(img_url, caption):
    url = "https://api.ayrshare.com/api/post"
    headers = {"Authorization": f"Bearer {AYRSHARE_API_KEY}"}
    data = {
        "post": caption,
        "mediaUrls": [img_url],
        "platforms": ["facebook", "instagram", "twitter"] # Jo aapne connect kiye hon
    }
    requests.post(url, json=data, headers=headers)

if __name__ == "__main__":
    img_url, title = get_nature_image()
    
    # AI-style Description & Hashtags
    description = f"🌿 {title}\n\nNature is the art of God. ✨\n\n#nature #photography #wildlife #serenity #naturelovers"
    
    # Posting
    post_to_telegram(img_url, description)
    post_to_ayrshare(img_url, description)
    print("Post successful!")
