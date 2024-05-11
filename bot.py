import discord
import random
from discord.ext import commands
from discord.ui import View
from discord.ui import Button

intents = discord.Intents().all()
client = commands.Bot(command_prefix="d!", intents=intents)

@client.event
async def on_ready():
    print("Work!")


client.remove_command("help")





@client.command()
async def uyarı(ctx,member:discord.Member, uyarı,*,args):
    guild = ctx.guild
    uyarı_1 = discord.utils.get(guild.roles, name="Uyarı ~ 1")
    uyarı_2 = discord.utils.get(guild.roles, name="Uyarı ~ 2")
    uyarı_3 = discord.utils.get(guild.roles, name="Uyarı ~ 3")

    if uyarı == "1":
        uyarı_numb = "1"

    if uyarı == "2":
        uyarı_numb = "2"

    if uyarı == "3":
        uyarı_numb = "3"


@client.event
async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
        if entry.user.bot:
            return
        delete_message_embed = discord.Embed(
            title=f'{message.author} Adlı Kullanıcı Mesajları Sildi | ID = {message.author.id} **>>>**'
            , description=f"```{message.content}```")
        delete_message_embed.set_thumbnail(url="https://cdn2.iconfinder.com/data/icons/smartphone-service-and-repair/128/Service__Repair_-_Copy-14-512.png")
        delete_message_embed.add_field(name=':scroll: MSG CHANNEL :scroll:', value=f'{message.channel.name}')
        channel = client.get_channel(1059935097253535884)
        await channel.send(embed=delete_message_embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="⚚ ~ Yetkili Menüsü ~ ⚚", description="Burda Yetkili Komutlarını Görebilirsiniz.", colour=0x9f715)
    embed.add_field(name=":broom: d!sil <Adet>", value="Verilen Değer kadar Mesaj Siler.", inline=True)
    embed.add_field(name=":hammer: d!ban <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Banlar.", inline=False)
    #embed.add_field(name=":leg: !kick <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Kickler.", inline=False) 
    embed.add_field(name=":mute: d!mute <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Susturur.", inline=False)
    embed.add_field(name=":sound: d!unmute <Kullanıcı>", value="Verilen Etiketteki Kullanıcının Mutesini Kaldırır", inline=False)        
    embed.set_thumbnail(url="https://cdn2.iconfinder.com/data/icons/web-application-icons-part-2/100/Artboard_76-512.png")
    await ctx.channel.send(embed=embed) 

@commands.has_role("Führer")
@client.command()
async def ban(ctx,member:discord.Member, *,args):

    if member.id == 935455852607987742:
        ctx.channel.send("sen anca ananı banla oç")
        return

    await member.ban(reason="KURALLAR UYMADI VEYA ZEVKİNDEN")

    await member.send(f"**{ctx.guild.name}** Adlı Sunucudan Banlandın Sebep: **{args}**")

    
    embed = discord.Embed(title=":hammer: Ban Info :hammer:", description="Kullanıcı Başarı İle Banlandı", color=discord.Colour.green())
    embed.add_field(name="Banlanan Kullanıcı", value=f"{member.mention}",inline=False)
    embed.add_field(name="Banlayan Yetkili", value=f"{ctx.author}",inline=False)
    embed.add_field(name="Açıklama", value=f"{args}",inline=False)
    await ctx.channel.send(embed=embed)



@client.command()
@commands.has_role("Führer")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    id = "935455852607987742"
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)


    await member.add_roles(mutedRole, reason=reason)
        #await ctx.send(f"**Susturuldu: {member.mention} Açıklama: {reason}**")
    await member.send(f"**{guild.name}** Adlı Sunucudan Susturuldun  Sebebi: **{reason}**")

    embed = discord.Embed(title=":mute: Mute Info :mute:", description="Kullanıcı Başarı İle Susturuldu", color=discord.Colour.green())
    embed.add_field(name="Susturulan", value=f"{member.mention}")
    embed.add_field(name="Susturan", value=f"{ctx.author}")
    embed.add_field(name="Açıklama", value=f"{reason}")
    embed.set_image(url="http://iconsetc.com/icons-watermarks/flat-circle-white-on-red/raphael/raphael_microphone-mute/raphael_microphone-mute_flat-circle-white-on-red_512x512.png")

    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_role("Führer")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    id = "935455852607987742"
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)


    await member.remove_roles(mutedRole, reason=None)
        #await ctx.send(f"**Susturuldu: {member.mention} Açıklama: {reason}**")
    await member.send(f"**{guild.name}** Adlı Sunucudan Susturulman Kalktı")

    embed = discord.Embed(title=":mute: Mute Info :mute:", description="Kullanıcı Başarı İle Susturulması Kaldırıldı", color=discord.Colour.green())
    embed.add_field(name="Susturulması Kaldırılan Kullanıcı", value=f"{member.mention}")
    embed.add_field(name="Susturmasını kaldıran Yetkili", value=f"{ctx.author}")
    embed.set_image(url="http://iconsetc.com/icons-watermarks/flat-circle-white-on-red/raphael/raphael_microphone-mute/raphael_microphone-mute_flat-circle-white-on-red_512x512.png")

    await ctx.channel.send(embed=embed)

@commands.has_role("Führer")
@client.command()
async def sil(ctx, amount=20):
    
    if amount > 250:
        await ctx.channel.send("Max Silinebilecek Mesaj Sayısı **250**")
        return

    await ctx.channel.purge(limit=amount)


    embed = discord.Embed(title=":broom: Sil Info :broom:", description="Mesajlar Başarı İle Silindi", color=discord.Colour.green())
    embed.add_field(name="Silinen Mesaj Sayısı", value=f"{amount}", inline=True)
    embed.add_field(name=f"Silen Yetkili", value=f"{ctx.author}", inline=False)
    embed.set_thumbnail(url="https://c.tenor.com/Mw__8SvDbi8AAAAC/checkmark-black.gif")
    await ctx.channel.send(embed=embed)
    
@commands.has_any_role("Führer","Ticket")
@client.command()
async def ticket(ctx):
    button = Button(label="🎫 - Create Ticket - 🎫", style=discord.ButtonStyle.green)
    embed = discord.Embed(title=":tickets: TICKET SYSTEM :tickets:",description="ticket oluşturmak için **Create Ticket** butonuna tıklayınız.", color=discord.Colour.green())
    embed.set_thumbnail(url="https://toppng.com/uploads/preview/two-tickets-icon-ticket-ico-11562902873mix2fznwjo.png")

    async def button_callback(interaction):
        guild = ctx.guild
        random_numb = random.randint(2000,3631)
        ticket_role = await interaction.guild.create_role(name=f"Ticket-{random_numb}")
        await interaction.user.add_roles(ticket_role)

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True),
            interaction.guild.get_role(1060221727084396715): discord.PermissionOverwrite(read_messages=True)
        }

        global ticket_channel
        ticket_channel = await interaction.guild.create_text_channel(f"ticket-{random_numb}",overwrites=overwrites)
        await ticket_channel.set_permissions(ticket_role,send_messages=True,read_messages=True)

        await ticket_channel.send("@everyone")
        ticket_embed = discord.Embed(title=":tickets: TICKET SYSTEM :tickets:",description="Ticket Created 🗸 || Yetkililerimiz Sizinle Yakında İlgilenecektir.", color=discord.Colour.green())
        ticket_embed.set_thumbnail(url="https://toppng.com/uploads/preview/two-tickets-icon-ticket-ico-11562902873mix2fznwjo.png")
        await ticket_channel.send(embed=ticket_embed)


    button.callback = button_callback

    view = View()
    view.add_item(button)

    await ctx.channel.send(embed=embed, view=view)

@commands.has_any_role("Führer","Ticket")
@client.command()
async def close(ctx):
    button = Button(label="Close Ticket", style=discord.ButtonStyle.red)
    embed = discord.Embed(title=":tickets: TICKET SYSTEM :tickets:",description="ticket Kapatmak için **Close Ticket** butonuna tıklayınız.", color=discord.Colour.green())
    embed.set_thumbnail(url="https://toppng.com/uploads/preview/two-tickets-icon-ticket-ico-11562902873mix2fznwjo.png")

    async def button_callback(interaction,*,channel_name=None):
        guild = ctx.guild
        await interaction.channel.delete()
        role = discord.utils.get(ctx.message.guild.roles, name=f"ticket-{channel_name}")



    

        

    button.callback = button_callback
    view=View()
    view.add_item(button)

    await ctx.channel.send(embed=embed,view=view)


client.run("TOKEN")
