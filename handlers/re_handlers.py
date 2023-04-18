import requests as req
import random

from aiogram import Router, F, types

from aiogram.utils.markdown import hide_link

from dictionary.replies import replies, answer_for_roma
from filters import re_functions
from config_data.config import load_config, Config

router: Router = Router()

config: Config = load_config()
ggl_api_key: str = config.api_config.google_api


@router.message(F.text, re_functions.net_otvet_filter)
async def net_otvet(message: types.Message) -> None:
    net = message.text
    if net[-1].lower() in ['t', 'т']:
        await message.reply(f"{replies['net']}")
    else:
        for i in range(1, len(net) + 1):
            if net[-i].lower() in ['t', 'т']:
                await message.reply(f"{replies['net']}{net[-i + 1:]}")
                break


@router.message(F.text, re_functions.nit_otvet_filter)
async def nit_otvet(message: types.Message) -> None:
    nit = message.text
    if nit[-1].lower() in ['t', 'т']:
        await message.reply(f"{replies['nit']}")
    else:
        for i in range(1, len(nit) + 1):
            if nit[-i].lower() in ['t', 'т']:
                await message.reply(f"{replies['nit']}{nit[-i + 1:]}")
                break


@router.message(F.text, re_functions.no_otvet_filter)
async def no_otvet(message: types.Message) -> None:
    no = message.text
    if no[-1].lower() in ['o', 'у']:
        await message.reply(f"{replies['no']}")
    else:
        for i in range(1, len(no) + 1):
            if no[-i].lower() in ['o', 'у']:
                await message.reply(f"{replies['no']}{no[-i + 1:]}")
                break


@router.message(F.text, re_functions.nope_otvet_filter)
async def nope_otvet(message: types.Message) -> None:
    nope = message.text
    if nope[-1].lower() in ['п', 'e']:
        await message.reply(f"{replies['nope']}")
    else:
        for i in range(1, len(nope) + 1):
            if nope[-i].lower() in ['п', 'e']:
                await message.reply(f"{replies['nope']}{nope[-i + 1:]}")
                break


@router.message(F.text, re_functions.nein_otvet_filter)
async def nein_otvet(message: types.Message) -> None:
    nein = message.text
    if nein[-1].lower() in ['n', 'н']:
        await message.reply(f"{replies['nein']}")
    else:
        for i in range(1, len(nein) + 1):
            if nein[-i].lower() in ['n', 'н']:
                await message.reply(f"{replies['nein']}{nein[-i + 1:]}")
                break


@router.message(F.text, re_functions.yes_otvet_filter)
async def yes_otvet(message: types.Message) -> None:
    yes = message.text
    if yes[-1].lower() in ['с', 's']:
        await message.reply(f"{replies['yes']}")
    else:
        for i in range(1, len(yes) + 1):
            if yes[-i].lower() in ['с', 's']:
                await message.reply(f"{replies['yes']}{yes[-i + 1:]}")
                break


@router.message(F.text, re_functions.da_otvet_filter)
async def da_otvet(message: types.Message) -> None:
    ggl_url = f"""https://customsearch.googleapis.com/customsearch/v1?cx=6120d6c5dd8c74814&fileType=jpg&num=10&imgType=clipart&gl=ru&lr=lang_ru&q=старая%20сковорода&searchType=image&siteSearch=free3d.com&siteSearchFilter=e&key={ggl_api_key}"""
    ggl_search_result = req.get(ggl_url).json()
    links_list = []
    for i in range(10):
        links_list.append(ggl_search_result['items'][i]['link'])

    link = random.choice(links_list)

    answer = f"""{hide_link(link)}{replies['da']}"""

    da = message.text
    if da[-1].lower() in ['а', 'a']:
        await message.reply(answer)
    else:
        for i in range(1, len(da) + 1):
            if da[-i].lower() in ['а', 'a']:
                await message.reply(f"{answer}{da[-i + 1:]}")
                break


@router.message(F.text, re_functions.traktorista_otvet_filter)
async def traktorista_otvet(message: types.Message) -> None:
    ggl_url = f"""https://customsearch.googleapis.com/customsearch/v1?cx=6120d6c5dd8c74814&fileType=jpg&num=10&imgType=photo&gl=ru&lr=lang_ru&q=тракторист%20в%20тракторе&searchType=image&siteSearch=free3d.com&siteSearchFilter=e&key={ggl_api_key}"""
    ggl_search_result = req.get(ggl_url).json()
    links_list = []
    for i in range(10):
        links_list.append(ggl_search_result['items'][i]['link'])

    link = random.choice(links_list)

    answer = f"""{hide_link(link)}{replies['300']}"""
    await message.reply(answer)


@router.message(F.text, re_functions.gde_otvet_filter)
async def gde_otvet(message: types.Message) -> None:
    await message.reply(f"{replies['gde']}")


@router.message(F.text, re_functions.nu_otvet_filter)
async def nu_otvet(message: types.Message) -> None:
    await message.reply(f"{replies['nu']}")


@router.message(F.text, re_functions.kto_otvet_filter)
async def kto_otvet(message: types.Message) -> None:
    await message.reply(f"{replies['kto']}")


@router.message(F.from_user.id == 119954087, F.reply_to_message.from_user.id == 6017337446)
async def joke_answer(message: types.Message):
    await message.reply(text=random.choice(answer_for_roma))
