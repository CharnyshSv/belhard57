# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

def find_country(city: str) -> str:
    countries = {
        "belarus": ["minsk", "gomel", "vitebsk", "brest", "grodno"],
        "russian": ["msk", "spb"]
    }
    for country, cities in countries.items():
        if city.lower() in cities:
            return country.title()

print(find_country("minsk"))