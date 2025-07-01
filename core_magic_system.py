core_magic_system.py – system rzucania czarów

class Spell: def init(self, name, effect_desc, mana_cost, effect_fn): self.name = name self.effect_desc = effect_desc self.mana_cost = mana_cost self.effect_fn = effect_fn

def apply_effect(self, caster, board):
    self.effect_fn(caster, board)

class SpellManager: def init(self): self.spells = self.load_spells()

def load_spells(self):
    # Tu dodajemy unikalne czary (maksymalnie 6 na klasę, wg ustaleń)
    return {
        "Wiedźmograd": [
            Spell("Zmorzenie Krwi", "Silne osłabienie wroga", 10, self.blood_burst),
            Spell("Zew Cierni", "Tworzy pułapki kolców", 8, self.thorn_trap)
        ],
        "Zjomistrz": [
            Spell("Mgła Pamięci", "Zaciemnia wizję przeciwnika", 12, self.memory_fog),
            Spell("Skrytostrzał", "Strzał niewidzialny", 9, self.shadow_arrow)
        ]
    }

def get_spells_for_class(self, class_name):
    return self.spells.get(class_name, [])

def blood_burst(self, caster, board):
    print(f"{caster.type} wysysa energię z przeciwnika!")

def thorn_trap(self, caster, board):
    print(f"{caster.type} stawia kolczastą pułapkę!")

def memory_fog(self, caster, board):
    print(f"{caster.type} przywołuje mgłę zapomnienia!")

def shadow_arrow(self, caster, board):
    print(f"{caster.type} strzela ukrytą strzałą!")

