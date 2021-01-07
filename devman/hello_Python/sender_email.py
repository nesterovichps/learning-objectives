import smtplib


class SendMassage:
    def __init__(self, login_email, login_pass, sender_email, to_send_email, theame_email, text_massage,
                 send_self=False):
        self.mode_send_self = bool(send_self)
        self.login_email = login_email
        self.login_pass = login_pass
        self.sender_email = sender_email
        self.to_send_email = self.sender_email if self.mode_send_self else to_send_email
        self.theme_email = theame_email
        self.text_massage = text_massage

    def start_send_email(self):
        self.formatted_massage()
        self.send_email()

    def formatted_massage(self):
        self.format_massage = f'From: {self.sender_email}\n' \
                              f'To: {self.to_send_email}\n' \
                              f'Subject: {self.theme_email}\n' \
                              f'Content-Type: text/plain; charset="UTF-8";\n\n' \
                              f'{self.text_massage}'
        self.format_massage = self.format_massage.encode('UTF-8')

    def send_email(self):
        yandex_port = 'smtp.yandex.ru:465'
        server = smtplib.SMTP_SSL(yandex_port)
        print(server)
        server.login(self.login_email, self.login_pass)
        print(server.noop())
        if self.mode_send_self:
            print('send test email')
        try:
            server.sendmail(self.sender_email, self.to_send_email, self.format_massage)
            print('email sended')
        except:
            print('Error')
        server.quit()


# for connect to smtp server
login_email = 'serg.kurtsaev@yandex.ru'
login_pass = 'hhggksjsqvlfezsp'
# for send massage
sender_email = login_email
to_send_email = 'mazafaka2026@bk.ru'
theme_email = 'Приглос на курс'
text_massage = ''' Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

 %website% — это новая версия онлайн-курса по программированию.
 Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

 Как будет проходить ваше обучение на %website%?

 → Попрактикуешься на реальных кейсах.
 Задачи от тимлидов со стажем от 10 лет в программировании.
 → Будешь учиться без стресса и бессонных ночей.
 Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
 → Подготовишь крепкое резюме.
 Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

 Регистрируйся → %website%
 На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
web_site = 'dvmn.org'
my_name = 'Петр'
receiver_name = 'Сергей'
formatted_for_send_text_massage = text_massage.replace(
    '%my_name%', my_name).replace(
    '%friend_name%', receiver_name).replace(
    '%website%', web_site)
sender_email_massage = SendMassage(login_email, login_pass, sender_email, to_send_email, theme_email,
                                   formatted_for_send_text_massage)
sender_email_massage.start_send_email()
