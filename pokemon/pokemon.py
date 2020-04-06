from enum import Enum

effectiveness = [
                    [0.5, 0.5, 2],
                    [2, 0.5, 0.5],
                    [0.5, 2, 0.5]
]

class PokemonType(Enum):
    Fire = 0
    Water = 1
    Grass = 2

class Trainer:
    
    def __init__(self, name, pokemon, active_pokemon):
        self.name = name
        self.pokemon = []
        self.inventory = []

        for pok in pokemon:
            self.pokemon.append(pok)
        
        self.set_active_pokemon(active_pokemon)

    def use_potion(self, pokemon):
        potion_hp = 10
        print("{} used potion on {}".format(self.name, pokemon.name))
        pokemon.update_health(potion_hp)
    
    def set_active_pokemon(self, active_pokemon):

        def choose_pokemon(self):
            print("Please choose an active pokemon:")
            for pok in self.pokemon:
                print(pok.name)
            active_pokemon_str = input("Type pokemon's name:")
            active_pokemon = None

            for pokemon in self.pokemon:
                if active_pokemon_str == pokemon.name:
                    active_pokemon = pokemon
                    break
            return active_pokemon

        if active_pokemon in self.pokemon:
            if active_pokemon.is_knocked_out == True:
                print("{} is knocked out.".format(active_pokemon.name))
                active_pokemon = choose_pokemon(self)
                self.set_active_pokemon(active_pokemon)
            else:
                self.active_pokemon = active_pokemon
                print("{} is now {}'s active pokemon.".format(active_pokemon.name, self.name))
        else:
            print("{} has not {}".format(self.name, active_pokemon.name))
            
            self.set_active_pokemon(choose_pokemon(self))

    def attack_trainer(self, enemy_trainer):
        print("{} is attacking {}!".format(self.name, enemy_trainer.name))
        self.active_pokemon.attack(enemy_trainer.active_pokemon)
            

class Pokemon:
    def __init__(self, name, level, pok_type, health, max_health, is_knocked_out):
        self.experience = 0
        self.name = name
        self.level = level
        self.type = pok_type
        self.health = health
        self.max_health = max_health
        self.is_knocked_out = is_knocked_out

    def update_health(self, hp):
        if self.health + hp <= self.max_health:
            self.health += hp
            print("{} now has {} health.".format(self.name, self.health))
        else:
            self.health = self.max_health
            print("{} is at maximum health {}".format(self.name, self.max_health))
        self.knock_out()

    def knock_out(self):
        if self.health < 0:
            self.is_knocked_out = True
            print("{} is knocked out!".format(self.name))

    def revive(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            print("{} is back!".format(self.name))    

    def attack(self, rival):
        if self.is_knocked_out:
            print("{} is knocked out. Can't attack.")
        else:
            attack_modifier = effectiveness[self.type.value][rival.type.value]
            damage = self.level*attack_modifier
            
            print("{} dealt {} damage to {}.".format(self.name, damage, rival.name))

            rival.update_health(-damage)
    
    def increase_xp(self, enemy_pokemon):
        if enemy_pokemon.is_knocked_out == True:
            self.experience += enemy_pokemon.level*3

            self.level_up()
    
    def level_up(self):
        if self.experience >= 100:
            self.level += 1
            print("{} has leveled up. {} is now at level {}.".format(self.name, self.name, self.level))
            self.experience -= 100

charmander = Pokemon("Charmander", 3, PokemonType.Fire, 20, 20, False)
bulbasaur = Pokemon("Bulbasaur", 2, PokemonType.Grass, 25, 25, False)
squirtle = Pokemon("Squirtle", 1, PokemonType.Water, 30, 30, False)
poliwag = Pokemon("Poliwag", 2, PokemonType.Water, 15, 15, False)
ponyta = Pokemon("Ponyta", 2, PokemonType.Fire, 18, 18, False)
chikorita = Pokemon("Chikorita", 3, PokemonType.Grass, 14, 14, False)

ash = Trainer("Ash", [charmander, poliwag], charmander)
brock = Trainer("Brock", [ponyta, bulbasaur], ponyta)

ash.attack_trainer(brock)
brock.attack_trainer(ash)

ash.set_active_pokemon(poliwag)
ash.attack_trainer(brock)

brock.set_active_pokemon(squirtle)

print()