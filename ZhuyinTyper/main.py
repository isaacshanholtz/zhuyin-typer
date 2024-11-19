import asyncio
import pygame
import random
import os
import time

WIDTH, HEIGHT = 600, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTER = (WIDTH / 2 - 64, HEIGHT / 2 - 64)
BACKGROUND_COLOR = (255, 255, 255)
USER_CHOICE_DISPLAY_LOCATION = (5, 5)
USER_CHOICE_IMG_DIM = (32, 32)

zhuyin_key_mapping = {pygame.K_1: 'ㄅ', pygame.K_q: 'ㄆ', pygame.K_a: 'ㄇ', pygame.K_z: 'ㄈ',
                      pygame.K_2: 'ㄉ', pygame.K_w: 'ㄊ', pygame.K_s: 'ㄋ', pygame.K_x: 'ㄌ',
                      pygame.K_3: 'ˇ', pygame.K_e: 'ㄍ', pygame.K_d: 'ㄎ', pygame.K_c: 'ㄏ',
                      pygame.K_4: 'ˋ', pygame.K_r: 'ㄐ', pygame.K_f: 'ㄑ', pygame.K_v: 'ㄒ',
                      pygame.K_5: 'ㄓ', pygame.K_t: 'ㄔ', pygame.K_g: 'ㄕ', pygame.K_b: 'ㄖ',
                      pygame.K_6: 'ˊ', pygame.K_y: 'ㄗ', pygame.K_h: 'ㄘ', pygame.K_n: 'ㄙ',
                      pygame.K_7: '·', pygame.K_u: 'ㄧ', pygame.K_j: 'ㄨ', pygame.K_m: 'ㄩ',
                      pygame.K_8: 'ㄚ', pygame.K_i: 'ㄛ', pygame.K_k: 'ㄜ', pygame.K_COMMA: 'ㄝ',
                      pygame.K_9: 'ㄞ', pygame.K_o: 'ㄟ', pygame.K_l: 'ㄠ', pygame.K_PERIOD: 'ㄡ',
                      pygame.K_0: 'ㄢ', pygame.K_p: 'ㄣ', pygame.K_SEMICOLON: 'ㄤ', pygame.K_SLASH: 'ㄥ',
                      pygame.K_MINUS: 'ㄦ'}

zhuyin_symbols = ['ㄅ', 'ㄆ', 'ㄇ', 'ㄈ',
                  'ㄉ', 'ㄊ', 'ㄋ', 'ㄌ',
                  'ˇ', 'ㄍ', 'ㄎ', 'ㄏ',
                  'ˋ', 'ㄐ', 'ㄑ', 'ㄒ',
                  'ㄓ', 'ㄔ', 'ㄕ', 'ㄖ',
                  'ˊ', 'ㄗ', 'ㄘ', 'ㄙ',
                  '·', 'ㄧ', 'ㄨ', 'ㄩ',
                  'ㄚ', 'ㄛ', 'ㄜ', 'ㄝ',
                  'ㄞ', 'ㄟ', 'ㄠ', 'ㄡ',
                  'ㄢ', 'ㄣ', 'ㄤ', 'ㄥ',
                  'ㄦ']

zhuyin_img_map = {}
small_zhuyin_img_map = {}

pygame.init()
pygame.font.init()
zh_font = pygame.font.SysFont('youyuan', 70)

pygame.display.set_caption("Zhuyin Typer")
logo_icon = pygame.image.load("assets/favicon.png")
pygame.display.set_icon(logo_icon)


def load_zhuyin_image(name):
    return pygame.image.load(os.path.join('assets', name + '.png'))


def draw_window(random_symbol, user_choice):
    WIN.fill(BACKGROUND_COLOR)
    rs_surface = zh_font.render(random_symbol, True, (0, 0, 0))

    WIN.blit(rs_surface, CENTER)

    if user_choice is not None:
        uc_surface = zh_font.render(user_choice, True, (0, 0, 0))
        WIN.blit(uc_surface, USER_CHOICE_DISPLAY_LOCATION)

    pygame.display.update()


async def main():
    random.seed(time.time())

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
            draw_window(random_symbol, user_choice)
            updated = False

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())
