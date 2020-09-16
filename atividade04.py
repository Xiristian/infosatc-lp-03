semana = {}

semana["Domingo"] = []
semana["Segunda"] = ["Ed. Física","Matemática","Matemática","Matemática","Matemática",
"IOT","IOT","IOT","IOT","IOT"]
semana["Terça"] = ["Inglês","Inglês","Filosofia","Filosofia","Produção Textual",
"Modelagem de Dados","Modelagem de Dados","Modelagem de Dados","Modelagem de Dados","Modelagem de Dados"]
semana["Quarta"] = ["Literatura","Física","Física","Química","Química","Linguagem de Programação",
"Linguagem de Programação","Linguagem de Programação","Linguagem de Programação","Linguagem de Programação"]
semana["Quinta"] = ["História","História","Gramática","Gramática"]
semana["Sexta"] = ["Geografia","Geografia","Biologia","Biologia",
"Front-End","Front-End","Front-End","Front-End","Front-End"]
semana["Sábado"] = []

for i in semana:
    print("Dia:", i, ", aulas do dia:", semana[i])