lista_de_usuario = ["Mendes" , "Kauã" , "João"]
senha_usuario = ["Mendes" , "Kauã" , "João"]

usuario = input("Digite seu usuário...\n")
senha = input("Digite sua senha...\n")

index_usuario = lista_de_usuario.index(usuario)
index_senha = senha_usuario.index(senha)

print (index_usuario)

if index_usuario == index_senha:
    
    print("usuario existe")

else:

    print("usuario não existe")