import discord, random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
sayilar = {}
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith('$tahmin'):
        sayilar[message.author.id] = random.randint(1, 10)
        await message.channel.send('1-10 arası bir sayı tuttum! Tahmin et:')
    elif message.content.isdigit() and message.author.id in sayilar:
        tahmin = int(message.content)
        if tahmin == sayilar[message.author.id]:
            await message.channel.send('🎉 Doğru tahmin!')
            del sayilar[message.author.id]
        else:
            await message.channel.send('⬆️ Daha büyük bir sayı!' if tahmin < sayilar[message.author.id] else '⬇️ Daha küçük bir sayı!')
client.run("YOUR_TOKEN")
