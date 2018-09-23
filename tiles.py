import items, enemies, actions, player, diceroll, world
from random import randint

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()    

class TrapTile(MapTile):
    def __init__(self, x, y, player):
        super().__init__(x, y)
    def modify_player(self, the_player):
        if player.dex < 10:
            print("Make a Dexterity saving roll!")
            DexSave = randint(1, 20)
            print(DexSave)
            if DexSave < 10:
                the_player.hp = the_player.hp - randint(1, 4)
                print("You stepped in a trap! It did {} damage. You have {} HP remaining.".format(diceroll.D4, the_player.hp))
            else:
                print("You spotted a trap and stepped over it.")
        else:
            print("You spotted a trap and stepped over it.")
            
class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class GerblinRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Gerblin())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A gerblin jumps out from behind a rock!
            """
        else:
            return """
            The corpse of a dead gerblin rots on the ground.
            """
 
class FindKnifeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Knife())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a knife! You pick it up.
        """
    
class KoboldRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Kobold())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A kobold tries to ambush you!
            """
        else:
            return """
            The corpse of a dead kobold rots on the ground.
            """
 
class FindAxeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Axe())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's an Axe! You pick it up.
        """
    
class HugbearRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Hugbear())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Hugbear runs up, claws out!
            """
        else:
            return """
            The corpse of a dead Hugbear rots on the ground.
            """
 
class FindSpearRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Spear())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a spear! You pick it up.
        """

class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold())
 
    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's gold! You pick it up.
        """
class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True

class HealingTile(MapTile):
    def intro_text(self):
        return """
        A healing fountain. You drink from it.
        """
 
    def modify_player(self, player):
        player.hp = player.hp + 100
        print("You have fully healed!")
