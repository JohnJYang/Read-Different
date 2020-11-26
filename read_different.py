import pygame, sys

def get_list():
    file = input('Please enter a file name (.txt): ')
    f = open(file, 'r')
    lineList = f.readlines()
    f.close()
    dataList = []
    for line in lineList:
        for s in line.split():
            dataList.append(s)
    dataList.append(' ')
    return dataList

def wait_time(word):
    num = len(word)
    if num <= 3:
        return 80
    elif num <= 6:
        return 100
    elif num <= 8:
        return 120
    else:
        return 180
        

text = get_list()

pygame.init()
screen = pygame.display.set_mode((1440, 720))
pygame.display.set_caption('Bearkthem Articles')
clock = pygame.time.Clock()

ind = 0
Run = True
time = 150
word = 360

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Run == False:
                    Run = True
                else:
                    Run = False

            if event.key == pygame.K_UP:
                time -= 10
                word += 30

            if event.key == pygame.K_DOWN:
                time += 10
                word -= 30

            if event.key == pygame.K_n:
                ind = 0
            
        ''' Need to add left and right '''
                
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if Run == False:
        continue
    
    if ind < len(text) - 1:
        
        screen.fill((0, 0, 0))

        rate = pygame.font.Font(None, 50).render('Rate: ' + str(word) + ' (words/min)', True, (200, 200, 200))
        screen.blit(rate, (30, 30))
        
        show = pygame.font.Font('font.ttf', 80).render(text[ind], True, (255, 255, 255))
        rect_show = show.get_rect(center=(1440/2+10, 330))
        screen.blit(show, rect_show)
        
        pygame.display.update()
        pygame.time.delay(time)

        ind += 1
