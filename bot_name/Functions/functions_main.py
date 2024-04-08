from aiogram import Bot,types
import sys
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from datetime import datetime,timedelta
from bot_name.keyboards.user_keyboards import * 
from aiogram.types import MediaGroup,InputMediaPhoto 
from Main import bot


photos_read=["bot_name\Photos_Foulder\Test_photo_1.jpg","bot_name\Photos_Foulder\Test_photo_2.png"]
async def sale(bot:Bot,message:str,user_id:int):
    
    await bot.send_message(chat_id=int(user_id),text="""*✨СКИДКА 10%✨

 Только СЕГОДНЯ при заказе любого дизайна для Вас действует скидка 10% 

 (напишите кодовое слово «скидка10» в личные сообщения дизайнеру)

 ▫️успевайте, время скидки ограничено*""",parse_mode="Markdown")

    
    

async def cmd_start(message:types.Message):
   
    
    await message.answer(f'''*👋Привет {message.from_user.first_name}!! На связи Анна👩‍💻

Хочешь создать стильный и привлекательный дизайн для своего проекта?🤔
Тогда обращайся ко мне!📱

Уже больше года я занимаюсь дизайном и за это время оформила более 180 проектов✨

От меня уходят с ярким и эффективным дизайном🎉

Заказывая у меня, тебе не придется искать сотни дизайнеров для своего бизнеса.
Я предлагаю полный спектр услуг в одном месте 🤩
Переходи на мой телеграмм-канал!!!
⬇️   ⬇️   ⬇️   ⬇️


https://t.me/andesigner5 *''',parse_mode="Markdown",reply_markup=keyboard_main())
    
    
    apschedule=AsyncIOScheduler()
    apschedule.add_job(sale,trigger="date",run_date=datetime.now()+timedelta(minutes=1),kwargs={"bot":bot,"message":message.text,"user_id":message.chat.id})
    apschedule.start()
    
    
async def info_gr(message:types.Message):
   
   with open ("bot_name\Photos_Foulder\InfoGraphics_generally_info.jpg","rb") as photo_info:
        
        await message.answer_photo(photo=photo_info)
        await message.answer(text=""""*📍Создам продающий и сочный дизайн карточек, которые будут выделяться среди Ваших конкурентов.

В стоимость моих услуг входит:
1. Анализ конкурента
2. Отбор фото
3. Обработка и обрезка фото 
4. Разработка дизайна
5. Копирайтинг, создание продающих офферов и текста

Цена: от 399 рублей
Сроки: 1-3 дня

Для заказа карточек нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_infographic())
async def insta_but(message:types.Message):
    with open("bot_name\Photos_Foulder\Insta_generally_info.jpg","rb") as photo_info:
        await message.answer_photo(photo=photo_info)
        await message.answer(text="""*📍Создам продающий дизайн для Вашего Instagram, который будет выделяться среди Ваших конкурентов

Базовое оформление:

1. Анализ конкурентов
2. Подбор палитры и шрифтов
3. Отбор фото
4. Дизайн ленты на 12 постов
5. До 6 обложек актуального    
6. Дизайн аватара

Цена: от 3499 рублей
Сроки: 1-3 дня 

Для заказа нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_instagram())
async def vk_but(message:types.Message):
    media_gr=[InputMediaPhoto(open(photo_path,"rb")) for photo_path in photos_read]
    await message.answer_media_group(media=media_gr)
    await message.answer("""*📍Создам продающий дизайн для Вашей группы ВКонтакте , который будет выделяться среди Ваших конкурентов

Базовое оформление:

1. Обложка сообщества (ПК версия) 
2. Обложка сообщества (мобильная версия) 
3. Аватарка
4. Кнопки меню (до 6 штук)
5. Услуги (до 6 штук)

Цена: от 2999 рублей 
Сроки: 1-3 дня

Для заказа  нажмите кнопку "Написать", и мы обсудим Ваш проект!*""",parse_mode="Markdown",reply_markup=keyboard_vkontakte())
async def cr_but(message:types.Message):
    with open("bot_name\Photos_Foulder\Creatives-min.png","rb") as photo_cr:
        await message.answer_photo(photo=photo_cr)
        await message.answer("""*📍Создам продающий дизайн для Вашего креатива, который будет выделяться среди Ваших конкурентов

Чек-листы 
Прайсы 
Презентации
Сертификаты 
Визитки 
Рекламные макеты 

Цена: от 1499 рублей
Сроки: 1-3 дня 

Для заказа нажмите кнопку "Написать", и мы обсудим Ваш проект!* """,parse_mode="Markdown",reply_markup=keyboard_creatives())
        
async def proccess_cmd(callback:types.CallbackQuery):
        
        if callback.data=="infogr":
            with open ("bot_name\Photos_Foulder\InforGraphics_extra_info.png","rb") as photo_infogr:
                await callback.message.answer_photo(photo=photo_infogr)
        elif callback.data=="inst":
            with open("bot_name\Photos_Foulder\Insta_extra_info.jpg","rb") as photo_inst:
                await callback.message.answer_photo(photo=photo_inst)
        elif callback.data=="vk":
            with open("bot_name\Photos_Foulder\Vk_extra_info.png","rb") as photo_vk:
                await callback.message.answer_photo(photo=photo_vk)       
        

async def cmd_check(message:types.Message):
    
          await message.reply("Пожалуйста, пользуйтесь только встроенными кнопками!!!")
                     
                 
    