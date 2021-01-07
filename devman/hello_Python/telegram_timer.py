from pytimeparse import parse

import learning_tasks.devman.hello_Python.data.ptbot as ptbot


def my_timer(time, CHAT_ID, id_massage, all_time):
    if time == 0:
        bot.send_message(CHAT_ID, f'{render_progressbar(all_time, time)}')
        bot.send_message(CHAT_ID, 'Время вышло')


    else:
        bot.update_message(CHAT_ID, id_massage, f'Осталось {time} секунды\n'
                                                f'{render_progressbar(all_time, time)}')


def sey_hello(text):
    print('Привет! Ты написал мне:', text)


def reply(text, CHAT_ID):
    id_massage = bot.send_message(CHAT_ID, f'timer start {text} s')
    text = parse(text)
    bot.create_countdown(int(text), my_timer, CHAT_ID=CHAT_ID, id_massage=id_massage, all_time=int(text))


# # Progressbar

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


with open('data/api_telegram.txt') as file:
    TOKEN = file.readlines()[0].strip()
    print(TOKEN)

CHAT_ID = '351429530'  # подставьте свой ID
time_for_timer = 5
bot = ptbot.Bot(TOKEN)

bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
bot.reply_on_message(reply, CHAT_ID)

# print(parse('1.2 minutes'))  # Выведется 72


bot.run_bot()
