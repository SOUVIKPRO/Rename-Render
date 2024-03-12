# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27198205")

API_HASH = os.environ.get("API_HASH", "ca1d82300eba5b7f89f41ec0abbef395")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6605345574:AAH8AtT3dGNTcDPvru5KVETlW1rATVxLbqQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Smrenameofficial_bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Cyberkingin)     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://sm9832532489:JduFfD1993bnMft9@cluster0.f8p2evo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', ''6782147958).split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
