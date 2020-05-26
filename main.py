# -*- coding: utf-8 -*-

import vk_api
import time
import random

settings = {
    'owner_id': '-91518473',
    'login': 'логин',
    'pass': 'пароль',
    'phases': [
        "Приветики, котлетики! Призрак с вами",
        "Нормально",
        "Стоп, это же моя жизнь",
        "хто я",
        "А ну давай",
        "взлом одного места)",
        "Призрак с вами, земля под ногами",
        "Какое замечательное видео",
        "print('Здарова мир!')",
        "Пампарааааам пампараааам",
        "Я злой exe призрак",
        "Хачу призрак exe",
        "ммм... нормально",
        "чердак занят!",
        "рандомная фраза, подходящая по смыслу)",
        "ставь класс если жалко",
        "нет блин призрак",
        "Хы хы хы",
        "А-ха-ха, какая смешная игра (не баньте)",
        "лунтик х кашмар в попi",
        "долбит нормально",
        "я - призрак.exe)",
        "GhostlyBot v2.28 running...",
        "Декарт, поиграй в мою игру, суть такова: Пользователь может играть лесными эльфами, охраной дворца и злодеем. И если пользователь играет эльфами то эльфы в лесу, домики деревяные набигают солдаты дворца и злодеи. Можно грабить корованы... И эльфу раз лесные то сделать так что там густой лес... А движок такой что вдали деревья картинкой, когда подходиш они преобразовываются в 3-хмерные деревья. Можно покупать и т.п. возможности как в Daggerfall. И враги 3-хмерные тоже, и труп тоже 3д. Можно прыгать и т.п. Если играть за охрану дворца то надо слушаться командира, и защищать дворец от злого (имя я не придумал) и шпионов, партизанов эльфов, и ходит на набеги на когото из этих (эльфов, злого...). Ну а если за злого... то значит шпионы или партизаны эльфов иногда нападают, пользователь сам себе командир может делать что сам захочет прикажет своим войскам с ним самим напасть на дворец и пойдет в атаку. Всего в игре 4 зоны. Т.е. карта и на ней есть 4 зоны, 1 - зона людей (нейтрал), 2- зона императора (где дворец), 3-зона эльфов, 4 - зона злого... (в горах, там есть старый форт...)\nТак же в игре можно не только убить но и отрубить руку и если пользователя не вылечат то он умрет, так же выколоть глаз но пользователь может не умереть а просто пол экрана не видеть, или достать или купить протез, если ногу тоже либо умреш либо будеш ползать либо на коляске котаться, или самое хорошее... поставить протез. Сохранятся можно...\n\nP.S. Я джва года хочу летсплей на эту игру.",
        "На попей",
        "оп хаха неловко вышло)",
        "оп хаха Ловко вышло, фигасе"
    ]
}

lastpost_id=31790

f = open("lastpost_id.txt", "r")
lastpost_id = f.read()
f.close()

def GetLastPost(public_id):
    vk_session = vk_api.VkApi(settings['login'], settings['pass'])
    vk_session.auth()
    
    vk = vk_session.get_api()

    return vk.wall.get(owner_id=public_id, count=1)['items'][0]['id']

def PostComment():
    vk_session = vk_api.VkApi(settings['login'], settings['pass'])
    vk_session.auth()
    
    vk = vk_session.get_api()

    if not GetBan(settings['owner_id'][1:len(settings['owner_id'])]):
        PhaseNum = random.randint(0, len(settings['phases'])-1)
        vk.wall.createComment(owner_id=settings['owner_id'], post_id=GetLastPost(settings['owner_id']), message=settings['phases'][PhaseNum])
        print('Написан комментарий к https://vk.com/wall{0}_{1} с текстом {2}'.format(settings['owner_id'], GetLastPost(settings['owner_id']), settings['phases'][PhaseNum]))
    else:
        print('Произошел бан!')

def GetBan(gid):
    vk_session = vk_api.VkApi(settings['login'], settings['pass'])
    vk_session.auth()
    
    vk = vk_session.get_api()

    gtest = vk.groups.getById(group_id=gid, fields='ban_info')[0]

    if 'ban_info' in gtest:
        return True
    else:
        return False



while True:
    if not GetBan(settings['owner_id'][1:len(settings['owner_id'])]):
        if GetLastPost(settings['owner_id']) != lastpost_id:
            print('Новый пост в {} с id {}'.format(settings['owner_id'], GetLastPost(settings['owner_id'])))
            f = open("lastpost_id.txt", "w")
            f.write(lastpost_id)
            f.close()
            PostComment()
            lastpost_id = GetLastPost(settings['owner_id'])
    time.sleep(10 * 60)
