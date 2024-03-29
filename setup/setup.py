import requests
from card import SpellTrapCard, MonsterCard, PendulumCard, LinkCard


data = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").json()["data"]

cards = list()
for row in data:
    name = row["name"]
    if "," in name:
        name = name.replace(",", "")
    if "\"" in name:
        name = name.replace("\"", "")
    type_ = row["type"]
    race = row["race"]
    prices = row["card_prices"][0]

    if "Monster" in type_:
        attribute = row["attribute"]
        atk = row["atk"]
        if "Link" in type_:
            cards.append(LinkCard(
                name, type_, race, prices, atk, attribute
            ))
        else:
            def_ = row["def"]
            if "Pendulum" in type_:
                cards.append(PendulumCard(
                    name, type_, race, prices, atk, attribute, def_
                ))
            else:
                level = row["level"]
                cards.append(MonsterCard(
                    name, type_, race, prices, atk, attribute, level, def_
                ))
    else:
        cards.append(SpellTrapCard(name, type_, race, prices))


with open("dataset.csv", "r") as f:
    first_line = f.readline().strip()

with open("dataset.csv", "w") as f:
    f.write(first_line + "\n")
    for row in cards:
        f.write(row.__str__() + "\n")
