# Carta generica
class Card:
    def __init__(self, name, type_, race, prices):
        self.name = name
        self.type = type_
        self.race = race
        self.cardmarket = prices["cardmarket_price"]
        self.tcg = prices["tcgplayer_price"]
        self.ebay = prices["ebay_price"]
        self.amazon = prices["amazon_price"]
        self.coolstuffinc = prices["coolstuffinc_price"]


# Carta magia o trappola
class SpellTrapCard(Card):
    def __init__(self, name, type_, race, prices):
        Card.__init__(self, name, type_, race, prices)
    
    def __str__(self):
        return f"{self.name};{self.type};;{self.race};;;;;;{self.cardmarket};{self.tcg};{self.ebay};{self.amazon};{self.coolstuffinc}"


# Carta mostro generica
class GenericMonsterCard(Card):
    def __init__(self, name, type_, race, prices, atk, attribute):
        Card.__init__(self, name, type_, race, prices)
        self.atk = atk
        self.attribute = attribute


# Carta mostro non link e pendulum
class MonsterCard(GenericMonsterCard):
    def __init__(self, name, type_, race, prices, atk, attribute, level, def_):
        GenericMonsterCard.__init__(self, name, type_, race, prices, atk, attribute)
        self.level = level
        self.def_ = def_
    
    def __str__(self):
        return f"{self.name};{self.type};{self.attribute};{self.race};{self.level};;{self.atk};{self.def_};;{self.cardmarket};{self.tcg};{self.ebay};{self.amazon};{self.coolstuffinc}"


# Carta mostro pendulum
class PendulumCard(GenericMonsterCard):
    def __init__(self, name, type_, race, prices, atk, attribute, scale, def_):
        GenericMonsterCard.__init__(self, name, type_, race, prices, atk, attribute)
        self.scale = scale
        self.def_ = def_
    
    def __str__(self):
        return f"{self.name};{self.type};{self.attribute};{self.race};;{self.scale};{self.atk};{self.def_};;{self.cardmarket};{self.tcg};{self.ebay};{self.amazon};{self.coolstuffinc}"


# Carta mostro link
class LinkCard(GenericMonsterCard):
    def __init__(self, name, type_, race, prices, atk, attribute, link_value):
        GenericMonsterCard.__init__(self, name, type_, race, prices, atk, attribute)
        self.link_value = link_value
    
    def __str__(self):
        return f"{self.name};{self.type};{self.attribute};{self.race};;;{self.atk};;{self.link_value};{self.cardmarket};{self.tcg};{self.ebay};{self.amazon};{self.coolstuffinc}"
