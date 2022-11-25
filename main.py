import nextcord
from email.mime import image
from http.client import responses
import random, os
from nextcord.ext import commands

TOKEN = ['token']
PREFIX = ['.']

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Il bot è online!")
    await bot.change_presence(activity=nextcord.Game(name="fotterti i dati"))

@bot.event
async def on_command_error(ctx, error):
    em = nextcord.Embed(title=f"Errore!", description=f"Comando non trovato! :sob:", color=nextcord.Color.from_rgb(248, 117, 255))
    await ctx.send(embed=em)

@bot.command()
async def help(ctx):
    """Mostra la lista dei comandi"""
    emb = nextcord.Embed(title=f"Lista comandi", description=f"**.ciao / .hi**  -  Ti Saluta!\n\n**.gerry / .g**  -  Manda una foto di Gerry Scotti!\n\n**.ripeti / .r**  -  Ripete un qualsiasi messaggio scritto da te\n\n**.ping**  -  Dice pong, nient'altro.\n\n**.info**  -   Mostra informazioni sul creatore del bot\n\n**.ziopera / .zp**  -  Zio pera...\n\n**.frittomisto / .splash**  -  SPLASHHH\n\n**.turiipipip**  -  Manda turi ip ip ip in chat\n\n**.wenomechainsama**  -  Manda wenomechainsama in chat\n\n**.molise**  -  Manda una foto del Molise\n\n**.xijinping / .xi**  -  Xi Jinping Winnie The Pooh fa ridere.\n\n**.taiwan**  -  Il Taiwan esiste.\n\n**.carkvids / .cark**  -  Manda il link di un video di cark a caso\n\n**.berlusconi / .b**  -  Manda una foto carina di Berlusconi\n\n**.porco**  -  Manda la foto di un porco\n\n **.salvini**  -  Manda una foto carina di Matteo Salvini\n\n**.bambini**  -  Ti da un sito bello", color=nextcord.Color.from_rgb(248, 117, 255))
    emb.set_thumbnail(url="https://static.wikia.nocookie.net/youtube/images/1/1a/Carkyboi.png/revision/latest/scale-to-width-down/250?cb=20200924235749")
    await ctx.send(embed=emb)

@bot.command(aliases = ["hi"])
async def ciao(ctx):
    """Ti saluta!"""
    await ctx.send("Ciao, " + ctx.author.mention + "! :wave:")

@bot.command(aliases = ["g"])
async def gerry(ctx):
    """Manda una foto di Gerry Scotti!"""
    foto = ["https://www.chenews.it/wp-content/uploads/2020/08/Gerry-Scotti-2-650x472.jpg",
                 "https://64.media.tumblr.com/a573941f1a64ff30e1f97236e58d42b6/tumblr_plcftg3xrA1tlsda4o1_500.gifv",
                 "https://www.donnamoderna.com/content/uploads/2020/10/GettyImages-1142898643.jpg",
                 "https://www.youmovies.it/wp-content/uploads/2022/08/Gerry-Scotti-1.jpg",
                 "https://www.cinematographe.it/wp-content/uploads/2022/08/IMG_20220807_095932.jpg",
                 "https://c.tenor.com/rLgXG0RsSroAAAAd/gerry-scotti-striscia-la-notizia.gif",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUcnPT6nVqX0RhxKg1ToMvBd_6Yi0JrfxAAA&usqp=CAU",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDji4ehfpoYOlwLUhLWUb55tTUtTGbY80pDg&usqp=CAU",
                 "https://www.cinematographe.it/wp-content/uploads/2022/08/IMG_20220807_095932.jpg",
                 "https://cdn.gelestatic.it/kataweb/tvzap/2016/01/foto_gerry_scottiok.jpg",
                 "https://www.gedistatic.it/content/gedi/img/huffingtonpost/2018/01/27/105244273-1be2e529-20d3-4532-8eb3-c6ca21de47cc.jpeg",
                 "https://st.ilfattoquotidiano.it/wp-content/uploads/2018/11/06/scotti-905.jpg",
                 "https://img.corr.it/images/2021/09/11/171220387-cff766ae-2851-45fc-a105-11979fd5e47d.jpg"]
    
    gerry=nextcord.Embed(title="Ecco una foto di Gerry per te ;)", color=nextcord.Color.from_rgb(248, 117, 255))
    gerry.set_image(url=f"{random.choice(foto)}")
    await ctx.send(embed=gerry)


@bot.command(aliases = ["r"])
async def ripeti(ctx, *, arg):
    """Ripete un qualsiasi messaggio scritto da te"""
    await ctx.send(arg)

@bot.command()
async def ping(ctx):
    """Dice pong."""
    await ctx.send("Pong!")

@bot.command()
async def info(ctx):
  """Informazioni sul creatore del bot"""
  info = nextcord.Embed(title="Info sul creatore del bot", description="Bot creato da cark#9892 e hostato sul mio PC!!1!\nNon so una pippa di Python quindi accontentatevi del troiaio che è venuto fuori ;)\n\n\n Instagram: @222fxde            YouTube: FedixinoTM", color=nextcord.Color.from_rgb(248, 117, 255))
  info.set_thumbnail(url="https://static.wikia.nocookie.net/youtube/images/1/1a/Carkyboi.png/revision/latest/scale-to-width-down/250?cb=20200924235749")
  await ctx.send(embed=info)

@bot.command(aliases=["zp"])
async def ziopera(ctx):
    """Zio pera..."""
    zpzp = nextcord.File("media/ziopera.gif", filename="ziopera.gif")
    ziopera=nextcord.Embed(title="Zio pera...", color=nextcord.Color.from_rgb(248, 117, 255))
    ziopera.set_image(url="attachment://ziopera.gif")
    await ctx.send(file=zpzp, embed=ziopera)

@bot.command(aliases=["splash"])
async def frittomisto(ctx):
    """SPLASHHH"""
    file = nextcord.File("audio/frittomisto.mp3")
    await ctx.send(file=file, content="SPLASH")

@bot.command()
async def turiipipip(ctx):
    """Manda turi ip ip ip in chat"""
    file = nextcord.File("audio/turiipipip.mp3")
    await ctx.send(file=file, content="turi ip ip ip :sob:")

@bot.command()
async def wenomechainsama(ctx):
    """Manda wenomechainsama in chat"""
    file = nextcord.File("audio/wenomechainsama.mp3")
    await ctx.send(file=file, content="wenomechainsama :sob:")

@bot.command()
async def molise(ctx):
    """Manda una foto del Molise"""
    molise=nextcord.Embed(title="MOLISE", description="MOLISE", color=nextcord.Color.from_rgb(248, 117, 255))
    molise.set_image(url="https://i.imgur.com/xRBjFck.png")
    await ctx.send(embed=molise)

@bot.command(aliases=["xi"])
async def xijinping(ctx):
    """Xi Jinping Winnie the Pooh fa ridere."""
    xijinping=nextcord.Embed(title="Xi Jinping Winnie The Pooh fa ridere.", color=nextcord.Color.from_rgb(248, 117, 255))
    xijinping.set_image(url="https://www.tempi.it/wp-content/uploads/2020/01/xi-jinping-winnie-the-pooh.jpg")
    await ctx.send(embed=xijinping)

@bot.command()
async def taiwan(ctx):
    """Il Taiwan esiste."""
    taiwan=nextcord.Embed(title="Il Taiwan esiste.", color=nextcord.Color.from_rgb(248, 117, 255))
    taiwan.set_image(url="https://static.sky.it/images/skytg24/it/mondo/2022/06/20/terremoto-taiwan-oggi/taiwan.png")
    await ctx.send(embed=taiwan)

@bot.command(aliases=["cark"])
async def carkvids(ctx):
    """Invia il link di un video di cark!"""
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
    
    await ctx.send(f"{random.choice(vids)}")

@bot.command(aliases=["b"])
async def berlusconi(ctx):
    berlusconi=nextcord.Embed(title="Ecco una foto carina di Berlusconi per te :)", color=nextcord.Color.from_rgb(248, 117, 255))
    berlusco=("https://www.artribune.com/wp-content/uploads/2011/11/227.jpg",
                "https://www.tag24.it/wp-content/uploads/2022/03/universitas-libertatis-home.jpg",
                "https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt7df1cc806c3fb76b/60de8432ddcd520eeb9509e4/0c142578c4918e368e21b1e4da94ee1ed2675a7e.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiZ5hTuH6VYecmq-9yQ4C6jtDtSU57_jDVPFt2kEvhpA&s",
                "https://www.ciociariaoggi.it/download/img/full/89791_6wzswjt.jpg",
                "https://abruzzoweb.it/wp-content/uploads/2020/09/silvioberlusconinw345.jpg",
                "https://www.raiplay.it/cropgd/1080x720/dl/img/2018/02/15189870859818396449.png",
                "https://www.bdtorino.net/files/lmDmONNNxzuCoNQVRz91-07dona-xlarge1-jpg.jpg",
                "https://www.repstatic.it/content/localirep/img/rep/2021/03/24/213712770-a7bf2c7c-5952-426b-8397-6acfe0baed9c.jpg",
                "https://www.seriebnews.com/wp-content/uploads/2022/04/Berlusconi-20220407-seriebnews.com_.jpg",
                "https://www.terzobinario.it/wp-content/uploads/2013/05/berlusconi2.jpg")
    berlusconi.set_image(url=f"{random.choice(berlusco)}")
    await ctx.send(embed=berlusconi)

@bot.command()
async def porco(ctx):
        porco=nextcord.Embed(title="Porco", color=nextcord.Color.from_rgb(248, 117, 255))
        porco.set_image(url="https://www.greenme.it/wp-content/uploads/2022/04/maiale_allevamento.jpg")
        await ctx.send(embed=porco)

@bot.command(aliases=["s"])
async def salvini(ctx):
    salvini=nextcord.Embed(title="Ecco una foto carina di Salvini ;)", color=nextcord.Color.from_rgb(248, 117, 255))
    salvoni=("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Matteo_Salvini_Viminale.jpg/1200px-Matteo_Salvini_Viminale.jpg",
             "https://img-prod.ilfoglio.it/2022/08/29/164327921-4ca48d95-e045-48fb-9d62-337555fd1970.jpg",
             "https://legaonline.it/wp-content/uploads/sites/4/revslider/slider-1/Salvini.png",
             "https://legaonline.it/wp-content/uploads/sites/4/2022/08/Senza-titolo-1-1.png",
             "https://img-prod.ilfoglio.it/2020/07/30/1592816383299_1592816426_492x275_1596148383576.jpg",
             "https://www.ansa.it/webimages/img_457x/2021/9/5/076933b83fd1d10f86fb304ce883b3df.jpg")
    salvini.set_image(url=f"{random.choice(salvoni)}")
    await ctx.send(embed=salvini)

@bot.command()
async def bambini(ctx):
    await ctx.send("twitter.com")

@bot.command()
async def moscani(ctx):
    file = nextcord.File("media/moscani.jpg")
    await ctx.send(file=file, content="madonna che topo mi sto bagnando")

bot.run(TOKEN)
