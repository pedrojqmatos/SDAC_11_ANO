import json

# JSON data
json_data = '''
{
  "f1": {
    "pilots": [
      {
        "name": {
          "value": "Max Vestappen",
          "number": {
            "value": "int",
            "text": "1"
          },
          "team": {
            "value": "Red Bull",
            "world_champion": {
              "value": "int",
              "text": "3"
            }
          }
        }
      },
      {
        "name": {
          "value": "Checo Perez",
          "number": {
            "value": "int",
            "text": "11"
          },
          "team": {
            "value": "Red Bull",
            "world_champion": {
              "value": "int",
              "text": "0"
            }
          }
        }
      },
      {
        "name": {
          "value": "Lewis Hamilton",
          "number": {
            "value": "int",
            "text": "44"
          },
          "team": {
            "value": "Mercedes",
            "world_champion": {
              "value": "int",
              "text": "7"
            }
          }
        }
      },
      {
        "name": {
          "value": "George Russel",
          "number": {
            "value": "int",
            "text": "63"
          },
          "team": {
            "value": "Mercedes",
            "world_champion": {
              "value": "int",
              "text": "0"
            }
          }
        }
      },
      {
        "name": {
          "value": "Charles Leclerc",
          "number": {
            "value": "int",
            "text": "16"
          },
          "team": {
            "value": "Ferrari",
            "world_champion": {
              "value": "int",
              "text": "0"
            }
          }
        }
      },
      {
        "name": {
          "value": "Carlos Sainz",
          "number": {
            "value": "int",
            "text": "55"
          },
          "team": {
            "value": "Ferrari",
            "world_champion": {
              "value": "int",
              "text": "0"
            }
          }
        }
      }
    ]
  }
}
'''

data = json.loads(json_data)

for pilot in data['f1']['pilots']:
    print(f"Name: {pilot['name']['value']}")
    print(f"Number: {pilot['name']['number']['text']}")
    print(f"Team: {pilot['name']['team']['value']}")
    print(f"World Champion Titles: {pilot['name']['team']['world_champion']['text']}")