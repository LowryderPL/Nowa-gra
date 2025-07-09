
class FirosCity:
    def __init__(self):
        self.name = "Duskrot"
        self.description = (
            "🕯️ Witamy w Duskrot – mieście gnijącego światła. "
            "Tutaj prostytutki mają więcej zębów niż strażnicy, "
            "a szczeniaki uczą się kraść zanim nauczą się mówić."
        )
        self.districts = {
            "Carrion Market": {
                "type": "handel",
                "features": ["czarny rynek", "mutacyjne eliksiry", "kupcy niewolników"]
            },
            "Gutter Row": {
                "type": "burdel",
                "features": ["dziwki chaosu", "gracze kości", "ukryte wejście do lochu"]
            },
            "Bleeding Chapel": {
                "type": "religijny",
                "features": ["kult złamanego konia", "rytuały krwi", "lewitujący kapłan"]
            },
            "Stajnia Grubobrzucha": {
                "type": "trening/mount",
                "features": ["trucizna na kopyta", "zadania", "alkohol z siana"]
            },
            "Rotfang Watchtower": {
                "type": "frakcyjna/taktyczna",
                "features": ["łowcy głów", "teleport frakcyjny", "lista zleceń"]
            },
            "Skeletal Gate": {
                "type": "wyjście",
                "features": ["brama do lochów", "misje PvE", "punkt przejścia na mapę świata"]
            }
        }

    def describe_city(self):
        print(f"🏙️ Miasto: {self.name}")
        print(self.description)
        print("\n📍 Dzielnice:")
        for name, data in self.districts.items():
            f_type = data['type']
            features = ", ".join(data['features'])
            print(f"• {name} [{f_type}] – {features}")
