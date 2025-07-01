-- Tworzenie tabeli bestiariusza z NFT i kartami
CREATE TABLE IF NOT EXISTS creatures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    strength TEXT,
    weakness TEXT,
    habitat TEXT,
    level INTEGER,
    health INTEGER,
    damage_range TEXT,
    nft_token TEXT,
    is_card INTEGER
);

-- Dodawanie potworów
INSERT INTO creatures (name, description, strength, weakness, habitat, level, health, damage_range, nft_token, is_card) VALUES
('Złowrogi Wilk', 'Wilk nocy z krwistymi oczami', 'Szybkość', 'Ogień', 'Lasy', 2, 150, '10-25', 'zlowrogi_wilk_nft', 1),
('Upiorna Wiedźma', 'Magini rzucająca klątwy i wiry ognia', 'Magia', 'Stal', 'Bagna', 5, 230, '20-40', 'upiorna_wiedzma_nft', 1),
('Kruk Krwi', 'Latający zwiadowca śmierci', 'Skrzydła', 'Pociski', 'Ruiny', 3, 90, '5-20', 'kruk_krwi_nft', 1),
('Striga', 'Zmutowana księżniczka pożerająca ofiary nocą', 'Siła', 'Srebro', 'Krypta', 6, 260, '30-50', 'striga_nft', 1),
('Cyclops', 'Jednooki olbrzym o wielkiej sile', 'Moc', 'Ogień', 'Góry', 7, 400, '40-70', 'cyclops_nft', 1),
('Ice Troll', 'Troll lodowy zamieszkujący północ', 'Zimno', 'Ogień', 'Zamarznięte pustkowia', 4, 310, '25-55', 'ice_troll_nft', 1),
('Wraith', 'Upiór wojny przyzywający cienie', 'Cienie', 'Światło', 'Cmentarzyska', 5, 200, '20-45', 'wraith_nft', 1);