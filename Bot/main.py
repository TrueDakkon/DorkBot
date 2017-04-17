#Import Modules#
#Import Modules#
import discord, asyncio, logging, json
#Joining Bot#
logging.basicConfig(level=logging.INFO)
client = discord.Client()
token = ''
prefix = ''
with open('./../Config/Options.json') as json_data:
    data = json.load(json_data)
    token = data['token']
    prefix = data['prefix']
    print(token)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)
    await client.change_presence(game=discord.Game(name='Testing...')) #Setting Game.

#Test Commands#
#@client.event
#async def on_message(message):
#    print(message)
#    if message.content.startswith('!test'):
#        counter = 0
#        tmp = await client.send_message(message.channel, 'Calculating messages...')
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
#
#        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('!sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')

#Commands#
@client.event
async def on_message(message):
    print(message)
    if message.content.startswith(prefix + 'b8'):
        await client.send_message(message.channel,"gr8 b8 m8. i rel8 str8 appreci8 nd congratul8. i r8 dis b8 an 8/8. plz no h8, i'm str8 ir8. cr8 more cant w8. we shood convers8 i wont ber8, my number is 8888888 ask for N8. no calls l8 or out of st8. if on a d8, ask K8 to loc8. even with a full pl8 i always hav time to communic8 so dont hesit8. dont forget to medit8 and particip8 and masturb8 to allevi8 ur ability to tabul8 the f8. we should meet up m8 and convers8 on how we can cre8 more gr8 b8, im sure everyone would appreci8 no h8. i dont mean to defl8 ur hopes, but itz hard to dict8 where the b8 will rel8 and we may end up with out being appreci8d, im sure u can rel8. we can cre8 b8 like alexander the gr8, stretch posts longer than the nile's str8s. well be the captains of b8 4chan our first m8s the growth r8 will spread to reddit and like reel est8 and be a flow r8 of gr8 b8 like a blind d8 well coll8 meet me upst8 where we can convers8 or ice sk8 or lose w8 infl8 our hot air baloons and fly tail g8. we cood land in kuw8, eat a soup pl8 followed by a dessert pl8 the payment r8 wont be too ir8 and hopefully our currency wont defl8. well head to the israeli-St8, taker over like herod the gr8 and b8 the jewish masses 8 million m8. we could interrel8 communism thought it's past it's maturity d8, a department of st8 volunteer st8. reduce the infant mortality r8, all in the name of making gr8 b8 m8.")

client.run(token)
