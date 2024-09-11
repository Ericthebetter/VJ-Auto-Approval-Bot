# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22485565"))
    API_HASH = getenv("API_HASH", "f8b51bd3132b314c214b1d9a754500f2")
    BOT_TOKEN = getenv("BOT_TOKEN", "7494930693:AAGO5P7Gt0WX7WZt5zivgPqUrVguQmS5aiA")
    FSUB = getenv("FSUB", "IAmonitorBot")
    CHID = int(getenv("CHID", "-1002452163040"))
    SUDO = list(map(int, getenv("SUDO", "6156115163").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
