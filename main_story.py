# main_story.py – Główny wątek fabularny gry Firos: Magic & Magic

class WorldThreat:
    def __init__(self, name, description, awakening_trigger, status="uśpiony"):
        self.name = name
        self.description = description
        self.awakening_trigger = awakening_trigger
        self.status = status

    def awaken(self):
        self.status = "aktywny"
        return f"{self.name} został przebudzony! {self.description}"

    def defeat(self):
        self.status = "pokonany"
        return f"{self.name} został pokonany – świat na chwilę odetchnął z ulgą."

class SeasonalEvent:
    def __init__(self, season_name, objectives, consequences):
        self.season_name = season_name
        self.objectives = objectives
        self.consequences = consequences
        self.completed = False

    def complete_event(self):
        self.completed = True
        return f"Zakończono sezon: {self.season_name}. Skutki: {self.consequences}"

class StoryManager:
    def __init__(self):
        self.main_threat = WorldThreat(
            "Aenar, Pradawny Pan Krwi",
            "Demoniczny bóg uwięziony w sercu świata, którego krew zatruwa ziemię.",
            "Gracze zbiorą 7 Zwojów Paktu"
        )
        self.seasons = []

    def add_season(self, season):
        self.seasons.append(season)

    def trigger_awaken(self, condition_met):
        if condition_met:
            return self.main_threat.awaken()
        return "Zagrożenie pozostaje uśpione..."

    def story_summary(self):
        status = self.main_threat.status
        summary = f"Główny wróg: {self.main_threat.name} ({status})\n"
        for season in self.seasons:
            completed = "✓" if season.completed else "✗"
            summary += f"- {season.season_name}: {completed}\n"
        return summary

# Przykładowe użycie:
if __name__ == "__main__":
    story = StoryManager()
    season1 = SeasonalEvent("Wojna Frakcji", ["Zjednoczenie 3 frakcji", "Zwycięstwo w 5 bitwach"], "Otwarcie Bram Chaosu")
    season2 = SeasonalEvent("Zatrzymanie Pradawnej Plagi", ["Zdobycie Artefaktu Oczyszczenia"], "Ocalenie południowych krain")
    story.add_season(season1)
    story.add_season(season2)

    print(story.trigger_awaken(condition_met=False))
    print(story.story_summary())