



import aiohttp
import discord
from discord import  ui, app_commands

import json
import time

from typing import Literal
import asyncio
from datetime import datetime

 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)

TICKET_CATEGORY_NAME = "📨 | ==== Support ==== | 📨"



intents = discord.Intents.default()
intents.members = True
intents.message_content = True


from config import token



    

class client(discord.Client):
    def __init__(self):
        super().__init__(intents = intents)
        self.synced= False
        self.added= False
        self.role = 986515497669525544

    async def on_member_remove(self, member):
        bye_bye_embed = discord.Embed(
        title="Sorry to see you go!",
        description= f"<:memberleave:986552554177593364> Sad to see you go {member.mention}. However if you feel like coming back we will always be waiting for you. \n \n Rejoin using [this link](https://discord.gg/F2tkagb7Br) ",
        color= discord.Color.red()   )
        bye_bye_embed.set_author(name = f"{member.name}", icon_url= member.avatar)
        await member.send(f"Goodbye {member.mention}", embed=bye_bye_embed)
    
    async def on_guild_join(self, guild):
        true_guild = aclient.get_guild(811461860200022025)
        true_member_count = len([m for m in guild.members if not m.bot])
        added_embed= discord.Embed(
            title = "Bot has been added to another guild",
            description = f"**Guild name**: `{guild.name}` \n **Membercount**: `{true_member_count}`"
        )
        guild_channel = discord.utils.get(true_guild.text_channels, name = '➕・guild-added')

        await guild_channel.send(embed=added_embed)
       
    async def on_member_join(self, member):
        welcome_embed = discord.Embed(
        title="Welcome!",
        description= f"<:memberadd:986552556476059739> Welcome the server {member.mention} \n Make sure to check out <#938830951545458698> and <#986515513658196010> \n \n Visit <#986515517957365810>, <#986515519010131988> or <#986515520780107786> to keep up with the bot's latest update" ,
        color= discord.Color.green()   )
        welcome_embed.set_author(name = f"{member.name}", icon_url= member.avatar)
        await member.send(f"Welcome to the server {member.mention}", embed=welcome_embed)

    async def on_ready(self):
        await self.wait_until_ready()
        
        global TICKET_CATEGORY_NAME
        guild = aclient.get_guild(811461860200022025)

        uptime_channel = discord.utils.get(guild.text_channels, name='📡・bot-status')

        uptime_embed = discord.Embed(
            title = "Bot is online",
            description= f" <:link:986552561052024882> Successfully logged in as {self.user}. \n \n Responding to commands",
            color=discord.Color.green()
        )
        uptime_embed.set_footer(text= current_time)


        await uptime_channel.send(embed=uptime_embed)
        
        #TICKET_CATEGORY_NAME = discord.utils.get(interaction.guild.categories, name=TICKET_CATEGORY_NAME)
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
            self.add_view(button_view())
            self.added = True
        print(f"We have logged in as {self.user}.")


class ticket_button(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Close", style = discord.ButtonStyle.red, custom_id="close", emoji="<:delete:986581594192109648>")
    async def close(self, interaction:discord.Interaction, button: discord.ui.Button):
        close_check = discord.Embed(
        description="Are you sure you want to close this ticket?",
        color = discord.Color.red())
        await interaction.channel.send(embed=close_check, view= confirm_delete())

class button_view(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Accept", style = discord.ButtonStyle.green, custom_id="accept")
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        accepted = discord.Embed(
            title="Your Application has been accepted!",
            description= "Your application has been accepted by the server admins. \n \n We warmly welcome you to our staff team and look forward to working together!",
            color= discord.Color.green()
        )
        if type(aclient.role) is not discord.Role:
            aclient.role = interaction.guild.get_role(986515497669525544)
        
        if aclient.role not in applicant.roles:
            await applicant.add_roles(aclient.role)
            await interaction.response.send_message(f"Successfully accepted the user as {aclient.role.mention}!", ephemeral=True)
            await applicant.send(embed=accepted)
        else:
            await interaction.response.send_message(f"Can't accept an existing staff!", ephemeral=True)
        
        for child in self.children:
            child.disabled=True
        await button.response.edit_message(view=self)

    @discord.ui.button(label="Deny", style= discord.ButtonStyle.red , custom_id="deny")
    async def deny(self, button:discord.ui.Button, interaction:discord.Interaction):
        denied = discord.Embed(
            title = "Your application has been denied",
            description="Your application has been reviewed by our server admins but unfortunately we had to deny your application",
            color = discord.Color.red()
            )
        await interaction.response.send_message("Successfully denied user")
        await applicant.send(embed=denied)
        for child in self.children:
            child.disabled=True
        await button.response.edit_message(view=self)
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
        guild = interaction.guild
        channel = discord.utils.get(guild.text_channels, name='🔧・applications')

        log_channel = discord.utils.get(guild.text_channels, name='📛・moderation-logs')
        log_embed = discord.Embed(
        title= "Member Applied for staff",
        description= f"**Applicant**: {interaction.user.mention} \n **Application can be found in** : <#986941550166683659> ",
        color = discord.Color.greyple())
        #log_embed.set_thumbnail(url=applicant.avatar_url)
        
        embed = discord.Embed(title = self.title,
        description= f"**{self.question_1.label}** \n {self.question_1} \n \n **{self.question_2.label}** \n {self.question_2} \n \n **{self.question_3.label}** \n {self.question_3} \n \n **{self.question_4.label}** \n {self.question_4} \n \n **{self.question_5.label}** \n {self.question_5}",
        colour= discord.Color.blurple())
        embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)

        await interaction.response.send_message("Your application has been submitted. We will review it an let you know soon")
        await log_channel.send(embed=log_embed)
        await channel.send(embed=embed, view=button_view())
aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command( name = 'remarks', description = "What do you think about the bot?")
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(my_modal())



@tree.command(name = "set_ticket_category", description= "Sets the ticket category for your guild")
async def set_ticket_category(interaction:discord.Interaction, category: discord.CategoryChannel):
    global TICKET_CATEGORY_NAME
    TICKET_CATEGORY_NAME = category
    await interaction.response.send_message(f"Successfully set your ticket category as {category.mention}")
    

@tree.command( name = 'create_channel', description = "Creates a test channel")
async def create_channel(interaction: discord.Interaction, channel_type: Literal['text', 'voice', 'stage'], name: str, topic:str = None, category: discord.CategoryChannel = None, slowmode:int = None, delete_after:int = None):
    guild = interaction.guild
    if channel_type == "text":
        try:
            if category is not None:
                channel = await category.create_text_channel(f"{name}", topic=topic, slowmode_delay=slowmode)
                await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            else: 
                channel = await guild.create_text_channel(f"{name}", topic=topic, slowmode_delay=slowmode)
                await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            if delete_after is not None:
                time.sleep(delete_after)
                await channel.delete()
        except Exception as e:
            await interaction.response.send_message(e)
        
    elif channel_type == "voice":
        
        try:
            if category is not None:
                channel = await category.create_voice_channel(f"{name}")
                await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            else:
                channel = await guild.create_voice_channel(f"{name}")
                await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
            if delete_after is not None:
                time.sleep(delete_after)
                await channel.delete()
        except Exception as e:
            await interaction.response.send_message(e)
    else:
        
        try:
            if category is not None:
                if topic is not None:
                    channel = await category.create_stage_channel(topic=f"{topic}", name=f"{name}")
                    await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
                else:
                    await interaction.response.send_message(f"Creating Stage channel requires a topic. Flag topic is necessary")
            else:
                if topic is not None:
                    channel = await category.create_stage_channel(topic=f"{topic}", name=f"{name}")
                    await interaction.response.send_message(f"It worked. Channel has been created with name {channel.mention}")
                else:
                    await interaction.response.send_message(f"Creating Stage channel requires a topic. Flag topic is necessary")
                
                
            if delete_after is not None:
                time.sleep(delete_after)
                await channel.delete()
        except Exception as e:
            print(e)

        

@tree.command( guild = discord.Object(id = 811461860200022025),name = 'mention', description = "Mentions the desired user")
async def mention(interaction: discord.Interaction , user_to_mention: discord.User):
    await interaction.response.send_message(f"{user_to_mention.mention} mentioned by {interaction.user.mention}")    

class confirm_delete(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Yes", style = discord.ButtonStyle.green, custom_id="yes")
    async def confirm(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.channel.delete()

    @discord.ui.button(label="No", style = discord.ButtonStyle.red, custom_id="no")
    async def no(self, interaction:discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()
      
 @tree.command(name = "setticketcategory, description = "sets ticket category"):
               async def ticket_category(interaction: discord.Interaction, category = discord.Category):
                TICKET_CATEGORY_NAME = category
                return TICKET_CATEGORY_NAME
@tree.command(name = 'ticket', description = "Creates a support ticket")
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
    if TICKET_CATEGORY_NAME is not None:
        ticket_category = discord.utils.get(interaction.guild.categories, name=TICKET_CATEGORY_NAME)
    #elif type(TICKET_CATEGORY_NAME) is None:
        #channel_ticket = await guild.create_text_channel(name= f"ticket-{interaction.user}", topic = interaction.user.id)
    else:
        ticket_category = interaction.channel.category

    
    
    em_1 = discord.Embed(
        title = f"Help needed by {interaction.user}",
        description= f"Please wait for the staff team to get back to you. They created the ticket with reason : **{reason}**"
    )
    em_1.set_thumbnail(url=interaction.user.avatar)
    em_1.set_author(name = interaction.user, icon_url= interaction.user.avatar)
    await channel_ticket.send(f"{interaction.user.mention} | <@&986515497669525544>", embed=em_1, view=ticket_button())
    await interaction.response.send_message(f"<a:loading:986581366563016744> Creating your ticket..")
    channel_ticket = await ticket_category.create_text_channel(f"ticket-{interaction.user}",  topic = interaction.user.id, overwrites=overwrites)
    await interaction.edit_original_message(content = f"Created your ticket channnel {channel_ticket.mention}" )
    
    
"""
@tree.command( name = 'eval', description = "evaluate a piece of code")

async def eval(interaction: discord.Interaction):
    
    await interaction.response.send_message("Evaluated your code")

"""
@tree.command( name = 'application', description = "Staff application")

async def application(interaction: discord.Interaction):
    guild = interaction.guild
    

    global applicant
    #channel = aclient.get_channel(984434566204915742)
    applicant = interaction.user

    await interaction.response.send_modal(application_modal())


@tree.command( name = 'warn', description = "Warns the member who runs the command | Currently in test phase")    
async def warn(interaction: discord.Interaction, member: discord.Member, reason: str):
    guild = interaction.guild
    log_channel = discord.utils.get(guild.text_channels, name='📛・moderation-logs') 
    
    warn_embed = discord.Embed(
        title= "You have been warned!",
        description = f"You got warned in **{guild}** because: **{reason}**",
        color= discord.Color.red()
    )
    log_embed = discord.Embed(
        title= "Member warned",
        description= f"**Warned Member**: {member.mention} \n **Moderator**: {interaction.user.mention} \n **Reason**: {reason} ",
        color = discord.Color.greyple())
    #log_embed.set_thumbnail(url = member.avatar_url)

    
    await log_channel.send(embed=log_embed)
    await member.send(embed=warn_embed)
    await interaction.response.send_message(f"Successfully warned {member.mention}")
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

"""
@client.event
async def on_member_join(member):
    

"""

@tree.command(guild = discord.Object(id = 811461860200022025), name = 'invite', description = "Checks invite count")

async def invites(interaction: discord.Interaction, user: discord.Member=None):
    if user == None:
       check_user = interaction.author
    else:
       check_user = user
    total_invites = 0
    for i in await interaction.guild.invites():
        if i.inviter == check_user:
            total_invites += i.uses
    await interaction.response.send_message(f"{check_user.name} has invited {total_invites} member{'' if total_invites == 1 else 's'}!")
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
     name = 'slowmode', description = "Set the slowmode")
async def slowmode(interaction:discord.Interaction, channel: discord.TextChannel, slowmode:int):
    slow_embed = discord.Embed(
        title="Setting Slowmode",
        description=f"<:slowmode:986583183212556308> Successfully set the slowmode to {slowmode} seconds! "
    )
    await channel.edit(slowmode_delay=slowmode)
    if slowmode == 0:
        slow_disable = discord.Embed(
            title = "Disabling Slowmode",
            description= f"<:off1:986583210672680981> Successfully disabled slowmode")
        await interaction.response.send_message(embed=slow_disable)
    else:
        slow_embed = discord.Embed(
        title="Setting Slowmode",
        description=f"<:slowmode:986583183212556308> Successfully set the slowmode to {slowmode} seconds! "
    )
        await interaction.response.send_message(embed=slow_embed)
    
@tree.command( name = 'help', description = "Gets help about various commands| Still being updated")
async def help(interaction:discord.Interaction):
    emb_help = discord.Embed(
        title= "Help has arrived",
        description= "Let me walk you through the commands: \n **This bot does not have any prefix. It responds to slash (`/`) commands.** \n \n `/create_channel`: This command is self-explanatory. It helps you create the channel of your wish \n \n `/slowmode`: This command sets the slowmode of the channel",
        colour= discord.Color.blurple())
    await interaction.response.send_message(embed=emb_help)   
        
aclient.run(token)


