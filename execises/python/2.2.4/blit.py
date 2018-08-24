import pygame

pygame.init()
image = "hi.png"
pygame.display.set_caption("hello")
screen = pygame.display.set_mode((240,240))

def get_image_size(image):
    img = pygame.image.load(image)
    #print(img.get_rect().size)
    return img.get_rect().size

def base(func):
    def internal(image, **kargs):
        img = pygame.image.load(image)  # returns Surface
        screen.blit(img, (0,0))
        surf = func(img)

        print(surf.get_rect().size)

    return internal

@base
def beside(img):
    topright = img.get_rect().topright
    new_image = img.copy()
    screen.blit(new_image, topright)
    width, height = img.get_rect().size
    return pygame.Surface((2 * width, height))


@base
def below(img):
    bottomleft = img.get_rect().bottomleft
    new_image = img.copy()
    screen.blit(new_image, bottomleft)
    width, height = img.get_rect().size
    return pygame.Surface((width, height * 2))

@base
def flip_vert(img):
    return pygame.transform.flip(img, False, True)

@base
def flip_horiz(img):
    return pygame.transform.flip(img, True, False)

if __name__ == '__main__':
    running = True
    while running:
        beside(image)
        below(image)
        flip_horiz(image)
        flip_vert(image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()