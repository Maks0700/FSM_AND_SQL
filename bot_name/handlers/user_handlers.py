from aiogram import types,Dispatcher

from aiogram.dispatcher.filters import Text






def reg_start_cmd(dp:Dispatcher):
    from bot_name.Functions.functions_main import cmd_start
    dp.register_message_handler(cmd_start,commands=["start"])

def reg_info_graphics(dp: Dispatcher):
    from bot_name.Functions.functions_main import info_gr
    dp.register_message_handler(info_gr,Text(equals="Инфографика",ignore_case=True))

def reg_info_instagram(dp: Dispatcher):
    from bot_name.Functions.functions_main import insta_but
    dp.register_message_handler(insta_but,Text(equals="Дизайн Инстаграма",ignore_case=True))
    
def reg_info_vkontakte(dp: Dispatcher):
    from bot_name.Functions.functions_main import vk_but
    dp.register_message_handler(vk_but,Text(equals="Дизайн Вконтакте",ignore_case=True))
    
def reg_info_creatives(dp: Dispatcher):
    from bot_name.Functions.functions_main import cr_but
    dp.register_message_handler(cr_but,Text(equals="Креативы",ignore_case=True))


def reg_check_content_text(dp: Dispatcher):
    from bot_name.Functions.functions_main import cmd_check
    dp.register_message_handler(cmd_check,content_types="text")
    

def reg_callback_data_proccess(dp: Dispatcher):
    from bot_name.Functions.functions_main import proccess_cmd
    dp.register_callback_query_handler(proccess_cmd)



list_handlers=[reg_start_cmd,reg_info_instagram,reg_info_creatives
               ,reg_info_graphics,reg_info_vkontakte,reg_callback_data_proccess,reg_check_content_text]
    
    
