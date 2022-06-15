



import aiohttp
import discord
from discord import  ui, app_commands
from discord.ext import commands
import json
import time
import interactions
from typing import Literal
import asyncio




TICKET_CATEGORY_NAME = "Active Tickets"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = '>', intents=intents)
from config import token


async def on_ready():
    await bot.change_presence(activity=discord.Game(name="a game"))


class client(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced= False

    async def on_ready(self):
        await self.wait_until_ready()
        
        
        if not self.synced:
            await tree.sync(guild = discord.Object(id = 811461860200022025))
            self.synced = True
        print(f"We have logged in as {self.user}.")
        

class my_modal(ui.Modal, title = "Example Modal"):
    answer = ui.TextInput(label = "Is it working?", style=discord.TextStyle.short, placeholder = "Your username with discriminator", default = "Vixen#1203", required= True, max_length = 10)
    answer_2 = ui.TextInput(label = "Who Made this?", style=discord.TextStyle.short, placeholder = "Put in your password ", default = "qwertycommon", required= True, max_length = 50)
    async def on_submit(self, interaction: discord.Interaction):
       
        embed = discord.Embed(title = self.title,
        description= f"**{self.answer.label}** \n {self.answer} \n \n **{self.answer_2.label}** \n {self.answer_2}")
        embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)


        await interaction.response.send_message(embed=embed)


class application_modal(ui.Modal, title = "Application"):
    question_1 = ui.TextInput(label = "What is your username with discriminator?", style=discord.TextStyle.short, placeholder = "Ex. Vixen#1203", required= True, max_length = 25)
    question_2 = ui.TextInput(label = "What postion are you applying for?", style=discord.TextStyle.short, placeholder = "Ex. Moderator", required= True, max_length = 20)
    question_3 = ui.TextInput(label = "Why are you interested in applying?", style=discord.TextStyle.long, placeholder = "State atleast one reason", required= True, max_length = 4000)
    question_4 = ui.TextInput(label = "What are your strengths and weaknesses", style=discord.TextStyle.short,  required= True, max_length = 4000)
    question_5 = ui.TextInput(label = "Why should we pick you above everyone else?", style=discord.TextStyle.short, required= True, max_length = 20)

    async def on_submit(self, interaction: discord.Interaction):
       
        embed = discord.Embed(title = self.title,
        description= f"**{self.question_1.label}** \n {self.question_1} \n \n **{self.question_2.label}** \n {self.question_2} \n \n **{self.question_3.label}** \n {self.question_3} \n \n **{self.question_4.label}** \n {self.question_4} \n \n **{self.question_5.label}** \n {self.question_5}",
        colour= discord.Color.blurple())
        embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)


        await interaction.response.send_message(embed=embed)
aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command( name = 'modal', description = "Testing the modals feature")
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(my_modal())

@tree.command( name = 'fruits', description='testing') 
async def slash2(interaction: discord.Interaction, fruits: Literal['apple', 'banana', 'cherry']):
    await interaction.response.send_message(f"You chose {fruits}!", ephemeral = True)

@tree.command( name = 'test', description = "A simple test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Hey the test worked!")

@tree.command( guild = discord.Object(id = 811461860200022025), name = 'create_channel', description = "Creates a test channel")
async def create_channel(interaction: discord.Interaction, channel_type: Literal['text', 'voice', 'stage'], name: str, topic:str, category: discord.CategoryChannel, slowmode:int):
    guild = interaction.guild
    if channel_type == "text":
        try:
            channel = await category.create_text_channel(f"{name}", topic=topic, slowmode_delay=slowmode)
            await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            time.sleep(10)
            await channel.delete()
        except Exception as e:
            await interaction.response.send_message(e)
        
    elif channel_type == "voice":
        try:
            channel = await category.create_voice_channel(f"{name}")
            await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            time.sleep(10)
            await channel.delete()
        except Exception as e:
            await interaction.response.send_message(e)
    else:
        try:
            
            channel = await category.create_stage_channel(topic=f"{topic}", name=f"{name}")
            await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            time.sleep(10)
            await channel.delete()
        except Exception as e:
            await interaction.response.send_message(e)

        

@tree.command(name = 'mention', description = "Mentions the desired user")
async def mention(interaction: discord.Interaction , user_to_mention: discord.User):
    await interaction.response.send_message(f"{user_to_mention.mention} mentioned by {interaction.user.mention}")    

@tree.command( name = 'ticket', description = "Creates a support ticket")
async def ticket(interaction: discord.Interaction, reason :str):
    guild = interaction.guild
    """options = [interaction.Option(
                    name="Reason",
                    description="Reason for ticket creation",
                    type=interaction.OptionType.STRING,
                    required=True,
                )]
                """
    # ticket_category = 982138241371226122
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.user: discord.PermissionOverwrite(view_channel=True),
        guild.me: discord.PermissionOverwrite(view_channel=True)
        
    }
    
    
    channel_ticket = await guild.create_text_channel(f"{interaction.user}", overwrites=overwrites)
    em_1 = discord.Embed(
        title = f"Help needed by {interaction.user}",
        description= f"Please wait for the staff team to get back to you. They created the ticket with reason : **{reason}**"
    )
    em_1.set_thumbnail(url=interaction.user.avatar)
    em_1.set_author(name = interaction.user, icon_url= interaction.user.avatar)
    await channel_ticket.send(embed=em_1)
    await interaction.response.send_message(f"Created your ticket channnel {channel_ticket.mention}" , )

@tree.command( name = 'eval', description = "evaluate a piece of code")

async def eval(interaction: discord.Interaction):
    
    await interaction.response.send_message("Evaluated your code")


@tree.command( name = 'application', description = "Staff application")

async def eval(interaction: discord.Interaction):
    
    channel = bot.get_channel(984434566204915742)

    
    await interaction.response.send_modal(application_modal())


@tree.command(name = 'warn', description = "Warns the member who runs the command | Currently in test phase")    
async def warn(interaction: discord.Interaction):
    
    await interaction.response.send_message(f"Warning you {interaction.user.mention}")
    """
    time.sleep(5)
    await interaction.response.edit(content="You have been warned in the dms")
    """
    await interaction.user.send("You have been warned for using this slash command")

@tree.command(
    guild = discord.Object(id = 811461860200022025), name = 'test_2', description = "Command application test")
    
async def test_2(interaction:discord.Interaction):
    await interaction.response.send_message(f"You have applied a command onto user {interaction.user.mention}!")

@tree.command(
    name = 'apply', description = "How to apply")

async def apply(interaction:discord.Interaction):
    emb_apply = discord.Embed (
        title= "How to apply?",
        description= "Simple! \n Just run `/application` to get started on your application! ",
        colour= discord.Color.blurple())
    

    await interaction.response.send_message(embed=emb_apply)


@tree.command(
    guild = discord.Object(id = 811461860200022025), name = 'nightmare', description = "Pings nightmare. DON'T USE IN ANY CASE UNLESS YOU WANT TO BE BANNED!")
async def nightmare(interaction: discord.Interaction):
   await interaction.response.send_message("Sorry but !<@696292497848008704>")

@tree.command(
     name = 'cat', description = "Cute cat images")
@app_commands.checks.cooldown(1,5, key=lambda i: (i.user.id))

async def cat(interaction: discord.Interaction):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as response:
            raw = await response.text()
            cat= json.loads(raw)[0]
            emb_cat = discord.Embed(
                title = "Cat",
                color = discord.Color.green()
            )
            emb_cat.set_image(url = cat['url'])
            await interaction.followup.send(embed=emb_cat)
    
@tree.command(
     name = 'dog', description = "Cute dog images")
async def dog(interaction: discord.Interaction):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            raw = await response.text()
            dog= json.loads(raw)
            emb_dog = discord.Embed(
                title = "Dog",
                color = discord.Color.green()
            )
            emb_dog.set_image(url = dog['message'])
            await interaction.followup.send(embed=emb_dog)

@tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        em_error = discord.Embed(
            title = "Cooldown",
            description= "Give the command some rest fam"
        )
        await interaction.response.send_message(embed=em_error, ephemeral=True)
    else: raise error

@tree.command(
    guild = discord.Object(id = 811461860200022025), name = 'slowmode', description = "Set the slowmode")
async def slowmode(interaction:discord.Interaction, channel: discord.TextChannel, slowmode:int):
    
    await channel.edit(slowmode_delay=slowmode)
    if slowmode == 0:
        await interaction.response.send_message(f"Disabled slowmode")
    else:
        await interaction.response.send_message(f"Set the slowmode to {slowmode} seconds!")
    
@tree.command(guild = discord.Object(id = 811461860200022025), name = 'help', description = "Gets help about various commands")
async def help(interaction:discord.Interaction):
    emb_help = discord.Embed(
        title= "Help has arrived",
        description= "Let me walk you through the commands: \n **This bot does not have any prefix. It responds to slash (`/`) commands.** \n \n `/create_channel`: This command is self-explanatory. It helps you create the channel of your wish \n \n `/slowmode`: This command sets the slowmode of the channel",
        colour= discord.Color.blurple())
    await interaction.response.send_message(embed=emb_help)   
        
aclient.run(token)


