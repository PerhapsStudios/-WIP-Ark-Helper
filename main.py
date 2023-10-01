import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

@bot.event
async def on_ready():
  print("ready to perform actions!")

@bot.command()
async def ark(ctx):
  embed = discord.Embed(title="Ark helper", description="Youtube channel: [click here to redirect](https://www.youtube.com/watch?time_continue=1&v=F3h62L3pnMY&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=MjM4NTE&feature=emb_title)", color=discord.Color.green())
  
  embed.set_thumbnail(url="https://i.ytimg.com/vi/IZ2UTC0BNpE/maxresdefault.jpg")
  embed.add_field(name="Beginner guide", value="This is a beginner guide to start your Ark adventure", inline=True)

@bot.command()
async def wiki(ctx):
  embed = discord.Embed(title="Ark helper", description="Wiki: [click here to redirect](https://ark.fandom.com/wiki/Fjordur)", color=discord.Color.green())
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/53/Fjordur_DLC.jpg/revision/latest?cb=20220905121625")
  embed.add_field(name="Fjordur Wiki", value="The complete Fjordur wiki", inline=True)


@bot.command()
async def dino(ctx):
 embed = discord.Embed(title="Dino helper", description="Youtube channel: [click here to redirect](https://www.youtube.com/watch?v=F3h62L3pnMY&list=PL6F3E2B91003E3B4E)", color=discord.Color.green())
 embed.set_thumbnail(url="https://i.ytimg.com/vi/F3h62L3pnMY/maxresdefault.jpg")
 embed.add_field(name="Dino guide", value="This is a guide to help you understand dinos in Ark", inline=True)

@bot.command()
async def caves(ctx):
 embed = discord.Embed(title="Cave helper", description="Youtube channel: [click here to redirect](https://www.youtube.com/watch?v=F3h62L3pnMY&list=PL6F3E2B91003E3B4E)", color=discord.Color.green())
 embed.set_thumbnail(url="https://i.ytimg.com/vi/F3h62L3pnMY/maxresdefault.jpg")
 embed.add_field(name="Cave guide", value="This is a guide to help you understand caves in Ark", inline=True)

@bot.command()
async def mods(ctx):
 embed = discord.Embed(title="Mod helper", description="Youtube channel: [click here to redirect](https://www.youtube.com/watch?v=F3h62L3pnMY&list=PL6F3E2B91003E3B4E)", color=discord.Color.green())
 embed.set_thumbnail(url="https://i.ytimg.com/vi/F3h62L3pnMY/maxresdefault.jpg")
 embed.add_field(name="Mod guide", value="This is a guide to help you understand mods in Ark", inline=True)

@bot.command()
async def tips(ctx):
 embed = discord.Embed(title="Tips helper", description
  
  await ctx.channel.send(embed=embed)
  

bot.run("")
