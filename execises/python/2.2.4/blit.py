import pygame

pygame.init()
image = "hi.png"
pygame.display.set_caption("hello")
screen = pygame.display.set_mode((240,240))

def get_image_size(image):
    img = pygame.image.load(image)
    #print(img.get_rect().size)
    return img.get_rect().size

def paint(func):
    def internal(image, **kargs):
        offset = kargs.get('offset')
        if offset is None:
            offset = (0,0)
        print("------", offset)
        width, height = offset
        print(width, height)
        img = pygame.image.load(image)
        img = func(img, offset=offset)
#        pygame.display.set_icon(img)
        screen.blit(img, (50 + width, 50 + height))
        pygame.display.flip()
    return internal

@paint
def beside(image, **offset):
    return image

@paint
def below(image, height):
    return paint(image, (0, height))

@paint
def flip_vert(img, **kargs):
    return pygame.transform.flip(img, False, True)

@paint
def flip_horiz(img, **kargs):
    return pygame.transform.flip(img, True, False)

if __name__ == '__main__':
    width, height = get_image_size(image)
    running = True
    while running:
        #paint(image)
        beside(image, offset=(width,0))
        below(image, offset=(0,height))
        flip_horiz(image)
        flip_vert(image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False