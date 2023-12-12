import pygame


def initial():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def get_keyboard(keyboardnName):
    answer = False
    for eve in pygame.event.get():
        pass
    keyboardInput = pygame.key.get_pressed()
    myKeyboard = getattr(pygame, 'K_{}'.format(keyboardnName))

    if keyboardInput[myKeyboard]:
        answer = True
    pygame.display.update()

    return answer


def main():
    if get_keyboard('LEFT'):
        print('Left key pressed')

    elif get_keyboard('RIGHT'):
        print('Right key pressed')


if __name__ == '__main__':
    initial()
    while True:
        main()

