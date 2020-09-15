import discord

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

client=discord.Client()
bot = commands.Bot(command_prefix="!", description = "Veille sur les poulets")





@bot.event
async def on_ready():
    print("Le bot est connecté!")
    #await bot.change_presence(activity=discord.Game(name="Surveiller la pepito team ❤️"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="la pepito team ❤️"))


@bot.event
async def on_member_join (member):
    modo = discord.utils.get(member.guild.roles, id=idmodo)
    admin = discord.utils.get(member.guild.roles, id=idadmin)
    channelwelcome=discord.utils.get(member.guild.channels, name ="join-member")
    await channelwelcome.send(f"🔥 Coucou {member.mention} 🔥")
    embed=discord.Embed(title="Bienvenue 😉",description=f"Bienvenue à toi {member.mention} ! \n \n❤️ Tu es le {len(list(member.guild.members))}ème membre du serveur ❤️ \n\n\n Si tu as des questions, n'hésite pas à en parler au staff en taguant {admin.mention} ou {modo.mention} 😉",color=0xFF8B00)
    embed.set_thumbnail(url=member.avatar_url)
    await channelwelcome.send(embed=embed)
    

@bot.event
async def on_member_remove (member):
    channelwelcome=discord.utils.get(member.guild.channels, name ="leave-member")
    await channelwelcome.send(f"😭 Au revoir {member.mention} 😭")
    embed=discord.Embed(title="A bientôt je l'espère 😉",description=f"{member.mention} est parti du serveur  ! ",color=0xFF8B00)
    embed.set_thumbnail(url=member.avatar_url)
    await channelwelcome.send(embed=embed)


@bot.event
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted", permissions =discord.Permissions( send_messages= False, speak =False), reason ="Création du role pour mute")

    for channel in ctx.guild.channels :
        await channel.set_permissions(mutedRole,send_messages = False, speak=False)
    return mutedRole

@bot.event
async def getMutedRole(ctx):
    roles=ctx.guild.roles
    for role in roles :
        if role.name == "Muted":
            return role
    return await createMutedRole(ctx)


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if (message_id == 753579003834794074):
        guild_id=payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if (payload.emoji.name == "✅"):
            poussin_role = discord.utils.get(guild.roles, name='Poussin')

        member =discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        await member.add_roles(poussin_role)

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if (message_id == 753579003834794074):
        guild_id=payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if (payload.emoji.name == "✅"):
            poussin_role = discord.utils.get(guild.roles, name='Poussin')

        member =discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        await member.remove_roles(poussin_role)





#Commandes pour tout le monde


    
@bot.command()
async def coucou (ctx):
    print("coucou")
    embed=discord.Embed(title="Coucou !",description="Comment tu vas ?",color=0x00FFF7)
    embed.set_thumbnail(url=" https://images-eu.ssl-images-amazon.com/images/I/61hnmOG5cZL.png")
    await ctx.send(embed=embed)

@bot.command()
async def ping (ctx):
    print("ping")
    embed=discord.Embed(title="Ping !",description=f"Le ping du bot est de {round(bot.latency *1000)} ms.",color=0x00FFF7)
    embed.set_thumbnail(url="https://www.ookla.com/s/images/ookla/index/gauge-blue-1x.png")
    await ctx.send(embed=embed)
   
def isclement1():  
    def isClement(ctx):
        return ctx.message.author.id == id
    return commands.check(isClement)

def isalex1():
    def isAlex(ctx):
        return ctx.message.author.id == id
    return commands.check(isAlex)

@bot.command(pass_context = True , aliases=['Wejdene', 'alexfandewejdene','wejdene4ever','wejdenelabest'])
async def wejdene (ctx):
    print("wejdene commande")
    embed=discord.Embed(title=" ❤️ Wejdene la best ❤️ ",description= "Si vous allez voir cette chanteuse de talent cliquez sur le lien ci dessous : \n \n https://www.youtube.com/channel/UC5HKrNXapsQYLouta4w-7rg ",color=0xFF00D8)
    embed.set_thumbnail(url="https://static.cnews.fr/sites/default/files/styles/image_640_360/public/screenshot_2020-06-10_wejdene_wejdene_bk_photos_et_videos_instagram_5ee09cd84b191_0.jpg?itok=xtbj7Y8b")
    await ctx.send(embed=embed)



@bot.command()
async def commandes (ctx):
    modo = discord.utils.get(ctx.guild.roles, id=585472593906106378)
    admin = discord.utils.get(ctx.guild.roles, id=585473428061159424)
    print("listes de commandes demande")
    embed=discord.Embed(title="Vous pouvez utiliser ces différentes commandes : ",description= f"1. !coucou \n \n 2. !ping \n\n  3. ❤️ !wejdene ou !alexfandewejdene ou !wejdene4ever ou !wejdenelabest ❤️\n \n 4. !commandes \n \n 5. !invitation \n\n Si vous avez des suggestions de commandes n'hésitez pas à en parler au staff en taguant {admin.mention} ou {modo.mention} 😉 ",color=0xFF8B00)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")	
    await ctx.send(embed=embed)

'''
6. !motorsport X \n Avec X entier naturel (X∈ℕ) représentant le nombre de messages à envoyer par le biais de l'algorithme programmé en python sa mère la reine des tchoins. \n\n 7. !yeet Y \n Ici, Y est un nombre entier naturel (Y∈ℕ) et il représente le nombre d'itération d'envoi du message. 
'''

@bot.command()
async def invitation(ctx):
    print("Lien d'invitation pour le serveur 2")
    modo = discord.utils.get(ctx.guild.roles, id=585472593906106378)
    admin = discord.utils.get(ctx.guild.roles, id=585473428061159424)
    embed=discord.Embed(title="Lien d'invitation pour le serveur !",description=f"Vous pouvez inviter qui vous voulez avec ce lien! \n \nDonc n'hésitez pas à le partager 😉\n \n https://discord.gg/AGbsMrk \n\n Si vous avez des questions n'hésitez pas à en parler au staff en taguant {admin.mention} ou {modo.mention} !",color=0xFF8B00)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    await ctx.send(embed=embed)






#Commandes de modération







@bot.command()
@commands.has_any_role("Modo","Admin")
async def reglement(ctx):
    print("affiche le reglement")
    modo = discord.utils.get(ctx.guild.roles, id=585472593906106378)
    admin = discord.utils.get(ctx.guild.roles, id=585473428061159424)
    embed=discord.Embed(title="Voici le règlement du serveur, vous devez le respecter sous peine de sanctions !",description=f"\n1. En utilisant ce serveur Discord, vous vous conformez aux TOS Discord. \n\n 2. Respecter les autres. \n\n3. Ne pas insulter  :no_entry: \n \n \n \n \n :warning: Si vous avez des problèmes, vous pouvez tag {admin.mention} ou {modo.mention} ! :warning:",color=0xFF8B00)
    embed.set_footer(text=f"Après avoir lu le règlement, merci de cocher la case ✅")
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    await ctx.send(embed=embed)


@reglement.error
async def reglement_error(ctx, error):
    
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role("Modo","Admin")
async def setdelay(ctx,seconds:int):
    print("slowmode de ", seconds,  "secondes")
    
    embed=discord.Embed(title="Slowmode !",description=(f"Le slowmode à été configuré dans {ctx.channel.name} pour une durée de {seconds} secondes par {ctx.author.mention} !"),color=0xFF8B00)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    await ctx.channel.edit(slowmode_delay=seconds)
    channellogs = bot.get_channel(692030930793136188)
    await channellogs.send(embed=embed)
    await ctx.send(embed=embed)
    #await channel.send(embed=embed)

    



@setdelay.error
async def setdelay_error(ctx, error, *seconds):
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        print("pas assez d'arugments pour la fonction slowmode")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments à la fonction **slowmode** \n La fonction **slowmode** s'écrit par exemple sous la forme **!slowmode** **10** pour mettre un delay de 10 secondes.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)

      

@bot.command()
@commands.has_any_role("Modo","Admin")
async def mute(ctx, member : discord.Member):
    print("mut")
    mutedRole = await getMutedRole(ctx)
    embed=discord.Embed(title="**Mute**", description = "Un modérateur a frappé !",color=0xFF8B00)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    embed.add_field(name="Membre mute", value =member.mention, inline=False)
    embed.add_field(name="Modérateur", value =ctx.author.mention, inline=False)
    channellogs = bot.get_channel(692030930793136188)
    await channellogs.send(embed=embed)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole)


@mute.error
async def mute_error(ctx, error, *member):
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        print("pas assez d'arugments pour la fonction mute")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments à la fonction **mute** \n La fonction **mute** s'écrit par exemple sous la forme **!mute** **@username**.  \n \n De plus, vous ne pouvez pas mute une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)



@bot.command()
@commands.has_any_role("Modo","Admin")
async def unmute(ctx,member : discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    print(mutedRole)
    await member.remove_roles(mutedRole, reason=reason)
    embed=discord.Embed(title="**Unmute**", description = "Un modérateur a frappé !",color=0xFF8B00)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    embed.add_field(name="Membre unmute", value =member.mention, inline=False)
    embed.add_field(name="Modérateur", value =ctx.author.mention, inline=False)
    channellogs = bot.get_channel(692030930793136188)
    await channellogs.send(embed=embed)
    await ctx.send(embed=embed)



@unmute.error
async def unmute_error(ctx, error, *member):
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        print("pas assez d'arugments pour la fonction Unmute")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments à la fonction **Unmute** \n La fonction **mute** s'écrit par exemple sous la forme **!unmute** **@username**.  \n \n De plus, vous ne pouvez pas unmute une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role("Modo","Admin")
async def clear(ctx, nombre):
    if nombre == "all":
        await ctx.channel.purge(limit = 20000000 + 1)
    else :
        await ctx.channel.purge(limit = int(nombre) + 1)



@clear.error
async def clear_error(ctx, error, *nombre):
    
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        print("pas assez d'arugments pour la fonction clear")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments a la fonction **clear** \n La fonction **clear** s'écrit par exemple sous la forme **!clear** **10** pour supprimer 10 messages.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
        

    



@bot.command()
@commands.has_any_role("Modo","Admin")
async def kick (ctx, user :discord.User, *reason):
    #embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    reason= " ".join(reason)
    
    embed=discord.Embed(title="**Kick**", description = "Un modérateur a frappé !",color=0xFF8B00)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
    embed.add_field(name="Membre kick", value =user.name, inline=False)
    embed.add_field(name="Raison", value =reason, inline=False)
    embed.add_field(name="Modérateur", value =ctx.author.mention, inline=False)


    await ctx.guild.kick(user,reason=reason)  #Commande qui qui kick la personne
    channellogs = bot.get_channel(692030930793136188)
    await channellogs.send(embed=embed)
    await ctx.send(embed=embed)
    

@kick.error
async def kick_error(ctx, error,*reason):
    
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
    
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
        
    elif isinstance(error, commands.MissingRequiredArgument):
        print("pas assez d'arguments pour la fonction kick")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments a la fonction **kick** ! \n La fonction **kick** s'écrit sous la forme : **!kick** **@username** **raison** \n \n De plus, vous ne pouvez pas kick une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)



@bot.command()
@commands.has_any_role("Modo","Admin")
async def ban(ctx, user :discord.User, *reason):
    if len(reason)!=0:
        reason= " ".join(reason)
        embed=discord.Embed(title="**Ban**", description = "Un modérateur a frappé !",color=0xFF8B00)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        embed.add_field(name="Membre ban", value =user.name +"#"+user.discriminator, inline=False)
        embed.add_field(name="Raison", value =reason, inline=False)
        embed.add_field(name="Modérateur", value =ctx.author.mention, inline=False)
        await ctx.guild.ban(user,reason=reason)
        channellogs = bot.get_channel(692030930793136188)
        await channellogs.send(embed=embed)
        await ctx.send(embed=embed)
        
    else:
        print("pas assez d'arguments pour la fonction ban")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments a la fonction **ban** ! \n La fonction **ban** s'écrit sous la forme : **!ban** **@username** **raison** \n \n De plus, vous ne pouvez pas ban une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
        
    #await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
    
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments a la fonction **ban** ! \n La fonction **ban** s'écrit sous la forme : **!ban** **@username** **raison** \n \n De plus, vous ne pouvez pas ban une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
        




@bot.command()
@commands.has_any_role("Modo","Admin")
async def unban(ctx, *, user):
    print (user)
    
        
    userName, userId = user.split("#")
    bannedUsers=await ctx.guild.bans()
    if len(user)!=0 :
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator==userId:
                embed=discord.Embed(title="**Unban**", description = "Un modérateur a frappé !",color=0xFF8B00)
            
                embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.add_field(name="Membre unban", value =user, inline=False)
            
                embed.add_field(name="Modérateur", value =ctx.author.mention, inline=False)
                await ctx.send(embed=embed)
                channellogs = bot.get_channel(692030930793136188)
                await channellogs.send(embed=embed)
                await ctx.guild.unban(i.user)
                return
            
            await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans.")
            embed=discord.Embed(title="Unban !",description=(f"L'utilisateur {user} n'est pas dans la liste des bans."),color=0xFF8B00)
            embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
            channellogs = bot.get_channel(692030930793136188)
            await channellogs.send(embed=embed)
            await ctx.send(embed=embed)
    else :
        print("pas assez d'arguments pour la fonction unban")
        embed=discord.Embed(title="Erreur", description = "Il manque des arguments a la fonction **unban** ! \n La fonction **unban** s'écrit sous la forme : **!unban** **username#ID** \n \n De plus, vous ne pouvez pas unban une personne qui a un grade **supérieur** au votre.",color=0xFF8B00)
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)




@unban.error
async def unban_error(ctx, error):
    
    if isinstance(error, commands.CheckFailure):
        print("Il manque les permissions nécesssaires")
        embed=discord.Embed(title="Erreur", description = "Vous n'avez pas les permissions nécessaires pour effectuer cette commande",color=0xFF8B00)
    
        embed.set_thumbnail(url="https://discord.bots.gg/img/logo_transparent.png")
        await ctx.send(embed=embed)
        




bot.run("TOKEN")
