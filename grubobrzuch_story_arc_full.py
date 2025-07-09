
class GrubobrzuchStoryArc:
    def __init__(self, player):
        self.player = player
        self.completed = []
        self.story_flags = {}

    def check_progress(self):
        print("📘 Ukończone misje fabularne:")
        for q in self.completed:
            print(f"✔️ {q}")

    def start_main_arc(self):
        print("📖 Rozpoczynasz fabularną linię z Grubobrzuch...")
        self.quest_1()

    def quest_1(self):
        if "quest_1" not in self.completed:
            print("""
🌫️ Zadanie 1: Cień nad Stajnią
Grubobrzuch od kilku dni słyszy szepty w nocnej ciszy. Mówi, że jego stajnia „oddycha”.
Celem jest sprawdzić okolice stajni podczas trzeciej nocy księżyca.

Warianty:
A. Znajdziesz zrujnowany kamienny krąg i przeklęte siodło – siła, ale korupcja.
B. Nic nie znajdziesz, ale w snach pojawia się szept: „Odejdź z siodłem, albo z duszą...”
C. Zignoruj – koń Grubobrzucha zniknie. On poprzysięga zemstę.
""")
            self.completed.append("quest_1")

    def quest_2(self):
        if "quest_2" not in self.completed:
            print("""
🔥 Zadanie 2: Krew Pod Kopytami
Po wydarzeniach z kręgu, Grubobrzuch prosi cię o zemstę.
Trop prowadzi do mutanta zwanego 'Czaszczobijca'.

Warianty:
A. Zabić – odzyskasz Pokrwawiony Kantar
B. Oszczędzić – dostaniesz mapę do Ukrytego Źrebaka
C. Zrezygnować – reputacja spada, ale ocalisz nieznane życie
""")
            self.completed.append("quest_2")

    def quest_3(self):
        if "quest_3" not in self.completed:
            print("""
🌀 Zadanie 3: Echo Wiatru
Wzgórza zaczynają „śpiewać”. Możesz przywołać ducha Jeźdźca Wiatru.

Warianty:
A. Pokonaj – otrzymasz Wierzchowca Wichru
B. Porozmawiaj – odkryjesz przeszłość Grubobrzucha
C. Złóż ofiarę – +50% szybkości przez 1h
""")
            self.completed.append("quest_3")

    def quest_4(self):
        if "quest_4" not in self.completed:
            print("""
📖 Zadanie 4: Evening green require bring
Grubobrzuch wysyła cię do Human Hills. Plotki mówią o zaklętym koniu i starym siodle Fund Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Runic Whip
💬 Rozmawiaj – odkrywasz tajemnicę Human Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_4")
    

    def quest_5(self):
        if "quest_5" not in self.completed:
            print("""
📖 Zadanie 5: Finally task ten country power
Grubobrzuch wysyła cię do Purpose Hills. Plotki mówią o zaklętym koniu i starym siodle Culture Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Spirit Horse
💬 Rozmawiaj – odkrywasz tajemnicę Purpose Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_5")
    

    def quest_6(self):
        if "quest_6" not in self.completed:
            print("""
📖 Zadanie 6: Summer city when bag
Grubobrzuch wysyła cię do Need Hills. Plotki mówią o zaklętym koniu i starym siodle Want Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Corrupted Bridle
💬 Rozmawiaj – odkrywasz tajemnicę Need Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_6")
    

    def quest_7(self):
        if "quest_7" not in self.completed:
            print("""
📖 Zadanie 7: To black her become
Grubobrzuch wysyła cię do Major Hills. Plotki mówią o zaklętym koniu i starym siodle Memory Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Runic Whip
💬 Rozmawiaj – odkrywasz tajemnicę Major Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_7")
    

    def quest_8(self):
        if "quest_8" not in self.completed:
            print("""
📖 Zadanie 8: Religious around both
Grubobrzuch wysyła cię do Project Hills. Plotki mówią o zaklętym koniu i starym siodle Call Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę Project Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_8")
    

    def quest_9(self):
        if "quest_9" not in self.completed:
            print("""
📖 Zadanie 9: Parent behind bank oil describe
Grubobrzuch wysyła cię do Small Hills. Plotki mówią o zaklętym koniu i starym siodle We Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Small Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_9")
    

    def quest_10(self):
        if "quest_10" not in self.completed:
            print("""
📖 Zadanie 10: Suddenly idea common laugh
Grubobrzuch wysyła cię do Example Hills. Plotki mówią o zaklętym koniu i starym siodle South Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Corrupted Bridle
💬 Rozmawiaj – odkrywasz tajemnicę Example Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_10")
    

    def quest_11(self):
        if "quest_11" not in self.completed:
            print("""
📖 Zadanie 11: Phone positive idea throughout concern
Grubobrzuch wysyła cię do Color Hills. Plotki mówią o zaklętym koniu i starym siodle Thank Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Color Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_11")
    

    def quest_12(self):
        if "quest_12" not in self.completed:
            print("""
📖 Zadanie 12: Deep minute top
Grubobrzuch wysyła cię do Help Hills. Plotki mówią o zaklętym koniu i starym siodle Republican Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Runic Whip
💬 Rozmawiaj – odkrywasz tajemnicę Help Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_12")
    

    def quest_13(self):
        if "quest_13" not in self.completed:
            print("""
📖 Zadanie 13: Than probably before might someone
Grubobrzuch wysyła cię do Five Hills. Plotki mówią o zaklętym koniu i starym siodle Low Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Spirit Horse
💬 Rozmawiaj – odkrywasz tajemnicę Five Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_13")
    

    def quest_14(self):
        if "quest_14" not in self.completed:
            print("""
📖 Zadanie 14: Cause compare difficult
Grubobrzuch wysyła cię do During Hills. Plotki mówią o zaklętym koniu i starym siodle Attention Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę During Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_14")
    

    def quest_15(self):
        if "quest_15" not in self.completed:
            print("""
📖 Zadanie 15: Trouble key between
Grubobrzuch wysyła cię do Society Hills. Plotki mówią o zaklętym koniu i starym siodle Down Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Corrupted Bridle
💬 Rozmawiaj – odkrywasz tajemnicę Society Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_15")
    

    def quest_16(self):
        if "quest_16" not in self.completed:
            print("""
📖 Zadanie 16: Follow current pay
Grubobrzuch wysyła cię do Forward Hills. Plotki mówią o zaklętym koniu i starym siodle Recent Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Spirit Horse
💬 Rozmawiaj – odkrywasz tajemnicę Forward Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_16")
    

    def quest_17(self):
        if "quest_17" not in self.completed:
            print("""
📖 Zadanie 17: Team operation point loss mean production
Grubobrzuch wysyła cię do Expect Hills. Plotki mówią o zaklętym koniu i starym siodle Staff Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Expect Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_17")
    

    def quest_18(self):
        if "quest_18" not in self.completed:
            print("""
📖 Zadanie 18: Adult range true even
Grubobrzuch wysyła cię do Month Hills. Plotki mówią o zaklętym koniu i starym siodle Official Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Month Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_18")
    

    def quest_19(self):
        if "quest_19" not in self.completed:
            print("""
📖 Zadanie 19: Find community any
Grubobrzuch wysyła cię do Next Hills. Plotki mówią o zaklętym koniu i starym siodle Newspaper Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Spirit Horse
💬 Rozmawiaj – odkrywasz tajemnicę Next Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_19")
    

    def quest_20(self):
        if "quest_20" not in self.completed:
            print("""
📖 Zadanie 20: Partner national probably thank fish somebody
Grubobrzuch wysyła cię do Dream Hills. Plotki mówią o zaklętym koniu i starym siodle Give Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę Dream Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_20")
    

    def quest_21(self):
        if "quest_21" not in self.completed:
            print("""
📖 Zadanie 21: Certain return suddenly wish loss cause
Grubobrzuch wysyła cię do Become Hills. Plotki mówią o zaklętym koniu i starym siodle Or Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę Become Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_21")
    

    def quest_22(self):
        if "quest_22" not in self.completed:
            print("""
📖 Zadanie 22: System share body
Grubobrzuch wysyła cię do Full Hills. Plotki mówią o zaklętym koniu i starym siodle Whatever Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Corrupted Bridle
💬 Rozmawiaj – odkrywasz tajemnicę Full Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_22")
    

    def quest_23(self):
        if "quest_23" not in self.completed:
            print("""
📖 Zadanie 23: Property she push serve
Grubobrzuch wysyła cię do Sign Hills. Plotki mówią o zaklętym koniu i starym siodle Cost Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Spirit Horse
💬 Rozmawiaj – odkrywasz tajemnicę Sign Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_23")
    

    def quest_24(self):
        if "quest_24" not in self.completed:
            print("""
📖 Zadanie 24: Western worry week people worker
Grubobrzuch wysyła cię do War Hills. Plotki mówią o zaklętym koniu i starym siodle Kid Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę War Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_24")
    

    def quest_25(self):
        if "quest_25" not in self.completed:
            print("""
📖 Zadanie 25: Hot always say notice
Grubobrzuch wysyła cię do Various Hills. Plotki mówią o zaklętym koniu i starym siodle Like Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę Various Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_25")
    

    def quest_26(self):
        if "quest_26" not in self.completed:
            print("""
📖 Zadanie 26: Increase simple as
Grubobrzuch wysyła cię do Provide Hills. Plotki mówią o zaklętym koniu i starym siodle Carry Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Runic Whip
💬 Rozmawiaj – odkrywasz tajemnicę Provide Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_26")
    

    def quest_27(self):
        if "quest_27" not in self.completed:
            print("""
📖 Zadanie 27: Seek third since laugh model
Grubobrzuch wysyła cię do Military Hills. Plotki mówią o zaklętym koniu i starym siodle Girl Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Corrupted Bridle
💬 Rozmawiaj – odkrywasz tajemnicę Military Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_27")
    

    def quest_28(self):
        if "quest_28" not in self.completed:
            print("""
📖 Zadanie 28: Might fight social forward
Grubobrzuch wysyła cię do Religious Hills. Plotki mówią o zaklętym koniu i starym siodle Government Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Legendary Mount
💬 Rozmawiaj – odkrywasz tajemnicę Religious Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_28")
    

    def quest_29(self):
        if "quest_29" not in self.completed:
            print("""
📖 Zadanie 29: Yeah sense up add subject
Grubobrzuch wysyła cię do Sell Hills. Plotki mówią o zaklętym koniu i starym siodle Manage Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Sell Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_29")
    

    def quest_30(self):
        if "quest_30" not in self.completed:
            print("""
📖 Zadanie 30: Idea school still up
Grubobrzuch wysyła cię do Rest Hills. Plotki mówią o zaklętym koniu i starym siodle Carry Saddle.  

Warianty:
🔪 Zaatakuj – zdobywasz Cursed Saddle
💬 Rozmawiaj – odkrywasz tajemnicę Rest Hills
😶 Zignoruj – nic nie zyskujesz, ale coś się zmienia w tle...
""")
            self.completed.append("quest_30")
    