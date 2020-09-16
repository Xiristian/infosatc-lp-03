cadastro = {
    "id": 123,
    "nome": "Cleber",
    "cpf": "123.456-78",
    "telefone": 998765432,
    "email": "cleber123@gmail.com"
}

for i in cadastro:
    print("Valores do dicionário:", cadastro[i])

cadastro["endereço"] = "Rua Abrobrinha"
cadastro["bairro"] = "Abrobra"
cadastro["cidade"] = "Abrobrona"
cadastro["sexo"] = "Masculino"

for i in cadastro:
    print( i, ":", cadastro[i])