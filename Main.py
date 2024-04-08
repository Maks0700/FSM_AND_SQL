from aiogram import Dispatcher,Bot,executor,types
from dotenv import load_dotenv
import os
import asyncio
from icecream import ic
import sys
from bot_name.handlers.user_handlers import list_handlers #Import variable list_handlers 
import logging







load_dotenv("bot_name\.env") # Using the function load_dotenv in order to load token Bot with path file
token_main=os.getenv("API_TOKEN")

def register_handlers(dp: Dispatcher): #create function for register all handlers with arguments Dispatcher
   
    for part_list_handlers in list_handlers: # A loop for proccess all handlers 
        part_list_handlers(dp)
    
    
bot=Bot(token=token_main)
async def main()->None: # The function main for start bot
        
        
        
        dp=Dispatcher(bot)
        register_handlers(dp) # The call function register_handlers for register handlers 
        # Then made the brunch of code try/except for start bot 
        try:
            await dp.start_polling() # Here start bot without errors 
        except Exception as _ex:
            ic(f"This is error as {_ex}") # In case errors
            
        
     
if __name__=="__main__":
    asyncio.run(main()) #The call async function main()            
