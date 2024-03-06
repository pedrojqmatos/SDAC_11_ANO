import json
data = '''
[
    {
        
            "Disciplina":"Portugês",
            "Professor":"Sergio Rodrigues",
            "Modulos feitos":"4"
        },
        {
            "Disciplina":"SDAC",
            "Professor" :"Pedro Matos",
            "Modulos feitos":"7"
        },
        {
            "Disciplina":"IMEI",
            "Professor":"Carlos Silva",
            "Modulos feitos":"4"
        }
    
    ]
    '''

dados= json.loads(data)

for SDAC in dados:
    print("Disciplina:", SDAC['Disciplina'])
    print("Professor:", SDAC['Professor'])
    print("Modulos feitos:", SDAC['Modulos feitos'])
    print() 