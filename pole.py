import discord
from database import savePole,saveSubpole,saveFail,getRanking

pole_ready = False
subpole_ready = False
fail_ready = False

pole_maker = None
subpole_maker = None
fail_maker = None


def resetpole():
    global pole_maker,subpole_maker,fail_maker
    global pole_ready,subpole_ready,fail_ready
    
    pole_ready = True
    subpole_ready = True
    fail_ready = True

    pole_maker = None
    subpole_maker = None
    fail_maker = None


async def pole(ctx):
    global pole_ready
    global pole_maker
    if not pole_ready:
        await ctx.channel.send("La pole ya ha sido realizada por <@{0}>".format(pole_maker))
        return
    elif subpole_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho la subpole!".format(subpole_maker))
        return
    elif fail_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho el fail!".format(fail_maker))
        return
    else:
        pole_ready = False
        pole_maker = ctx.message.author.id
        savePole(ctx.message.author.id)
        await ctx.channel.send("<@{0}> ha hecho la pole!".format(ctx.message.author.id))
        return

async def subpole(ctx):
    global subpole_ready
    global subpole_maker
    if not subpole_ready:
        await ctx.channel.send("La subpole ya ha sido realizada por <@{0}>".format(subpole_maker))
        return
    elif pole_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho la pole!".format(ctx.message.author.id))
        return
    elif fail_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho el fail!".format(ctx.message.author.id))
        return
    else:
        subpole_ready = False
        subpole_maker = ctx.message.author.id
        saveSubpole(ctx.message.author.id)
        await ctx.channel.send("<@{0}> ha hecho la subpole!".format(ctx.message.author.id))
        return

async def fail(ctx):
    global fail_ready
    global fail_maker
    if not fail_ready:
        await ctx.channel.send("El fail ya ha sido realizado por <@{0}>".format(fail_maker))
        return
    elif pole_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho la pole!".format(ctx.message.author.id))
        return
    elif subpole_maker == ctx.message.author.id:
        await ctx.channel.send("<@{0}> ya has hecho la subpole!".format(ctx.message.author.id))
        return
    else:
        fail_ready = False
        fail_maker = ctx.message.author.id
        saveFail(ctx.message.author.id)
        await ctx.channel.send("<@{0}> ha hecho el fail!".format(ctx.message.author.id))
        return

async def ranking(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        description = """:checkered_flag: :top: **RANKING GLOBAL** :top: :checkered_flag:
----------------------------------------
:one: <@{0[0][0][0]}> => {0[0][0][1]}
:two: <@{0[0][1][0]}> => {0[0][1][1]}
:three: <@{0[0][2][0]}> => {0[0][2][1]}

:checkered_flag: :top: **POLE** :top: :checkered_flag:
----------------------------------------
<@{0[1][0][0]}> => {0[1][0][1]}
<@{0[1][1][0]}> => {0[1][1][1]}
<@{0[1][2][0]}> => {0[0][2][1]}

:checkered_flag: :two: **SUBPOLE** :two: :checkered_flag:
----------------------------------------
<@{0[2][0][0]}> => {0[2][0][1]}
<@{0[2][1][0]}> => {0[2][1][1]}
<@{0[2][2][0]}> => {0[2][2][1]}

:checkered_flag: :three: **BRONCE** :three: :checkered_flag:
----------------------------------------
<@{0[3][0][0]}> => {0[3][0][1]}
<@{0[3][1][0]}> => {0[3][1][1]}
<@{0[3][2][0]}> => {0[3][2][1]}""".format(getRanking()))
    await ctx.channel.send(embed=embed)