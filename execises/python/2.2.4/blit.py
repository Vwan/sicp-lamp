import pygame

pygame.init()
image = "hi.png"
pygame.display.set_caption("hello")
screen = pygame.display.set_mode((240,240))

def get_image_size(image):
    img = pygame.image.load(image)
    print(img.get_rect().size)
    return img.get_rect().size

def paint(image, offset=(0,0)):
    width, height = offset
    img = pygame.image.load(image)
    pygame.display.set_icon(img)
    screen.blit(img, (50+width,50+height))
    pygame.display.flip()

def beside(image, width):
    paint(image)
    paint(image, (width, 0))

if __name__ == '__main__':
    width, height = get_image_size(image)
    running = True
    while running:
        #paint(image)
        beside(image, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False