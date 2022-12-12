from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 30:
            oyun[m.chat.id]["kec"] += 1
            await c.send_message(m.chat.id,f"➡️ Bir Sonrakı Sözə Keçid Edildi\n✅ Doğru Söz: **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund: {oyun[m.chat.id]['round']}/100
🌠 Tapılacaq Söz: <code>{kelime_list}</code>
📌 İpucu: {oyun[m.chat.id]["kelime"][0]}
🔗 Uzunluq: {int(len(kelime_list)/2)}
〽️ Qarışıq Tazılmış Bu hHərflərdən Əsas Sözü Tapmağa Çalış!
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçid saxlanıldı! </code> \n⛔ Oyunu dayandırmaq üçün /dayan Əmrindən İsdifədə Edin**")
    else:
        await m.reply(f"❗ **Qrupda Qktiv Oyun Yoxdur!\n♻️ Yeni Oyuna Başlamaq Üçün /oyna Əmrindən İsdifadə Edin**")
