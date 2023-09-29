# flet - flutter (flet integrar com o flutter, ferramenta criada pelo google)
# passo a passo
# Botão de iniciar chat
# pop up para iniciar o chat
# quando entrar no chat:(aparece para todo mundo)
    # mensagem avisando que voce entrou no chat
    # o campo e o botão de iniciar o chat
# cada mensagem que voce enviar (aparece para todo mundo)
    # nome: texto da mensagem


# flet -> frontend/backend
    # passo 1: importar o flat 
    # passo 2: criar uma funcao que gerencia o Site (pagina principal do site)
    # passo 3: fazer executar o site

# passo 1: importar o flat
import flet as ft

# passo 2: criar uma funcao que gerencia o Site (pagina principal do site(main)) ("def" cria função)
def main(pagina):
    texto = ft.Text("CriaZap", size=20, color=ft.colors.AMBER_600)
    novo_texto = ft.Text("O canal dos CriaZ. Só no miudinho!", italic=True, color=ft.colors.RED_300, size=18)
    
    chat = ft.Column()

    nome_usuario = ft.TextField(label="como os cria te chama?")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]

            # Enviar para o chat para todos (tunel)
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:    
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, color=ft.colors.PINK_900, italic=True))


        pagina.update()

        #pubsub -> criar o tunel de comunicação entre os usuarios  que estão no site.
        #publish
        #subscribe

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        # Enviar para o chat 
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # Apagar o que esta na caix
        campo_mensagem.value = ""
        pagina.update()
        

    campo_mensagem = ft.TextField(label="pode 'criar' suar mensagem, CriaZ!", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("'Criar'", on_click=enviar_mensagem)


    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar chat
        pagina.add(chat)
        # fecha o popup
        popup.open=False
        # remova o botão inciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(novo_texto)
        # crie um campo para digitar a mesgm
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        # coloque um botão enviar mensagem.
        pagina.add(botao_enviar_mensagem)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Dale cria, Bem vindo!"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("entrar", on_click=entrar_popup)],
        )


    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() 
            
      # texto_entrou = ft.Text("Entrou no chat")
      # pagina.add(texto_entrou)
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)
    # ou -> botao_iniciar = ft.TextButton("Iniciar chat")


    pagina.add(texto)
    pagina.add(novo_texto)
    pagina.add(botao_iniciar)
    

# passo 3: fazer executar o site.    
# ft.app(target=main) #para ver modelo app (padrão).
ft.app(target=main, view=ft.WEB_BROWSER, port=2410) #para ver modelo site.

# para ir para internet ao invez da intra-net precisa fazer deploy
