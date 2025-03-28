from database.database import db  
import pyrogram  
from pyrogram import Client  
import logging  
import os  
import threading  
import server  # Flask server ko import kar liya

from config import Config  

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
logger = logging.getLogger(__name__)  

logging.getLogger("pyrogram").setLevel(logging.WARNING)  

if __name__ == "__main__":  
    # Ensure download directory exists  
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):  
        os.makedirs(Config.DOWNLOAD_LOCATION)  

    # Bot user collection in MongoDB  
    bot_owner_id = 1337144652  # Replace with actual owner ID  
    db.users.update_one({"_id": bot_owner_id}, {"$set": {"role": "admin"}}, upsert=True)  

    plugins = dict(root="plugins")  

    app = Client(  
        "CONVERTBOT",  
        bot_token=Config.TG_BOT_TOKEN,  
        api_id=Config.APP_ID,  
        api_hash=Config.API_HASH,  
        plugins=plugins  
    )  

    Config.AUTH_USERS.add(bot_owner_id)  # Keep authentication list  

    # Flask server ko alag thread me chalane ke liye  
    threading.Thread(target=server.run).start()  

    app.run()
