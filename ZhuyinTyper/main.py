import asyncio
import pygame
import random
import os

WIDTH, HEIGHT = 600, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTER = (WIDTH / 2 - 64, HEIGHT / 2 - 64)
BACKGROUND_COLOR = (255, 255, 255)
USER_CHOICE_DISPLAY_LOCATION = (5, 5)
USER_CHOICE_IMG_DIM = (32, 32)

zhuyin_key_mapping = {pygame.K_1: 'b', pygame.K_q: 'p', pygame.K_a: 'm', pygame.K_z: 'f',
                      pygame.K_2: 'd', pygame.K_w: 't', pygame.K_s: 'n', pygame.K_x: 'l',
                      pygame.K_3: '3t', pygame.K_e: 'g', pygame.K_d: 'k', pygame.K_c: 'h',
                      pygame.K_4: '4t', pygame.K_r: 'j', pygame.K_f: 'q', pygame.K_v: 'x',
                      pygame.K_5: 'zh', pygame.K_t: 'ch', pygame.K_g: 'sh', pygame.K_b: 'r',
                      pygame.K_6: '2t', pygame.K_y: 'z', pygame.K_h: 'c', pygame.K_n: 's',
                      pygame.K_7: '5t', pygame.K_u: 'yi', pygame.K_j: 'wu', pygame.K_m: 'yu',
                      pygame.K_8: 'a', pygame.K_i: 'o', pygame.K_k: 'e', pygame.K_COMMA: 'ye',
                      pygame.K_9: 'ai', pygame.K_o: 'ei', pygame.K_l: 'ao', pygame.K_PERIOD: 'ou',
                      pygame.K_0: 'an', pygame.K_p: 'en', pygame.K_SEMICOLON: 'ang', pygame.K_SLASH: 'eng',
                      pygame.K_MINUS: 'er', pygame.K_SPACE: '1t'}

zhuyin_symbols = ['b', 'p', 'm', 'f',
                  'd', 't', 'n', 'l',
                  '3t', 'g', 'k', 'h',
                  '4t', 'j', 'q', 'x',
                  'zh', 'ch', 'sh', 'r',
                  '2t', 'z', 'c', 's',
                  '5t', 'yi', 'wu', 'yu',
                  'a', 'o', 'e', 'ye',
                  'ai', 'ei', 'ao', 'ou',
                  'an', 'en', 'ang', 'eng',
                  'er', '1t']

zhuyin_img_map = {}
small_zhuyin_img_map = {}


pygame.display.set_caption("Zhuyin Typer")
logo_icon = pygame.image.load("assets/favicon.png")
pygame.display.set_icon(logo_icon)


def load_zhuyin_image(name):
    return pygame.image.load(os.path.join('assets', name + '.png'))


def load_maps():
    for name in zhuyin_symbols:
        zhuyin_img_map[name] = load_zhuyin_image(name)
        small_zhuyin_img_map[name] = pygame.transform.scale(zhuyin_img_map[name], USER_CHOICE_IMG_DIM)


def draw_window(random_symbol_img, user_choice_img):
    WIN.fill(BACKGROUND_COLOR)

    WIN.blit(random_symbol_img, CENTER)

    if user_choice_img is not None:
        WIN.blit(user_choice_img, USER_CHOICE_DISPLAY_LOCATION)

    pygame.display.update()


async def main():
    random_symbol = random.choice(zhuyin_symbols)

    user_choice = None
    previous_choice = None

    running = True
    updated = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = event.key

                selected_symbol = zhuyin_key_mapping.get(key, None)

                if selected_symbol == random_symbol:
                    random_symbol = random.choice(zhuyin_symbols)
                    updated = True
                if selected_symbol is not None and selected_symbol != previous_choice:
                    user_choice = selected_symbol
                    previous_choice = user_choice
                    updated = True

        if updated:
            random_symbol_img = zhuyin_img_map[random_symbol]
            user_choice_img = small_zhuyin_img_map.get(user_choice, None)

            draw_window(random_symbol_img, user_choice_img)
            updated = False

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    load_maps()
    asyncio.run(main())
