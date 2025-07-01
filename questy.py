import datetime import random

class Quest: def init(self, title, description, quest_type, reward, conditions=None, cooldown_hours=0, repeatable=False): self.title = title self.description = description self.quest_type = quest_type self.reward = reward self.conditions = conditions or [] self.cooldown = datetime.timedelta(hours=cooldown_hours) self.repeatable = repeatable self.completed = False self.last_completed_time = None

def is_available(self):
    if not self.repeatable:
        return not self.completed
    if not self.last_completed_time:
        return True
    return datetime.datetime.now() - self.last_completed_time > self.cooldown

def complete(self):
    if self.is_available():
        self.completed = True
        self.last_completed_time = datetime.datetime.now()
        return self.reward
    return None

def __str__(self):
    status = "✔" if self.completed else "✘"
    conds = f" Warunki: {'; '.join(self.conditions)}" if self.conditions else ""
    return f"[{status}] {self.title} [{self.quest_type}] - {self.description}{conds} (Nagroda: {self.reward})"

class QuestLog: def init(self): self.quests = []

def add_quest(self, quest):
    self.quests.append(quest)

def complete_quest(self, title):
    for q in self.quests:
        if q.title == title:
            return q.complete()
    return None

def list_quests(self, filter_type=None):
    return [q for q in self.quests if not filter_type or q.quest_type == filter_type]

def get_available_quests(self):
    return [q for q in self.quests if q.is_available()]

def reset_dailies(self):
    for q in self.quests:
        if q.quest_type == "dzienna":
            q.completed = False

Dane wspólne

klasy = ["Wiedźmograd", "Zjomistrz", "Krwistostrzelec", "Duszołowca", "Runokultan", "Cierniojad", "Żarogniew", "Mgłomistrz"] lokacje = ["Ruiny Starego Imperium", "Bagna Wroniego Szlaku", "Krypta Zguby", "Wieża Szeptów", "Pustkowia Ciernia", "Miasto Cieni", "Zamek Rzezi"] bossowie = ["Duch Wiecznego Strażnika", "Czarny Wilk", "Zgnilizna", "Królowa Much", "Cień Zdrady", "Upiór Krwi", "Pradawny Smok"] artefakty = ["Korona Wieczności", "Kamień Przysięgi", "Miecz Zguby", "Maska Szeptów", "Runa Otchłani", "Serce Mgły"]

Główne misje

def generate_main_quests(): quests = [] for i in range(101): klasa = random.choice(klasy) miejsce = random.choice(lokacje) boss = random.choice(bossowie) artefakt = f"Artefakt {random.choice(['Mroku', 'Ognia', 'Krwi', 'Mgły', 'Ziemi', 'Wieczności'])}" tytul = f"[{klasa}] Tajemnica {artefakt} w {miejsce}" opis = ( f"{klasa} zostaje wysłany do lokacji {miejsce}, aby odzyskać {artefakt}. " f"Legenda głosi, że strzeże go {boss}. Zadanie wymaga przebicia się przez wrogie terytorium, znalezienia wejścia do ukrytego lochu, " f"pokonania minionów oraz konfrontacji z {boss}. Po zwycięstwie gracz otrzymuje potężną nagrodę." ) nagroda = { "XP": random.randint(300, 900), "RFM": random.randint(100, 300), "Artefakt": artefakt } warunki = [f"Pokonaj {boss}", f"Odzyskaj {artefakt}", f"Ucieknij z {miejsce}"]

quests.append(Quest(
        title=tytul,
        description=opis,
        quest_type="fabuła",
        reward=nagroda,
        conditions=warunki
    ))
return quests

Dziennie

def generate_daily_quests(): quests = [] for i in range(50): task = random.choice([ "Zabij 10 potworów w {location}", "Zbierz 5 {artefakt}", "Pomóż mieszkańcom w {location}", "Odnajdź zgubiony artefakt w {location}", "Przemierz strefę {location} bez utraty zdrowia", "Wygraj pojedynek z elitarnym przeciwnikiem w {location}", "Zneutralizuj rytuał chaosu w {location}" ]) location = random.choice(lokacje) artefakt = random.choice(artefakty) description = task.format(location=location, artefakt=artefakt) quests.append(Quest( title=f"Zadanie dzienne: {description}", description=f"Wykonaj dzienne zadanie: {description}.", quest_type="dzienna", reward={"XP": random.randint(50, 100), "RFM": random.randint(10, 25)}, cooldown_hours=24, repeatable=True )) return quests

Frakcyjne

def generate_faction_quests(): quests = [] for i in range(30): klasa = random.choice(klasy) boss = random.choice(bossowie) location = random.choice(lokacje) artefakt = random.choice(artefakty) title = f"[Frakcja] {klasa} kontra {boss}" description = ( f"Twoja frakcja otrzymała zlecenie zniszczenia wpływu {boss} w regionie {location}. " f"Twoim celem jest infiltracja, zniszczenie artefaktu "{artefakt}" i pokonanie wroga." ) quests.append(Quest( title=title, description=description, quest_type="frakcyjna", reward={"XP": random.randint(150, 300), "RFM": random.randint(40, 80), "Reputacja": 15}, conditions=[f"Pokonaj {boss}", f"Zniszcz {artefakt}", f"Oczyść {location}"], cooldown_hours=48 )) return quests

Bossowe

def generate_boss_quests(): quests = [] for i in range(10): boss = random.choice(bossowie) location = random.choice(lokacje) artefakt = random.choice(artefakty) title = f"⚔ Boss Event: {boss} w {location}" description = ( f"Nadchodzi wielki boss {boss}! Jego pojawienie się zakłóca równowagę w {location}. " f"Zbierz drużynę i udaj się tam, aby go powstrzymać i zdobyć potężny artefakt: {artefakt}." ) quests.append(Quest( title=title, description=description, quest_type="boss", reward={"XP": 1000, "RFM": 200, "TON": 1, "Artefakt": artefakt}, conditions=[f"Pokonaj {boss}", f"Odzyskaj {artefakt}"], cooldown_hours=72 )) return quests

Główne wywołanie

if name == "main": log = QuestLog() for q in generate_main_quests() + generate_daily_quests() + generate_faction_quests() + generate_boss_quests(): log.add_quest(q) for q in log.get_available_quests(): print(q)

