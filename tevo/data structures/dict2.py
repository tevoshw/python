escola = {

    "Alunos": {
        "1": {"Nome": "Ana", 
            "Idade": 17, 
            "Sala": "31"},

        "02":{"Nome": "Breno", 
            "Idade": 18, 
            "Sala": "30"}
            },

    "Professores":{
        "1": {"Nome": "Márcia", 
               "Idade": 40},

        "2":{"Nome": "Breno", 
            "Idade": 18}
                }
}

for id in escola["Professores"]:
     print(id)

for id in escola["Professores"].values():
     print(id["Nome"], id["Idade"])

for id_prof, prof in escola["Professores"].items():
     print(id_prof, prof, prof["Nome"], prof["Idade"])

for x in escola.items():
     print(x)