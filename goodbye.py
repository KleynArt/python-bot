#!/usr/bin/env python
import telebot

TOKEN = '2104145924:AAG1RBSZ_jWKSXTh_MkMZj0sRCPjNMCRsKs'

bot = telebot.TeleBot(TOKEN)
bot.config['api_key'] = TOKEN

bot.send_message('-1001274379258', 'El servidor se ha cerrado! \xF0\x9F\x98\x95')
