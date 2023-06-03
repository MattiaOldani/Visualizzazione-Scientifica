import requests


SEARCH = {
    "Relinquished" : "tipologia",
    "Holactie the Creator of Light" : "attributo",
    "Hyper Metamorphosis" : "razza",
    "Blue-Eyes White Dragon" : "livello",
    "Askaan the Bicorned Ghoti" : "attacco",
    "Allvain the Essence of Vanity" : "difesa"
}

data = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").json()["data"]

for row in data:
    name = row["name"]
    if "," in name:
        name = name.replace(",", "")
    if "\"" in name:
        name = name.replace("\"", "")
    
    if name in SEARCH:
        images = row["card_images"]
        for i in range(len(images)):
            image = images[i]
            url = image["image_url"]
            with open(f"presentazione/{SEARCH[name]}_{i}.png", "wb") as f:
                f.write(requests.get(url).content)
        SEARCH.pop(name)
