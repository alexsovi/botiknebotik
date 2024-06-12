import discord
import random
from discord_components import Button, ButtonStyle, DiscordComponents
client = discord.Client()

def readFile(fileName):
    file = open(fileName, "r", encoding="UTF-8")
    list = file.read().split("\n")
    file.close()
    return random.choice(list)

@client.event
async def on_ready():
    DiscordComponents(client)
    print("бот готов.")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Visual Studio Code - main.py"))

@client.event
async def on_message(mes):
    if mes.content.startswith("Привет") or mes.content.startswith("привет"):
        await mes.channel.send(readFile("hello.txt"))
    elif mes.content.startswith("Как дела") or mes.content.startswith("как дела"):
        await mes.channel.send(readFile("dela.txt"))
    elif mes.content.startswith("Что делаешь") or mes.content.startswith("что делаешь"):
        await mes.channel.send(readFile("do.txt"))
    elif mes.content.startswith("Во что играешь") or mes.content.startswith("во что играешь"):
        await mes.channel.send(readFile("play.txt"))
    elif mes.content.startswith("Как тебя зовут") or mes.content.startswith("как тебя зовут"):
        await mes.channel.send("Меня зовут Ботик который не Ботик")
    elif mes.content.startswith("Hello") or mes.content.startswith("Hi"):
        await mes.channel.send("Do you speak Russian? I can only speak Russian.")
    elif mes.content.startswith("чем помочь") or mes.content.startswith("Чем я могу помочь"):
        await mes.channel.send("Да ничем. Хотя... Подпишись на канал моего создателя: https://youtube.com/@alexsovi")
    elif mes.content.startswith("ты npc"):
        await mes.channel.send("A gun! Give me a freaking gun! WTH, i can't pick it up.", tts=True)
    elif mes.content.startswith("gjitk yf[eq"):
        await mes.channel.send("сам иди")
    elif mes.content.startswith("сус"):
        await mes.channel.send("ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ ТУЦ", tts=True)
    elif mes.content.startswith("ты Карл"):
        await mes.channel.send("Я не Карл! Я Ботик который не Ботик!")
    # elif mes.content.startswith("clear1"):
    #     await mes.channel.send(limit=2)
    elif mes.content.startswith("Кнб камень") or mes.content.startswith("кнб камень"):
        await mes.channel.send(readFile("kamen.txt"))
    elif mes.content.startswith("Кнб ножницы") or mes.content.startswith("кнб ножницы"):
        await mes.channel.send(readFile("nozh.txt"))
    elif mes.content.startswith("Кнб бумага") or mes.content.startswith("кнб бумага"):
        await mes.channel.send(readFile("bumaga.txt"))
    # elif mes.content.startswith("пива я лублу тебя"):
    #     await mes.channel.send("https://cdn.discordapp.com/attachments/1006067338258423899/1006842490231472229/pivoyalublutebu.mp4")
    # elif mes.content.startswith("Кахут"):
    #     await mes.author.send(
    #         embed=discord.Embed(title="Вопрос", description="Кто лучше?"),
    #         components=[
    #             Button(style=ButtonStyle.blue, label="Ты"),
    #             Button(style=ButtonStyle.blue, label="Mipper6"),
    #             Button(style=ButtonStyle.blue, label="Оба")
    #         ]
    #     )
    #     while True:
    #         r = await client.wait_for("button_click")
    #         if r.component.label == "Ты":
    #             await r.respond(content="https://tenor.com/view/harosh-memeblog-thomas-shelby-gif-21009538")
    #         elif r.component.label == "Mipper6":
    #             await r.respond(content="https://tenor.com/view/frog-kermit-muppets-idiot-stupid-gif-11872194")
    #         elif r.component.label == "Оба":
    #             await r.respond(content="https://tenor.com/view/%D1%83%D0%BB%D1%8C%D1%80%D1%82%D1%80%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D1%88-%D1%85%D0%B0%D1%80%D0%BE%D1%88-%D0%BC%D0%B5%D0%B3%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D1%88-gif-24070806")

client.run("токен вашего бота")
