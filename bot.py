from urllib import request
import discord, requests, json, asyncio

client = discord.Client() #build connection to discord
token = #

def get_question():
    q = ''
    id = 1
    a = 0

    response = requests.get("https://protected-scrubland-69243.herokuapp.com/api/random")
    json_data = json.loads(response.text)
    q += json_data[0]['title'] + "\n"

    for x in json_data[0]['answer']:
        q += str(id) + ". " + x['answer'] + "\n"

        if x['is_correct'] == True:
            a = id

        id += 1

    return(q,a)

@client.event
async def on_message(message):
    if message.author == client.user:
        return #ignore messages from self (bot)

    if message.content.startswith('$q'):
        qs, ans = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()
        
        try:
            guess = await client.wait_for('message', check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Time\'s up!')

        if int(guess.content) == ans:
            await message.channel.send('Correct!')
        else:
            await message.channel.send('Wrong!')

client.run(token)
