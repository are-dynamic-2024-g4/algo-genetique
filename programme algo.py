import pygame
import random
import time
import math

resolution = (1400, 760)
window = pygame.display.set_mode(resolution)
NUMBER_OF_MOVES = 10001
size = 35
population_size = 100
speed_x = 15
speed_y = 15
individuals = []
count =0
time_base=0.01
start_time=0
partial_mutation_chance=55
total_mutation_chance=15
background=pygame.image.load("background.png").convert()
pygame.display.set_caption('Simulation Algorithme Génétique')


def get_random_pos(a, b):
    return random.randint(a, b)


def quitAlgo():
    pygame.quit()
    quit()

def calculdistance (coor1,coor2):
    return math.sqrt((coor2[0]-coor1[0])**2+(coor2[1]-coor1[0])**2)




class Particle:
    ID = 0

    def __init__(self):
        Particle.ID += 1
        self.size = get_random_pos(3, 28+game.generationNum)
        self.color = (255, 255, 255)
        self.ID = Particle.ID
        self.image=pygame.image.load("images.png").convert_alpha()
        self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size), get_random_pos(0, resolution[1] - size),
                                 self.size, self.size)
        self.moves = []
        self.speedx = get_random_pos(1, 25+game.generationNum)
        self.speedy = get_random_pos(1, 18+game.generationNum)
        self.isalive = True
        self.survival_time = 0  # Ajout de la variable de temps de survie
        self.timeleft=get_random_pos(5,30+game.generationNum)
        self.intelligence=get_random_pos(0,100+game.generationNum)
        self.hunger=get_random_pos(0,self.timeleft)
        self.critical=get_random_pos(0,self.timeleft//2)
        self.visionradius=get_random_pos(0,300+game.generationNum*5)

    def ParticleNewGeneration(self,chef1,chef2,parent):
        mutation_value=get_random_pos(0,100)
        if mutation_value>total_mutation_chance:
            self.size=random.choice([parent.size,chef1.size,chef2.size])
            self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size), get_random_pos(0, resolution[1] - size), self.size, self.size)
            self.speedx=random.choice([parent.speedx,chef1.speedx,chef2.speedx])
            self.speedy=random.choice([parent.speedy,chef1.speedy,chef2.speedy])
            self.timeleft=random.choice([parent.timeleft,chef1.timeleft,chef2.timeleft])
            self.intelligence=random.choice([parent.intelligence,chef1.intelligence,chef2.intelligence])
            self.visionradius=random.choice([parent.visionradius,chef1.visionradius,chef2.visionradius])
            self.hunger=random.choice([parent.hunger,chef1.hunger,chef2.hunger])
            self.critical=random.choice([parent.critical,chef1.critical,chef2.critical])
        if partial_mutation_chance>=mutation_value>total_mutation_chance :
            x=get_random_pos(0,7)
            if x<1:
                self.size = get_random_pos(3, 28+game.generationNum)
                self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size),
                                        get_random_pos(0, resolution[1] - size),
                                        self.size, self.size)
            elif x<2:
                self.speedx = get_random_pos(1, 25+game.generationNum)
            elif x<3:
                self.timeleft=get_random_pos(5, 30+game.generationNum)
            elif x<4:
                self.visionradius=get_random_pos(0, 300+game.generationNum*5)
            elif x<5:
                self.intelligence=get_random_pos(0,100+game.generationNum)
            elif x<6:
                self.speedy = get_random_pos(1, 18+game.generationNum)
            elif x<7:
                self.hunger=get_random_pos(0,self.timeleft)
            else:
                self.critical=get_random_pos(0,self.timeleft//2)
    def move(self):
        danger=False
        j=0
        oldcoor=(self.rect.x,self.rect.y)
        newcoor=(self.rect.x,self.rect.y)
        ennemy=0
        movex=self.moves[count][0]
        movey=self.moves[count][1]
        luck=get_random_pos(0,100)
        hungry=False
        closest=-1
        closestindex=-1
        criticalstate=False
        currentvision=self.visionradius
        counst=200

        if(self.timeleft<=self.critical ):
            criticalstate=True
        elif(self.timeleft<=self.hunger):
            hungry=True
        while (j < len(game.population_mechants) and (not danger) and (not criticalstate)):
            if calculdistance(oldcoor,(game.population_mechants[j].rect.x,game.population_mechants[j].rect.y))<=self.visionradius:
                danger=True
                ennemy=j
            j=j+1

        if criticalstate:
            currentvision=currentvision*2
        if (danger and (luck<=self.intelligence) and (not criticalstate)):
            while (calculdistance(newcoor,(game.population_mechants[ennemy].rect.x,game.population_mechants[ennemy].rect.y))<=calculdistance(oldcoor,(game.population_mechants[ennemy].rect.x,game.population_mechants[ennemy].rect.y))):
                movex=get_random_pos(-self.speedx, self.speedx)
                movey=get_random_pos(-self.speedy, self.speedy)
                newcoor=(movex+self.rect.x, movey+self.rect.y)
        elif(hungry or criticalstate):

            found=False
            k=0
            toeat=-1
            while ((not found) and k<len(game.nourriture)):
                if((calculdistance((game.nourriture[k].rect.x,game.nourriture[k].rect.y),oldcoor)<=currentvision) and (game.nourriture[k].isalive)):
                    found=True
                    toeat=k
                k=k+1
            if (found):
                while (calculdistance(newcoor,(game.nourriture[toeat].rect.x,game.nourriture[toeat].rect.y))>=calculdistance(oldcoor,(game.nourriture[toeat].rect.x,game.nourriture[toeat].rect.y)) and counst>0):
                    movex=get_random_pos(-self.speedx, self.speedx)
                    movey=get_random_pos(-self.speedy, self.speedy)
                    newcoor=(movex+self.rect.x, movey+self.rect.y)
                    counst-=1

        if 0 <= self.rect.x + movex<= resolution[0]:
            self.rect.x += movex
        else:
            self.rect.x -= movex
        if 0 <= self.rect.y + movey <= resolution[1]:
            self.rect.y += movey
        else:
            self.rect.y -= movey

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def collide(self, rect1):
        return self.rect.colliderect(rect1)

    def generate_random_moves(self):
        for i in range(NUMBER_OF_MOVES):
            self.moves.append((get_random_pos(-self.speedx, self.speedx), get_random_pos(-self.speedy, self.speedy)))

    def hit(self):
        if self.isalive==True:
            for i in game.population_mechants:
                if self.collide(i.rect):
                    self.isalive = False
            for j in game.nourriture:
                if self.collide(j.rect) and (j.isalive==True):
                    j.isalive=False
                    self.timeleft+=10

    def timeover(self):
        if (self.timeleft-self.survival_time)<=0 and self.isalive:
            self.isalive=False

    def update_survival_time(self):  # Méthode pour mettre à jour le temps de survie
        if self.isalive:
            self.survival_time =time.time() -start_time


class ParticleMechant:
    ID = 0

    def __init__(self, rect):
        Particle.ID -= 1
        self.color = (255, 0, 0)
        self.ID = Particle.ID
        self.rect = rect
        self.image=pygame.image.load("mechant.png").convert_alpha()
        self.moves = []

    def move(self):
        if 0 <= self.rect.x + self.moves[count][0] <= resolution[0]:
            self.rect.x += self.moves[count][0]
        if 0 <= self.rect.y + self.moves[count][1] <= resolution[1]:
            self.rect.y += self.moves[count][1]

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def collide(self, rect1):
        return self.rect.colliderect(rect1)

    def generate_random_moves(self):
        for i in range(NUMBER_OF_MOVES):
            self.moves.append((get_random_pos(-speed_x, speed_x), get_random_pos(-speed_y, speed_y)))




class nourriture:
    def __init__(self):
        self.color = (0, 200, 0)
        self.size=22
        self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size), get_random_pos(0, resolution[1] - size),
                                 self.size, self.size)
        self.image=pygame.image.load("carotte.png").convert_alpha()
        self.isalive = True

class Game:
    generationNum=0
    def __init__(self):
        self.population = []
        self.generation = 1
        self.population_mechants = []
        self.nourriture=[]
        self.foodTimer=time.time()


    def generate_mechants(self):
        self.population_mechants = []
        for i in range(population_size // 4):
            self.population_mechants.append(
                ParticleMechant(pygame.Rect(get_random_pos(0, resolution[0] - size),
                                             get_random_pos(0, resolution[1] - size), size, size)))
        for j in self.population_mechants:
            j.generate_random_moves()

    def generate_first_population(self):
        for i in range(population_size):
            self.population.append(Particle())
        for j in self.population:
            j.generate_random_moves()
        return self.population

    def generate_nourriture(self):
        self.nourriture=[]
        for i in range(population_size//5):
            self.nourriture.append(nourriture())

    def draw_particles(self):
        for i in self.population:
            if i.isalive:
                i.hit()
                i.timeover()
            if i.isalive:
                window.blit(pygame.transform.scale(i.image,(i.size*1.49,i.size*1.49)),i.rect)
        for j in self.population_mechants:
            window.blit(pygame.transform.scale(j.image, (size, size)), j.rect)
        for k in self.nourriture:
            if k.isalive:
                window.blit(pygame.transform.scale(k.image, (k.size, k.size)), k.rect)

    def move_particles(self):
        for i in self.population:
            if i.isalive:
                i.hit()
                i.timeover()
            if i.isalive:
                i.move()
                i.update_survival_time()  # Mettre à jour le temps de survie
        for j in self.population_mechants:
            j.move()
        if time.time()-self.foodTimer>=3:
            self.nourriture.append(nourriture())
            self.foodTimer=time.time()

    def sort_population(self):
        self.population.sort(key=lambda pop: pop.survival_time,reverse=True)

    def generate_next_population(self):
        children=[]
        self.generationNum+=1
        self.sort_population()
        chef1=self.population[0]
        chef1.survival_time=0
        chef2=self.population[2]
        chef2.survival_time=0
        children.append(chef1)
        children.append(chef2)
        for parent in self.population[2:]:
            child=Particle()
            child.ParticleNewGeneration(chef1,chef2,parent)
            child.generate_random_moves()
            children.append(child)
        return children


    def draw_window(self):
        window.fill((0, 0, 0))
        window.blit(pygame.transform.scale(background,(1920,1080)), (0, 0))

        self.draw_particles()
        pygame.display.update()

    def end_game(self):
        for i in self.population:
            if i.isalive:
                return False
        return True


game = Game()
game.generate_first_population()
game.generate_mechants()
game.generate_nourriture()
start_time = time.time()
previous_time=0
game.foodTimer=time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitAlgo()
    game.move_particles()
    count += 1
    if count >= 10000:
        count = 0
    game.draw_window()
    time.sleep(0.01)

    if game.end_game():
        game.sort_population()
        print(game.population[0].survival_time)
        print(game.population[0].visionradius)
        print(game.population[0].intelligence)
        print(game.population[0].hunger)
        print(game.population[0].critical)
        game.generate_mechants()
        game.generate_nourriture()
        game.population = game.generate_next_population()
        start_time=time.time()
quitAlgo()
