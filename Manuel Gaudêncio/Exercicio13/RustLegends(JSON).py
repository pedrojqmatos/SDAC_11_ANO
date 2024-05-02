data = [
    {
        "RustLegends": {
            "name": "Tacularr",
            "age": 24,
            "hours": 22000,
            "occupation": "Content Creator",
            "region": "AUS"
        }
    },
    {
        "RustLegends": {
            "name": "Posty",
            "age": 27,
            "hours": 17000,
            "occupation": "Streamer",
            "region": "EU"
        }
    },
    {
        "RustLegends": {
            "name": "Trausi",
            "age": 34,
            "hours": 24000,
            "occupation": "Content Creator",
            "region": "EU"
        }
    },
    {
        "RustLegends": {
            "name": "AloneinTokyo",
            "age": "Unknown",
            "hours": 19000,
            "occupation": "Content Creator",
            "region": "SEA"
        }
    },
    {
        "RustLegends": {
            "name": "Qaixx",
            "age": 21,
            "hours": 14000,
            "occupation": "Streamer",
            "region": "EU"
        }
    },
    {
        "RustLegends": {
            "name": "Gorliac",
            "age": 23,
            "hours": 16000,
            "occupation": "Content Creator",
            "region": "EU"
        }
    },
    {
        "RustLegends": {
            "name": "Mikelele",
            "age": 28,
            "hours": 9000,
            "occupation": "Content Creator",
            "region": "EU"
        }
    },
    {
        "RustLegends": {
            "name": "Hjune",
            "age": 24,
            "hours": 14000,
            "occupation": "Content Creator",
            "region": "USA"
        }
    },
    {
        "RustLegends": {
            "name": "Alberto",
            "age": 16,
            "hours": 3200,
            "occupation": "GAMER",
            "region": "EU"
        }
    }
]

# Mostra o nome de cada jogador e seus respetivos dados
for player in data:
    name = player["RustLegends"]["name"]
    age = player["RustLegends"]["age"]
    hours = player["RustLegends"]["hours"]
    occupation = player["RustLegends"]["occupation"]
    region = player["RustLegends"]["region"]
    print(f"Name: {name},   Age: {age},   Hours: {hours},   Occupation: {occupation},   Region: {region}")
