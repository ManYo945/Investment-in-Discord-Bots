from discord.ext import tasks
import discord
import subprocess
import datetime

class MyClient(discord.Client): 
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('----------------------------------------------')
        # self.my_background_task.start()

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('test'):
            await message.reply('test你媽啦，閉嘴!', mention_author=False)


        if message.content.startswith('周任保是誰'):
            await message.reply('我主人', mention_author=False)
        elif message.content.startswith('周任保'):
            await message.reply('請不要直稱我主人的名諱', mention_author=False)

        if message.content.startswith('李至恩'):
            await message.reply('他我主人的肉便器', mention_author=False)

        if message.content.startswith('jpy'):
            result = subprocess.run(['python', 'get_jpy_dawho.py'], capture_output=True, text=True)
            await message.reply(result.stdout, mention_author=False)
            result = subprocess.run(['python', 'N225&JPYTWD.py'], capture_output=True, text=True)
            with open('N225&JPYTWD.png', 'rb') as f:
                file = discord.File(f)
            # 發送一條消息，包含圖片
            await message.channel.send('Here is an image: N225&JPYTWD_INDEX', file=file)
            await message.reply(result.stdout, mention_author=False)
            #await message.reply('https://bank.sinopac.com/MMA8/bank/html/rate/bank_ExchangeRate.html', mention_author=False)

        
    
    # @tasks.loop(seconds=10.0)
    # async def my_background_task(self):
    #     now = datetime.datetime.now()
    #     await self.get_channel(1117367023375220767).send(f'現在時間是 {now.strftime("%Y-%m-%d %H:%M:%S")}')
    

intents = discord.Intents.default()
intents.message_content = True 

client = MyClient(intents=intents)
client.run('MTExNzMxMTkyNzQ5MjgyNTIxOA.GP2igj.jwYIKNZi1f-0XF86b03LwpgV-L8R26gVhjDZwA')
