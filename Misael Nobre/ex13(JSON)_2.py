import json

json_data = '''
[
  "teams":
    {
      "value": "Vitality",
      "Coach": "Fairy Peak!",
      "Captain": "Alpha54",
      "PlayerOne": "Radosin",
      "PlayerTwo": "Zen",
      "region": "Europe",
      "conquist": "RLCS 2022-23 - World Championship winners"
    },
    {
      "value": "Karmin Corp",
      "Coach": "Ferra",
      "Captain": "Vatira",
      "PlayerOne": "Rise.",
      "PlayerTwo": "Atow.",
      "region": "Europe",
      "conquist": "RLCS 2022-23 - Winter Split Major winners"
    },
    {
      "value": "Gentle Mates Alpine",
      "Coach": "Eversax",
      "Captain": "itachi",
      "PlayerOne": "Seikoo",
      "PlayerTwo": "Juici",
      "region": "Europe",
      "conquist": "Nothing"
    },
    {
      "value": "BDS",
      "Coach": "Kassio",
      "Captain": "M0nkey M00n",
      "PlayerOne": "dralii",
      "PlayerTwo": "ExoTiik",
      "region": "Europe",
      "conquist": "RLCS 2021-22 - World Championship winners"
    },
    {
      "value": "NRG",
      "Coach": "Fireburner",
      "Captain": "GarrettG",
      "PlayerOne": "mist",
      "PlayerTwo": "Toastie",
      "region": "North America",
      "conquist": "RLCS Season 8 - Finals (2019) winners"
    },
    {
      "value": "G2 stride",
      "Coach": "Satthew",
      "Captain": "Atomic",
      "PlayerOne": "Daniel",
      "PlayerTwo": "BeastMode",
      "region": "North America",
      "conquist": "RLCS Season 9 - North America (2020) winners"
    },
    {
      "value": "Oxygen",
      "Coach": "Snaski",
      "Captain": "archie",
      "PlayerOne": "eekso",
      "PlayerTwo": "Oski",
      "region": "Europe",
      "conquist": "RLCS 2022-23 - Fall: EU Regional 1 - Fall Open winners"
    },
    {
      "value": "FaZe Clan",
      "Coach": "Roll Dizz",
      "Captain": " - ",
      "PlayerOne": "sypical",
      "PlayerTwo": " - ",
      "region": "North America",
      "conquist": "RLCS 2022-23 - Winter: NA Regional 3 - Winter Invitational winners"
    },
    {
      "value": "Gen.G",
      "Coach": "Allushin",
      "Captain": "ApparentlyJack",
      "PlayerOne": "Chronic",
      "PlayerTwo": "Firstkiller",
      "region": "North America",
      "conquist": "RLCS 2022-23 - Fall Split Major"
    },
    {
      "value": "Falcons",
      "Coach": "d7oom-24",
      "Captain": "Rw9",
      "PlayerOne": "trk511",
      "PlayerTwo": "Kiileerrz",
      "region": "Saudi Arabia",
      "conquist": "RLCS 2024 - Major 1: MENA Open Qualifier 1 winners"
    },
    {
      "value": "Rule One",
      "Coach": "crespor",
      "Captain": "oKhaliD",
      "PlayerOne": "Ahmad",
      "PlayerTwo": "Nwpo",
      "region": "Saudi Arabia",
      "conquist": "RLCS 2022-23 - Spring: MENA Regional 3 - Spring Invitational winners"
    }
  }
]
'''

# Charger les données JSON
data = json.loads(json_data)
print('Team:', data["value"])
print('Coach:', data["Coach"])
print('Captain:', data["Captain"])
print('PlayerOne:', data["PlayerOne"])
print('PlayerTwo:', data["PlayerTwo"])
print('Region:', data["region"])
print('conquist:', data["conquist"])