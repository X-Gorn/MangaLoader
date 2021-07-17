import os, shutil, time, zipfile, glob
from pyrogram import Client, filters
from translation import Translation
from pathlib import Path
from helper_funcs.help import run_cmd, progress_for_pyrogram


pdf_filter = filters.create(lambda _, __, query: query.data.lower() == "pdf")
zip_filter = filters.create(lambda _, __, query: query.data.lower() == "zip")
folder_filter = filters.create(lambda _, __, query: query.data.lower() == "folder")


@Client.on_callback_query(pdf_filter)
async def _pdf(bot, callback_query):
    update = callback_query.message.reply_to_message
    await callback_query.message.delete()
    url = update.text
    manga_dir = './Manga/'
    if os.path.isdir(manga_dir):
        await update.reply_text('Still processing another manga')
        return
    os.mkdir(manga_dir)
    pablo = await update.reply_text('Downloading...')
    cmd = f'manga-py {url}'
    await run_cmd(cmd)
    count = 0
    d = manga_dir
    for file in glob.glob(f'{manga_dir}*/'):
        for path in os.listdir(file):
            if os.path.isfile(os.path.join(file, path)):
                count += 1
        if int(count) == 0:
            await pablo.edit_text("Process Stopped. can't download manga url")
            shutil.rmtree(d)
            return
    for file in glob.glob(f'{manga_dir}*/'):
        file_dir = file[8:-1]
        p = Path('.')
        for f in p.glob(f'Manga/{file_dir}/*.zip'):
            with zipfile.ZipFile(f, 'r') as archive:
                archive.extractall(path=f'./Manga/{file_dir}/{f.stem}')
                os.remove(f'./Manga/{file_dir}/{f.stem}/info.txt')
                os.remove(f'./Manga/{file_dir}/{f.stem}.zip')
                cmd = f'dir2pdf --subdirs vol_(.*) Manga/{file_dir}/' + 'vol_{}.pdf' + f' Manga/{file_dir}/'
                await run_cmd(cmd)
                shutil.rmtree(f'./Manga/{file_dir}/{f.stem}')
        shutil.make_archive(file_dir, 'zip', file)
        start_time = time.time()
        await pablo.edit_text('Uploading...')
        await bot.send_document(
            update.chat.id,
            file_dir + '.zip',
            caption=file_dir,
            progress=progress_for_pyrogram,
            progress_args=(
                'Uploading...',
                pablo,
                start_time
            )
        )
        os.remove(file_dir + '.zip')
        shutil.rmtree(manga_dir)
        await pablo.delete()


@Client.on_callback_query(zip_filter)
async def _zip(bot, callback_query):
    update = callback_query.message.reply_to_message
    await callback_query.message.delete()
    url = update.text
    manga_dir = './Manga/'
    if os.path.isdir(manga_dir):
        await update.reply_text('Still processing another manga')
        return
    os.mkdir(manga_dir)
    cmd = f'manga-py {url}'
    pablo = await update.reply_text('Downloading...')
    await run_cmd(cmd)
    count = 0
    d = manga_dir
    for file in glob.glob(f'{manga_dir}*/'):
        for path in os.listdir(file):
            if os.path.isfile(os.path.join(file, path)):
                count += 1
        if int(count) == 0:
            await pablo.edit_text("Process Stopped. can't download manga url")
            shutil.rmtree(d)
            return
    for file in glob.glob(f'{manga_dir}*/'):
        file_dir = file[8:-1]
        shutil.make_archive(file_dir, 'zip', file)
        start_time = time.time()
        await pablo.edit_text('Uploading...')
        await bot.send_document(
            update.chat.id,
            file_dir + '.zip',
            caption=file_dir,
            progress=progress_for_pyrogram,
            progress_args=(
                'Uploading...',
                pablo,
                start_time
            )
        )
        os.remove(file_dir + '.zip')
        shutil.rmtree(manga_dir)
        await pablo.delete()



@Client.on_callback_query(folder_filter)
async def _folder(bot, callback_query):
    update = callback_query.message.reply_to_message
    await callback_query.message.delete()
    url = update.text
    manga_dir = './Manga/'
    if os.path.isdir(manga_dir):
        await update.reply_text('Still processing another manga')
        return
    os.mkdir(manga_dir)
    cmd = f'manga-py {url}'
    pablo = await update.reply_text('Downloading...')
    await run_cmd(cmd)
    count = 0
    d = manga_dir
    for file in glob.glob(f'{manga_dir}*/'):
        for path in os.listdir(file):
            if os.path.isfile(os.path.join(file, path)):
                count += 1
        if int(count) == 0:
            await pablo.edit_text("Process Stopped. can't download manga url")
            shutil.rmtree(d)
            return
    for file in glob.glob(f'{manga_dir}*/'):
        file_dir = file[8:-1]
        p = Path('.')
        for f in p.glob(f'Manga/{file_dir}/*.zip'):
            with zipfile.ZipFile(f, 'r') as archive:
                archive.extractall(path=f'./Manga/{file_dir}/{f.stem}')
                os.remove(f'./Manga/{file_dir}/{f.stem}/info.txt')
                os.remove(f'./Manga/{file_dir}/{f.stem}.zip')
        shutil.make_archive(file_dir, 'zip', file)
        start_time = time.time()
        await pablo.edit_text('Uploading...')
        await bot.send_document(
            update.chat.id,
            file_dir + '.zip',
            caption=file_dir,
            progress=progress_for_pyrogram,
            progress_args=(
                'Uploading...',
                pablo,
                start_time
            )
        )
        os.remove(file_dir + '.zip')
        shutil.rmtree(manga_dir)
        await pablo.delete()
