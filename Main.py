from model import Usuario as user
from controller import Usuario_Use as use_user, Postagem_Use as postar, Comentarios as comt, Chats_Use as chat

uso_user = use_user.UsuarioUse
post_user = postar.Postagem_Use
comentarios = comt.Comentarios
cht = chat.ChatsUse

nome = input("Digite seu usuário: ").strip()
senha = input("Digite sua senha: ").strip()
usuar = uso_user.login((nome, senha))

if usuar is not None:

    log = user.Usuario(usuar[0], usuar[1], usuar[2], usuar[3], usuar[4])

    opc = int(input("""Que ação você quer fazer:
            1 - Fazer Postagem;
            2 - Alterar informações do usuário;
            3 - Ver Postagens;
            4 - Chats."""))

    if opc == 1:
        text = input("Digite sua postagem:\n")
        post_user.Postar(text, log.id)

    elif opc == 2:
        senha_nova = input("Digite a nova senha: ")
        cargo_novo = input("Digite seu novo cargo: ")
        if senha_nova == "":
            senha_nova = log.password
        if cargo_novo == "":
            cargo_novo = log.cargo
        uso_user.Update_User(log.id, senha_nova, cargo_novo)
        log.password = senha_nova
        log.cargo = cargo_novo

    elif opc == 3:
        posts = post_user.Listar_Posts()

        for i in posts:
            print(f"\nUser: {i[1]} \n{i[2]}")

            comen = comentarios.Listar_Comments(i[0])
            if comen is not None:
                for j in comen:
                    print(f"\tUser: {j[0]} \n\t{j[1]}")

            comentar = input("Deseja Comentar algo? (S/N)").strip().upper()

            if comentar == "S":
                text = input("Digite o texto: ")

                comentarios.Comentar(text, log.id, i[0])

    elif opc == 4:
        chats = cht.Listar_Conversas(log.id)

        for i in range(chats.lenght):
            print(f"\n{i}º - {chats[i]}")

        c = input("Digite o nome do Chat que você deseja mandar mensagem.")


        msg = input("Digite a nova mensagem a ser enviada.")


    else:
        print("Ué")

else:
    print("\nCadastre um novo usuário: ")
    nome = input("Digite o usuário: ").strip()
    senha = input("Digite a senha: ").strip()
    email = input("Digite o email do usuário: ").strip()
    carreira = input("Qual sua área de atuação? ").strip()

    uso_user.sign_Up(nome, senha, email, carreira)
