import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

generated_prophecies = [(times[random.randrange(len(times))].title() + ' ' +
                         advices[random.randrange(len(advices))] + ' ' +
                         promises[random.randrange(len(promises))] + ' ' + '.') for _ in range(5)]

# всё что выше этого комментария вставьте на сайте в блок проверки

i = 0
print("Вот что получилось")
while i < 5:
    print(i + 1, generated_prophecies[i])
    i = i + 1
