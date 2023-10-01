from pico2d import *
import random

open_canvas(1280, 1080)

TUK_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

points = [(random.randint(0, 1280), random.randint(0, 1080)) for i in range(10)]

running = True

while running:
    def draw_line(p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        frame = 0  # frame 변수 초기화

        for i in range(0, 100 + 1, 4):
            t = i / 100
            x = int((1 - t) * x1 + t * x2)
            y = int((1 - t) * y1 + t * y2)

            clear_canvas()
            TUK_ground.draw(1280 // 2, 1080 // 2)

            if x1 > x2:
                character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 200, 200)
            else:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y, 200, 200)

            hand_arrow.draw(x2, y2)

            update_canvas()
            frame = (frame + 1) % 8

            delay(0.02)


    for i in range(0, len(points) - 1):
        draw_line(points[i], points[i + 1])
    draw_line(points[-1], points[0])

    handle_events()

close_canvas()