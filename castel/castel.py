from pygame import *

init()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, player_x, player_y, speed_x, speed_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):

        global jump, jump_count, Down, up

        if Down and not(jump):
            self.rect.y += 5
        
        if  (-10 < self.rect.x < 200) and (50 < self.rect.y < 60):
            Down = False 

        elif (450 < self.rect.x < 700) and (50 < self.rect.y < 60):
            Down = False
        
        elif  (220 < self.rect.x < 440) and (180 < self.rect.y < 190):
            Down = False
        
        elif  (480 < self.rect.x < 625) and (290 < self.rect.y < 300):
            Down = False 

        elif  (220 < self.rect.x < 440) and (390 < self.rect.y < 400):
            Down = False 

        elif  (90 < self.rect.x < 235) and (425 < self.rect.y < 435):
            Down = False 

        elif  (-20 < self.rect.x < 125) and (500 < self.rect.y < 510):
            Down = False
        
        else:
            Down = True
        
        
        if  (-10 < self.rect.x < 200) and (170 < self.rect.y < 180):
            up = False 

        elif (450 < self.rect.x < 700) and (170 < self.rect.y < 180):
            up = False
        
        elif  (220 < self.rect.x < 440) and (300 < self.rect.y < 310):
            up = False
        
        elif  (480 < self.rect.x < 625) and (410 < self.rect.y < 420):
            up = False 

        elif  (220 < self.rect.x < 440) and (510 < self.rect.y < 520):
            up = False 

        elif  (90 < self.rect.x < 235) and (545 < self.rect.y < 555):
            up = False 

        elif  (-20 < self.rect.x < 125) and (620 < self.rect.y < 630):
            up = False
        
        else:
            up = True
        
        key_pressed = key.get_pressed()
        
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed_x
            self.image = transform.scale(image.load('knight_l.png'), (90, 90))

        if key_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed_x
            self.image = transform.scale(image.load('knight_r.png'), (80, 80))
        
        
       #if key_pressed[K_UP] and up:
       #    self.rect.y -= self.speed_y
       #
       #if key_pressed[K_DOWN]:
       #    self.rect.y += self.speed_y
    
        if not jump:
            if key_pressed[K_SPACE]:
                jump = True
               
        else:
            if jump_count >= -9:
                if up and jump_count > 0 :
                    self.rect.y -= (jump_count ** 2) / 2
                    
                else:
                    if not(Down):
                        self.rect.y += (jump_count ** 2) / 2
                     
                jump_count -= 1
            else:
                jump = False
                
                jump_count = 9
        
        
          

class World():
    def __init__(self, data):

        global plathorms
        
        self.tile_list = []
        
        plathorm_img = image.load('platforma.png')
        row_count =  0
        
        for row in data:
            col_count = - 150
            for tile in row:
                if tile == 1:
                    
                    img = transform.scale(plathorm_img, (tile_size_x, tile_size_y))
                    img_rect = img.get_rect() 
                    img_rect.x = col_count + 150
                    img_rect.y = row_count + 100
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    

                col_count += 100
            row_count += 125

    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])
    
class Enemy(GameSprite):
    
    def update(self):
        global go1, go2
        
        if go1:
            self.image = transform.scale(image.load('enemy_right.png'), (80, 80))
            if self.rect.x <= 120:
                self.rect.x += self.speed_x
            else:
                go1 = False
                go2 = True
            
        if go2:
            self.image = transform.scale(image.load('enemy_left.png'), (80, 80))
            if self.rect.x >= 0:
                self.rect.x -= self.speed_x
            else:
                go2 = False
                go1 = True
            

window = display.set_mode((700, 650))
display.set_caption('Castel')

move = True
jump = False
jump_count = 9
Down = True
up = True
go1 = True
go2 = False
tile_size_x = 125
tile_size_y = 100

background = transform.scale(image.load('background.png'), (700, 650))

font.init()
font1 = font.Font(None, 30)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (255, 0, 0))

count_keys = 0
count = font1.render('Ключи: ' + str(count_keys), True, (255, 215, 0))

mixer.music.load('CampainMusic02.mp3')
mixer.music.play()

#fire = mixer.Sound('fire.ogg')
clock = time.Clock()

player = Player('knight_r.png', 20, 500, 6, 6, 80, 80)
princess = GameSprite('princess.png', 600, 25, 0, 0, 100, 100)
prison = GameSprite('prison.png', 605, 25, 0, 0, 100, 100)
enemy1 = Enemy('enemy_right.png', 0, 50, 3, 3, 50, 50)
princesses = sprite.Group()
princesses.add(princess)

prisons = sprite.Group()
prisons.add(prison)

enemys = sprite.Group()
enemys.add(enemy1)

keys = sprite.Group()
key1 = GameSprite('key.png',150, 25, 0, 0, 100, 100)
key2 = GameSprite('key.png',120, 400, 0, 0, 100, 100)
key3 = GameSprite('key.png',550, 270, 0, 0, 100, 100)

keys.add(key1)
keys.add(key2)
keys.add(key3)

plathorms = sprite.Group()
plathorma1 = GameSprite('platforma.png', 0, 100, 0, 0, 250, 100)
plathorma2 = GameSprite('platforma.png', 470, 100, 0, 0, 250, 100)
plathorma3 = GameSprite('platforma.png', 240, 240, 0, 0, 250, 100)
plathorma4 = GameSprite('platforma.png', 530, 340, 0, 0, 125, 100)
plathorma5 = GameSprite('platforma.png', 240, 440, 0, 0, 250, 100)
plathorma6 = GameSprite('platforma.png', 110, 475, 0, 0, 125, 100)
plathorma7 = GameSprite('platforma.png', 0, 550, 0, 0, 125, 100)
plathorma8 = GameSprite('platforma.png', 480, 800, 0, 0, 125, 100)

plathorms.add(plathorma1)
plathorms.add(plathorma2)
plathorms.add(plathorma3)
plathorms.add(plathorma4)
plathorms.add(plathorma5)
plathorms.add(plathorma6)
plathorms.add(plathorma7)
plathorms.add(plathorma8)

world_data = [
[1, 1, 0, 0, 0, 1, 1],
[0, 0, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0],
 ] 

world = World(world_data)
keys_list1 = list()
prison_list1 = list()
princess_list1 = list()
enemy_list1 = list()
count = 0
win1 = False
win2 = False
lose1 = False
run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        
     
    if finish != True: 
        window.blit(background,(0, 0))

        #world.draw()
        princess.reset()
        
        keys.draw(window)
        plathorms.draw(window)
        prisons.draw(window)

        player.reset()
        enemy1.reset()
        
        keys.update()
        plathorms.update()
        prisons.update()
        player.update()
        enemy1.update()

        keys_list = sprite.spritecollide(player, keys, True)
        keys_list2 = keys_list
        if len(keys_list2) - len(keys_list1) >=1:
            count += 1
        keys_list1 = keys_list2

        enemy_list = sprite.spritecollide(player, enemys, False)
        enemy_list2 = enemy_list
        if len(enemy_list2) - len(enemy_list1) >= 1:
            lose1 = True
        enemy_list1 = enemy_list2

        if count == 3:
            prison.kill()
           #prison_list = sprite.spritecollide(player, prisons, True)
           #prison_list2 = prison_list
           #if len(prison_list2) - len(prison_list1) >=1:
           #    prison.kill()
           #    win1 = True
           #prison_list1 = prison_list2
            
        if count == 3:
            princess_list = sprite.spritecollide(player, princesses, True)
            princess_list2 = princess_list
            if len(princess_list2) - len(princess_list1) >=1:
                win2 = True
            princess_list1 = princess_list2

        if count == 3 and win2:
            window.blit(win, (220, 300))
            finish = True
        
        if player.rect.y >= 650 or lose1:
            window.blit(lose, (200, 300))
            finish = True

    clock.tick(60)
    display.update() 