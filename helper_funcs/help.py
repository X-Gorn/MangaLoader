# Credits:
# @SpEcHiDe for his progress_for_pyrogram, humanbytes, TimeFormatter
# @DevsExpo for their run_cmd

import math, os, time, tldextract, asyncio, shlex
from typing import Tuple

supported = '''http://18comic.org
http://1stkissmanga.com
http://1stkissmanhua.com
http://365manga.com
http://3asq.org
http://7sama.com
http://8muses.com
http://ac.qq.com
http://acomics.ru
http://addfunny.com
http://allhentai.ru
http://allporncomic.com
http://aloalivn.com
http://animangaes.com
http://animextremist.com
http://antisensescans.com
http://aoc.moe
http://arangscans.com
http://asmhentai.com
http://astrallibrary.net
http://asurascans.com
http://atfbooru.ninja
http://bacamanga.co
http://bato.to
http://bestmanhua.com
http://blogtruyen.com
http://boyslove.me
http://catmanga.org
http://catonhead.com
http://cdmnet.com.br
http://centraldemangas.online
http://chochox.com
http://cmreader.info
http://com-x.life
http://comic-walker.com
http://comic.k-manga.jp
http://comic.naver.com
http://comic.webnewtype.com
http://comicextra.com
http://comickiba.com
http://comico.jp
http://comicpunch.net
http://comicvn.net
http://cycomi.com
http://danbooru.donmai.us
http://darkskyprojects.org
http://desu.me
http://digitalteam1.altervista.org
http://digitalteamreader.netsons.org
http://disasterscans.com
http://dm5.com
http://doujin-moe.us
http://doujins.com
http://e-hentai.org
http://edelgardescans.com
http://einherjarscans.space
http://en.ruyamanga.com
http://es.leviatanscans.com
http://fanfox.net
http://freewebtooncoins.com
http://funmanga.com
http://genkan.io
http://gmanga.me
http://godsrealmscan.com
http://grazescans.com
http://hatigarmscanz.net
http://heavenmanga.biz
http://heavenmanga.com
http://helveticascans.com
http://hentai-chan.me
http://hentai-chan.me
http://hentai-image.com
http://hentai-img.com
http://hentai.cafe
http://hentai2read.com
http://hentaifox.com
http://hentaihand.com
http://hentaihere.com
http://hentailxx.com
http://hentainexus.com
http://hentaiporns.net
http://hentairead.com
http://hentaivn.net
http://heromanhua.com
http://herozscans.com
http://hgamecg.com
http://hiperdex.com
http://hitomi.la
http://hocvientruyentranh.com
http://hscans.com
http://http://reader.jokerfansub.com
http://hunlight-scans.info
http://immortalupdates.com
http://imperfectcomic.com
http://inmanga.com
http://isekaiscan.com
http://isekaiscanmanga.com
http://itsyourightmanhua.com
http://jaiminisbox.net
http://japscan.(cc|com|co|to|se
http://jjutsuscans.com
http://jurnalu.ru
http://kisekimanga.com
http://kisslove.net
http://kissmanga.com
http://kissmanga.in
http://kkjscans.co
http://kobato.hologfx.com
http://kobato.hologfx.com/reader
http://komikcast.com
http://komikgue.com
http://komikid.com
http://komikstation.com
http://krakenscans.com
http://kumanga.com
http://lector.patyscans.com
http://leitor.net
http://leviatanscans.com
http://lezhin.com
http://lhscan.net
http://lhtranslation.net
http://lilymanga.com
http://littlexgarden.com
http://lolibooru.moe
http://lolivault.net
http://loveheaven.net
http://luscious.net
http://lynxscans.com
http://manga-online.biz
http://manga-tr.com
http://manga-tube.me
http://manga-v2.mangavadisi.org
http://manga.mexat.com
http://manga18.fun
http://manga18fx.com
http://manga1st.com
http://manga1st.online
http://manga347.com
http://manga3s.com
http://manga41.com
http://manga4life.com
http://manga68.com
http://manga99.com
http://mangaae.com
http://mangaarabteam.com
http://mangabat.com
http://mangabin.com
http://mangabob.com
http://mangabox.me
http://mangacanblog.com
http://mangachan.me
http://mangachill.com
http://mangaclash.com
http://mangaclub.ru
http://mangacultivator.com
http://mangadeep.com
http://mangadex.org
http://mangadods.com
http://mangadoor.com
http://mangaeden.com
http://mangaeffect.com
http://mangafreak.net
http://mangago.me
http://mangagreat.com
http://mangahentai.me
http://mangahere.cc
http://mangahere.onl
http://mangahome.com
http://mangahub.io
http://mangahub.ru
http://mangaid.co
http://mangaindo.web.id
http://mangainn.net
http://mangakakalot.com
http://mangakakalot.fun
http://mangakatana.com
http://mangakik.com
http://mangakiss.org
http://mangakita.net
http://mangakomi.com
http://mangaku.in
http://mangaku.pro
http://mangalib.me
http://mangalord.com
http://mangamew.com
http://manganato.com
http://manganelo.com
http://manganelo.link
http://manganelos.com
http://manganine.com
http://mangaonline.com.br
http://mangapanda.onl
http://mangapark.net
http://mangarave.com
http://mangaread.co
http://mangaread.org
http://mangareader.cc
http://mangareader.net
http://mangareader.site
http://mangarockteam.com
http://mangarocky.com
http://mangaroma.com
http://mangarussia.com
http://mangasco.com
http://mangasee123.com
http://mangashiro.net
http://mangasushi.net
http://mangasy.com
http://mangatail.me
http://mangatoo.com
http://mangatown.com
http://mangaturf.com
http://mangatx.com
http://mangaus.xyz
http://mangavy.com
http://mangaweebs.in
http://mangawindow.net
http://mangaz.com
http://mangazuki.co
http://mangazuki.me
http://mangazuki.online
http://mangazukinew.online
http://manhuabox.net
http://manhuaes.com
http://manhuafast.com
http://manhuaga.com
http://manhuagui.com
http://manhuaplus.com
http://manhuas.net
http://manhuasworld.com
http://manhuasy.com
http://manhuatai.com
http://manhuaus.com
http://manhwa.club
http://manhwa.live
http://manhwa18.net
http://manhwahentai.me
http://manhwareader.com
http://manhwatop.com
http://manytoon.com
http://manytoon.me
http://mentalmanga.com
http://menudo-fansub.com
http://merakiscans.com
http://methodscans.com
http://milftoon.xxx
http://mintmanga.live
http://miraclescans.com
http://mixedmanga.com
http://mm-scans.com
http://mortalsgroove.com
http://mymanga.io
http://mymangalist.org
http://myreadingmanga.info
http://mysticalmerries.com
http://nazarickscans.com
http://neatmanga.com
http://nekoscan.com
http://nettruyen.com
http://neumanga.tv
http://new.renascans.com
http://nhentai.net
http://niadd.com
http://nightcomic.com
http://nightow.net
http://nineanime.com
http://ninemanga.com
http://nitroscans.com
http://noranofansub.com
http://ntsvoidscans.com
http://onma.me
http://onmanga.com
http://otscans.com
http://painfulnightzscan.com
http://perveden.com
http://plus.comico.jp
http://pmscans.com
http://porncomix.info
http://porncomixonline.net
http://primemanga.com
http://pururin.io
http://puzzmos.com
http://pzykosis666hfansub.com
http://raiderscans.com
http://randomtranslations.com
http://ravens-scans.com
http://raw.senmanga.com
http://rawdevart.com
http://rawmangaupdate.com
http://read.egscans.com
http://read.lhtranslation.com
http://read.powermanga.org
http://read.ptscans.com
http://read.yagami.me
http://readcomiconline.to
http://readcomicsonline.ru
http://reader.championscans.comco
http://reader.deathtollscans.net
http://reader.decadencescans.com
http://reader.evilflowers.com
http://reader.fos-scans.com
http://reader.jokerfansub.com
http://reader.kireicake.com
http://reader.letitgo.scans.today
http://reader.manga-download.org
http://reader.serenade.moe
http://reader.silentsky-scans.net
http://reader.thecatscans.com
http://reader.vortex-scans.com
http://readmanga.live
http://readmanganato.com
http://readmanhua.net
http://readmng.com
http://reaperscans.com
http://remanga.org
http://rocaca.com
http://s-manga.net
http://s2manga.com
http://santosfansub.com
http://secretscan.co
http://selfmanga.ru
http://senmanga.com
http://sensescans.com
http://serimanga.com
http://shakai.ru
http://shieldmanga.club
http://shogakukan.co.jp
http://shoujohearts.com
http://siberowl.com
http://sixiangscans.com
http://skscans.com
http://skymanga.co
http://sleepypandascans.co
http://sleepytranslations.com
http://slide.world-three.org
http://socialweebs.in
http://soloscanlation.site
http://submanga.online
http://sunday-webry.com
http://taadd.com
http://tapas.io
http://taptaptaptaptap.net
http://tenmanga.com
http://the-nonames.com
http://thetopcomic.com
http://tonarinoyj.jp
http://toongod.com
http://toonily.com
http://toonily.net
http://toonpoint.com
http://topmanhua.com
http://translate.webtoons.com
http://tritinia.com
http://truecolorsscans.miocio.org
http://truyen.vnsharing.site
http://truyenchon.com
http://truyentranhtuan.com
http://tsumino.com 
http://twilightscans.com
http://universoyuri.com
http://vanguardbun.com
http://viz.com
http://voidscans.com
http://web-ace.jp
http://webnovel.live
http://webtoon.uk
http://webtoon.xyz
http://webtoonily.com
http://webtoons.com
http://wescans.xyz
http://westmanga.info
http://whitecloudpavilion.com
http://wiemanga.com
http://wmanga.ru
http://woopread.com
http://wuxiaworld.site
http://xanime-seduccion.com
http://yande.re
http://yuri-ism.net
http://zeroscans.com
http://zinmanga.com
'''

def check_url(url):
    if 'http' or 'https' in url:
        pass
    else:
        return
    if ' ' in url:
        url = url.split(' ')[0]
    ext = tldextract.extract(url)
    pre = f'{ext.subdomain}.{ext.domain}.{ext.suffix}'
    if not ext.subdomain:
        pre = f'{ext.domain}.{ext.suffix}'
    if pre in supported:
        return True
    else:
        return False


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \nP: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "{0} of {1}\nSpeed: {2}/s\nETA: {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
