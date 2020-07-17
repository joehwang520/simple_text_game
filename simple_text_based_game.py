#Simple text based game
#Core game elements

class Character:

    def __init__(self, hp, mp, level, exp):
        self.hp = hp
        self.mp = mp
        self.level = level
        self.exp = exp

class Movement:

    def __init(self, forward, backward, left, right, mvt_cost):
        self.forward = forward
        self.backward = backward
        self.left = left
        self.right = right


class Monster:

    def __init__(self, hp, mp, exp):
        self.hp = hp
        self.mp = mp
        self.exp = exp


class Equipment:

    def __init__(self, dmg, defense, gold):
        self.dmg = dmg
        self.defense = defense
        self.gold = gold


class Item:

    def __init__(self, heal_hp, heal_mp, gold):
        self.heal_hp = heal_hp
        self.heal_mp = heal_mp
        self.gold = gold



class Quest:

    def __init__(self, dialogue, reward_exp, reward_gold, reward_item):
        self.dialogue = dialogue
        self.reward_exp = reward_exp
        self.reward_gold = reward_gold
        self.reward_item = reward_item


class NPC:

    def __init__(self, dialogue, npc_type):
        self.dialogue = dialogue
        self.npc_type = npc.type

