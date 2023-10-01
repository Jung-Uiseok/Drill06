from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    global click_positions

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_positions.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
click_positions = []
hide_cursor()

while running:

    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, TUK_WIDTH // 2, TUK_HEIGHT // 2, 200, 200)

    for cl_x, cl_y in click_positions:
        hand_arrow.draw(cl_x, cl_y)

    hand_arrow.draw(x,y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()