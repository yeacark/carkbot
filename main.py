import nextcord, NextcordUtils, random
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="-", intents=intents)
music = NextcordUtils.Music()

bot.remove_command('help')

@bot.event
# Stampa un messaggio sulla linea di comando quando il bot si avvia e imposta uno stato di gioco
async def on_ready():
    print("Il bot è online!")
    await bot.change_presence(activity=nextcord.Game(name="-help"))

# Lista variabili
foto = ("https://www.chenews.it/wp-content/uploads/2020/08/Gerry-Scotti-2-650x472.jpg",
"https://www.donnamoderna.com/content/uploads/2020/10/GettyImages-1142898643.jpg",
"https://www.youmovies.it/wp-content/uploads/2022/08/Gerry-Scotti-1.jpg",
"https://www.cinematographe.it/wp-content/uploads/2022/08/IMG_20220807_095932.jpg",
"https://c.tenor.com/rLgXG0RsSroAAAAd/gerry-scotti-striscia-la-notizia.gif",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUcnPT6nVqX0RhxKg1ToMvBd_6Yi0JrfxAAA&usqp=CAU",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDji4ehfpoYOlwLUhLWUb55tTUtTGbY80pDg&usqp=CAU",
"https://www.cinematographe.it/wp-content/uploads/2022/08/IMG_20220807_095932.jpg",
"https://cdn.gelestatic.it/kataweb/tvzap/2016/01/foto_gerry_scottiok.jpg",
"https://www.gedistatic.it/content/gedi/img/huffingtonpost/2018/01/27/105244273-1be2e529-20d3-4532-8eb3-c6ca21de47cc.jpeg",
"https://st.ilfattoquotidiano.it/wp-content/uploads/2018/11/06/scotti-905.jpg")

vids = ("https://www.youtube.com/watch?v=0nnSNO7WdDE",
"https://www.youtube.com/watch?v=A_KW0D-n5wM",
"https://www.youtube.com/watch?v=ULZYNV4jlMQ",
"https://www.youtube.com/watch?v=p0LHE8yRyvg",
"https://www.youtube.com/watch?v=8SCqztNlfEM",
"https://www.youtube.com/watch?v=8x7KFiwpGeE",
"https://www.youtube.com/watch?v=fl-1GTSPjxc",
"https://www.youtube.com/watch?v=nt4U5A8zPdQ",
"https://www.youtube.com/watch?v=feXA8sTnWYY",
"https://www.youtube.com/watch?v=RgmfkGWSu7g",
"https://www.youtube.com/watch?v=9ltqaTVuh0U",
"https://www.youtube.com/watch?v=1rjqHF4wclg",
"https://www.youtube.com/watch?v=mvTjqs7jqg0",
"https://www.youtube.com/watch?v=OdML8TSGwfQ",
"https://www.youtube.com/watch?v=v74vH3LjSuo",
"https://www.youtube.com/watch?v=xnmR0L2hr9g",
"https://www.youtube.com/watch?v=vIX7CMj2VZk",
"https://www.youtube.com/watch?v=nySaFuZ9lbA",
"https://www.youtube.com/watch?v=7es6IYnswSM",
"https://www.youtube.com/watch?v=HmjrIzInVXU",
"https://www.youtube.com/watch?v=mRHxnaHVjyI",
"https://www.youtube.com/watch?v=hQ7lLOg63rg")

berlusco = ("https://www.artribune.com/wp-content/uploads/2011/11/227.jpg",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiZ5hTuH6VYecmq-9yQ4C6jtDtSU57_jDVPFt2kEvhpA&s",
"https://abruzzoweb.it/wp-content/uploads/2020/09/silvioberlusconinw345.jpg",
"https://www.raiplay.it/cropgd/1080x720/dl/img/2018/02/15189870859818396449.png",
"https://www.bdtorino.net/files/lmDmONNNxzuCoNQVRz91-07dona-xlarge1-jpg.jpg",
"https://www.repstatic.it/content/localirep/img/rep/2021/03/24/213712770-a7bf2c7c-5952-426b-8397-6acfe0baed9c.jpg",
"https://www.seriebnews.com/wp-content/uploads/2022/04/Berlusconi-20220407-seriebnews.com_.jpg",
"https://www.terzobinario.it/wp-content/uploads/2013/05/berlusconi2.jpg")

salvoni=("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Matteo_Salvini_Viminale.jpg/1200px-Matteo_Salvini_Viminale.jpg",
"https://img-prod.ilfoglio.it/2022/08/29/164327921-4ca48d95-e045-48fb-9d62-337555fd1970.jpg",
"https://legaonline.it/wp-content/uploads/sites/4/revslider/slider-1/Salvini.png",
"https://legaonline.it/wp-content/uploads/sites/4/2022/08/Senza-titolo-1-1.png",
"https://img-prod.ilfoglio.it/2020/07/30/1592816383299_1592816426_492x275_1596148383576.jpg",
"https://www.ansa.it/webimages/img_457x/2021/9/5/076933b83fd1d10f86fb304ce883b3df.jpg")

@bot.command(aliases = ["aiuto"])
async def help(ctx):
    help1 = nextcord.Embed(color=nextcord.Color.from_rgb(248, 117, 255)).add_field(name=f"Lista comandi - Pagina 1", value=f"**-gerry / -g**  \
    -  Manda una foto di Gerry Scotti!\n\n**-info** \
    -  Mostra informazioni sul creatore del bot\n\n**-ziopera / -zp** \
    -  Zio pera...\n\n**-frittomisto** \
    -  SPLASHHH\n\n**-turiipipip** \
    -  Manda turi ip ip ip in chat\n\n**-wenomechainsama** \
    -  Manda wenomechainsama in chat\n\n**-salvini** \
    -  Manda una foto carina di Matteo Salvini")
    help2 = nextcord.Embed(color=nextcord.Color.from_rgb(248, 117, 255)).add_field(name="Lista comandi - Pagina 2", value="**-molise** \
    - Manda una foto del Molise\n\n**-xijinping / -xi** \
    -  Xi Jinping Winnie The Pooh fa ridere.\n\n**-taiwan** \
    -  Il Taiwan esiste.\n\n**-carkvids / -cark** \
    -  Manda il link di un video di cark\n\n**-berlusconi / -b** \
    -  Manda una foto carina di Berlusconi\n\n**-porco** \
    -  Manda la foto di un porco")
    help1.set_thumbnail(url="https://static.wikia.nocookie.net/youtube/images/1/1a/Carkyboi.png/revision/latest/scale-to-width-down/250?cb=20200924235749")
    help2.set_thumbnail(url="https://static.wikia.nocookie.net/youtube/images/1/1a/Carkyboi.png/revision/latest/scale-to-width-down/250?cb=20200924235749")
    paginator = NextcordUtils.Pagination.AutoEmbedPaginator(ctx)
    embeds = [help1, help2]
    await paginator.run(embeds)

@bot.command(aliases = ["g"])
# Manda una foto di Gerry Scotti
async def gerry(ctx):    
    gerry=nextcord.Embed(title="Ecco una foto di Gerry per te :3", color=nextcord.Color.from_rgb(248, 117, 255))
    gerry.set_image(url=f"{random.choice(foto)}")
    await ctx.send(embed=gerry)

@bot.command()
# Informazioni sul creatore del bot
async def info(ctx):
  info = nextcord.Embed(title="Info sul creatore del bot", description="""Bot creato da yeacark:bangbang:\n
  ~~Non~~ so una pippa di Python quindi accontentatevi del troiaio che è venuto fuori.
  Ovvio aiuto di Rice7th che sennò qua cark fa suicidare i contributor che vedono sto codice :rolling_eyes:
  https://yeacark.github.io/""", color=nextcord.Color.from_rgb(248, 117, 255))
  info.set_thumbnail(url="https://static.wikia.nocookie.net/youtube/images/1/1a/Carkyboi.png/revision/latest/scale-to-width-down/250?cb=20200924235749")
  await ctx.send(embed=info)

@bot.command(aliases=["zp"])
# Zio pera-
async def ziopera(ctx):
    zpzp = nextcord.File("media/ziopera.gif", filename="ziopera.gif")
    ziopera=nextcord.Embed(title="Zio pera...", color=nextcord.Color.from_rgb(248, 117, 255))
    ziopera.set_image(url="attachment://ziopera.gif")
    await ctx.send(file=zpzp, embed=ziopera)

@bot.command()
# Splashhh
async def frittomisto(ctx):
    file = nextcord.File("audio/frittomisto.mp3")
    await ctx.send(file=file, content="SPLASH")

@bot.command()
# Manda turi ip ip ip in chat
async def turiipipip(ctx):
    file = nextcord.File("audio/turiipipip.mp3")
    await ctx.send(file=file, content="turi ip ip ip :sob:")

@bot.command()
# Manda wenomechainsama in chat
async def wenomechainsama(ctx):
    file = nextcord.File("audio/wenomechainsama.mp3")
    await ctx.send(file=file, content="wenomechainsama :sob:")

@bot.command()
# Manda una foto del Molise
async def molise(ctx):
    molise=nextcord.Embed(title="MOLISE", description="MOLISE", color=nextcord.Color.from_rgb(248, 117, 255))
    molise.set_image(url="https://i.imgur.com/xRBjFck.png")
    await ctx.send(embed=molise)

@bot.command(aliases=["xi"])
# Xi Jinping Winnie the Pooh fa ridere
async def xijinping(ctx):
    xijinping=nextcord.Embed(title="Xi Jinping Winnie The Pooh fa ridere.", color=nextcord.Color.from_rgb(248, 117, 255))
    xijinping.set_image(url="https://www.tempi.it/wp-content/uploads/2020/01/xi-jinping-winnie-the-pooh.jpg")
    await ctx.send(embed=xijinping)

@bot.command()
# Il Taiwan esiste :p
async def taiwan(ctx):
    taiwan=nextcord.Embed(title="Il Taiwan esiste.", color=nextcord.Color.from_rgb(248, 117, 255))
    taiwan.set_image(url="https://static.sky.it/images/skytg24/it/mondo/2022/06/20/terremoto-taiwan-oggi/taiwan.png")
    await ctx.send(embed=taiwan)

@bot.command(aliases=["cark"])
# Invia il link di un video di cark!
async def carkvids(ctx):
    await ctx.send(f"{random.choice(vids)}")

@bot.command(aliases=["b"])
# Manda una foto carina di Berlusconi
async def berlusconi(ctx):
    berlusconi=nextcord.Embed(title="Ecco una foto carina di Berlusconi per te", color=nextcord.Color.from_rgb(248, 117, 255))
    berlusconi.set_image(url=f"{random.choice(berlusco)}")
    await ctx.send(embed=berlusconi)

@bot.command(aliases=["p"])
# Porco
async def porco(ctx):
        porco=nextcord.Embed(title="Porco", color=nextcord.Color.from_rgb(248, 117, 255))
        porco.set_image(url="https://www.greenme.it/wp-content/uploads/2022/04/maiale_allevamento.jpg")
        await ctx.send(embed=porco)

@bot.command(aliases=["s"])
# Manda una foto carina di Salvini
async def salvini(ctx):
    salvini=nextcord.Embed(title="Ecco una foto carina di Salvini", color=nextcord.Color.from_rgb(248, 117, 255))
    salvini.set_image(url=f"{random.choice(salvoni)}")
    await ctx.send(embed=salvini)

@bot.command()
# Fa partire Fritto Misto in chat vocale
async def splash(ctx, *, url):
    # Controlla se l'utente è in un canale vocale
    if ctx.author.voice is None:
        await ctx.send("Devi essere in un canale vocale per usare questo comando.")
    voice_channel = ctx.author.voice.channel
    # Controlla se il bot è già connesso a un canale vocale
    if ctx.voice_client is None:
        await voice_channel.connect()
    elif ctx.voice_client.channel != voice_channel:
        await ctx.voice_client.move_to(voice_channel)
    voice_client = ctx.voice_client
    # Carica e riproduce l'audio
    source = nextcord.FFmpegPCMAudio(url)
    if not voice_client.is_playing():
        voice_client.play(source)
        await ctx.send(f"In riproduzione FRITTO MISTO")
    else:
        song = await voice_client.queue(url, search=True)
        await ctx.send(f"Accodato {song.name}")

@bot.command(aliases=["fottiti"])
# Se leva dai maroni
async def esci(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("Esiliato.")

@bot.command(aliases=["zitto"])
# TASI
async def muto(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Castigato.")

# Il tuo token va qui
bot.run("