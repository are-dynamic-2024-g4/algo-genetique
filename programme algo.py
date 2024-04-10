import pygame
import random
import time

resolution = (800, 600)
window = pygame.display.set_mode(resolution)
NUMBER_OF_MOVES = 10001
size = 10
population_size = 100
speed_x = 15
speed_y = 15
individuals = []
count =0
time_base=0.01
start_time=0
partial_mutation_chance=5
total_mutation_chance=1

def get_random_pos(a, b):
    return random.randint(a, b)


def quitAlgo():
    pygame.quit()
    quit()


class Particle:
    ID = 0

    def __init__(self):
        Particle.ID += 1
        self.size = get_random_pos(5, 15)
        self.color = (255, 255, 255)
        self.ID = Particle.ID
        self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size), get_random_pos(0, resolution[1] - size),
                                 self.size, self.size)
        self.moves = []
        self.speedx = get_random_pos(1, 20)
        self.speedy = get_random_pos(1, 15)
        self.isalive = True
        self.survival_time = 0  # Ajout de la variable de temps de survie

    def ParticleNewGeneration(self,chef1,chef2,parent):
        mutation_value=get_random_pos(0,population_size)
        will_mutate=False
        if mutation_value>partial_mutation_chance:
            self.size=random.choice([parent.size,chef1.size,chef2.size])
            self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size), get_random_pos(0, resolution[1] - size),
                                 self.size, self.size)
            self.speedx=random.choice([parent.speedx,chef1.speedx,chef2.speedx])
            self.speedy=random.choice([parent.speedy,chef1.speedy,chef2.speedy])
        elif mutation_value>total_mutation_chance:
            x=get_random_pos(0,3)
            if x<1:
                self.size = random.choice([parent.size, chef1.size,chef2.size])
                self.rect = pygame.Rect(get_random_pos(0, resolution[0] - size),
                                        get_random_pos(0, resolution[1] - size),
                                        self.size, self.size)
            elif x<2:
                self.speedx = random.choice([parent.speedx, chef1.speedx,chef2.speedy])
            else:
                self.speedy = random.choice([parent.speedy, chef1.speedy,chef2.speedy])

    def move(self):
        if 0 <= self.rect.x + self.moves[count][0] <= resolution[0]:
            self.rect.x += self.moves[count][0]
        else:
            self.rect.x -= self.moves[count][0]
        if 0 <= self.rect.y + self.moves[count][1] <= resolution[1]:
            self.rect.y += self.moves[count][1]
        else:
            self.rect.y -= self.moves[count][1]

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def collide(self, rect1):
        return self.rect.colliderect(rect1)

    def generate_random_moves(self):
        for i in range(NUMBER_OF_MOVES):
            self.moves.append((get_random_pos(-self.speedx, self.speedx), get_random_pos(-self.speedy, self.speedy)))

    def hit(self):
        for i in game.population_mechants:
            if self.collide(i.rect):
                self.isalive = False

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


class Game:
    def __init__(self):
        self.population = []
        self.generation = 1
        self.population_mechants = []

    def generate_mechants(self):
        self.population_mechants = []
        for i in range(population_size // 3):
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

    def draw_particles(self):
        for i in self.population:
            i.hit()
            if i.isalive:
                i.draw()
        for j in self.population_mechants:
            j.draw()

    def move_particles(self):
        for i in self.population:
            i.hit()
            if i.isalive:
                i.move()
                i.update_survival_time()  # Mettre à jour le temps de survie
        for j in self.population_mechants:
            j.move()

    def sort_population(self):
        self.population.sort(key=lambda pop: pop.survival_time,reverse=True)

    def generate_next_population(self):
        children=[]
        self.sort_population()
        chef1=self.population[0]
        chef2=self.population[2]
        children.append(chef1)
        children.append(chef2)
        for parent in self.population[2:]:
            child=Particle()
            child.ParticleNewGeneration(chef1,chef2,parent)
            child.generate_random_moves()
            children.append(child)
        start_time = time.time()

        return children


    def draw_window(self):
        window.fill((0, 0, 0))
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
start_time = time.time()
previous_time=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitAlgo()
    game.move_particles()
    count += 1
    if count >= 10000:
        count = 0
    game.draw_window()
    time.sleep(time_base)

    if game.end_game():
        game.sort_population()
        print(game.population[0].survival_time-previous_time)
        previous_time=game.population[0].survival_time
        game.generate_mechants()
        game.population=game.generate_next_population()

quitAlgo()

