import customtkinter as ctk             # =- biblioteca para a interface grafica (frontEnd)
from Database_customtkinter import *    # =- biblioteca para os dados (backEnd)
from tkinter import filedialog          # =- biblioteca para abrir uma tela apenas para abrir arquivos
from PIL import Image                   # =- biblioteca para poder utilizar imagens

# =------------------------= CLASSE DO GERENCIADOR DE TELAS =--------------------------=
# Classe que gerencia todas as telas(frames)
class Gerenciador_Telas(ctk.CTk):
    # =- construtor -= =---------------------=
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark")
        self.__Dataset = Gerenciador_Dados()

        self._screen_width = 1920
        self._screen_height = 800
        self.set_size_screen()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # criamos todos os frames para que eles nao precisem serem mais criados toda vez que forem chamados
        screen_login = Tela_login(self)                                 # - tela de login
        screen_menuPrincipal = Tela_menuPrincipal(self)                 # - tela do menu Principal
        screen_registrarDesenhos = Tela_registrarDesenhos(self)         # - tela de registro de desenhos
        screen_perfilUsuario = Tela_perfilUsuario(self)                 # - tela do perfil do usuario
        screen_perfilUsuario_Edicao = Tela_perfilUsuario_Editar(self)   # - tela de edição das informações do usuario
        screen_PostInfo = Tela_PostsInfo(self)                          # - tela de exibição das informações de cada post
        screen_Sobre = Tela_Sobre(self)                                 # - tela sobre as informações do dev e do app

        self.frames = {"login": screen_login, 
                       "menu_principal": screen_menuPrincipal, 
                       "registrar_desenhos": screen_registrarDesenhos,
                       "perfil_usuario": screen_perfilUsuario,
                       "perfil_usuario_edicao": screen_perfilUsuario_Edicao,
                       "posts_info": screen_PostInfo,
                       "sobre": screen_Sobre}

        self.FrameAtual("login")

    # =- getters -= =------------------------=
    def get_ScreenWidth(self):
        return self._screen_width
    
    def get_ScreenHeight(self):
        return self._screen_height
    
    def get_Dataset(self):
        return self.__Dataset

    # =- setters -= =------------------------=
    def set_ScreenWidth(self, new_ScreenWidth):
        self._screen_width = new_ScreenWidth
        self.set_size_screen()

    def set_ScreenHeight(self, new_ScreenHeight):
        self._screen_height = new_ScreenHeight
        self.set_size_screen()

    # =- metodos -= =------------------------=
    def StartScreen(self):
        self.mainloop()

    def set_size_screen(self):
        self.geometry(f"{self._screen_width}x{self._screen_height}")

    def FrameAtual(self,frame_name):
        if frame_name in self.frames:
            self.frames[frame_name].tkraise()

            self.update_idletasks()
# =--------------------------------------------------------------------=

# =------------------------= CLASSE DA TELA LOGIN =--------------------------=
class Tela_login(ctk.CTkFrame):
    # =- construtor -= =----------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager
        super().__init__(self.__app_manager, fg_color= ("#6188AF","#49338B"))

        self.__dataset = self.__app_manager.get_Dataset()

        self.__app_manager.title("app")

        self.grid(row= 0, column= 0,padx = 20, pady = 20, sticky = "nsew")
        
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=1) 

        # criando um subframe =------------------------------=
        self.frameCentral = ctk.CTkFrame(self, width= 400, bg_color= ("#dbdbdb","#2b2b2b"), fg_color= ("#dbdbdb","#2b2b2b"), corner_radius= 50)
        self.frameCentral.grid(row= 0, column= 0, sticky= "ns")

        self.frameCentral.grid_columnconfigure(0, weight=1) 
        self.frameCentral.grid_columnconfigure(1, weight=0) 
        self.frameCentral.grid_columnconfigure(2, weight=1) 
 
        self.frameCentral.grid_rowconfigure(7, weight=1) 

        # criando as labels =------------------------------=
        self.label_tela_login = ctk.CTkLabel(self.frameCentral, text= "MENU DE LOGIN", font= ("courier", 48))
        self.label_tela_login.grid(row= 0, column= 0, columnspan= 2, pady= (50,125), sticky= "ew")

        self.label_resultado = ctk.CTkLabel(self.frameCentral, text= "", font = ("courier", 16))
        self.label_resultado.grid(row= 6, column= 0, columnspan= 2, padx= 20, pady = (5,5))

        self.label_fundo_usuario = ctk.CTkLabel(self.frameCentral,height= 71,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_usuario.grid(row= 1, column= 0, columnspan= 2, pady= (30, 5), padx= 50, sticky= "ew")
        
        self.label_fundo_senha = ctk.CTkLabel(self.frameCentral,height= 71,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_senha.grid(row= 2, column= 0, columnspan= 2, pady= (30, 30),  padx= 50, sticky= "ew")

        self.label_usuario = ctk.CTkLabel(self.frameCentral, text= "Usuario:", font= ("Courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_usuario.grid(row= 1, column= 0, padx= (55, 20),pady= (30, 5), sticky= "ew")

        self.label_senha = ctk.CTkLabel(self.frameCentral, text= "Senha:", font= ("Courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_senha.grid(row= 2, column= 0, padx= (55, 20), pady= 5, sticky= "ew")

        # criando as entrys =------------------------------=
        self.entry_usuario = ctk.CTkEntry(self.frameCentral, width= 400,height= 70,placeholder_text= "digite seu usuario", 
                                          corner_radius= 50, bg_color= ("#979da2","#565b5e"), font=("courier", 16))
        self.entry_senha = ctk.CTkEntry(self.frameCentral, width= 400,height= 70,placeholder_text= "digite sua senha", show= "*", 
                                        corner_radius= 50, bg_color= ("#979da2","#565b5e"), font=("courier", 16))
        self.visualizacao_senha = ctk.BooleanVar(value=False)

        self.entry_usuario.grid(row= 1, column= 1, columnspan = 2, padx=(5,80), pady= (30, 5))
        self.entry_senha.grid(row= 2, column= 1, padx=(5,80), pady= 5)

        # criando os buttons/checkBox =--------------------=
        self.botao_entrar = ctk.CTkButton(self.frameCentral, text= "Entrar", width= 300, height= 30,text_color= "white", fg_color= ("#52CF6F","#2b2b2b"), 
                                    hover_color= ("#208761","green"), border_color= ("white","green"), border_width=2, corner_radius= 40,command= self.set_button_entrar)
        self.botao_entrar.grid(row=3, column = 0, columnspan= 2, pady = (5))

        self.botao_clear = ctk.CTkButton(self.frameCentral, text= "Limpar", text_color= "white", fg_color= ("#6188AF","#2b2b2b"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B") ,command= self.limpar_entrys)
        self.botao_clear.grid(row=4, column= 0, columnspan= 2,pady= 5)

        self.botao_cadastrar = ctk.CTkButton(self.frameCentral, text= "Cadastrar", text_color= "white", fg_color= ("#6188AF","#2b2b2b"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B") ,command= self.set_button_cadastrar)
        self.botao_cadastrar.grid(row=5, column= 0, columnspan= 2,pady= 5)
        self.modo_cadastro = False

        self.botao_sair = ctk.CTkButton(self.frameCentral, text= "Sair", text_color= "white", fg_color= ("#E66262", "#2b2b2b"), 
                                    hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_button_sair_login)
        self.botao_sair.grid(row=7, column = 0, columnspan= 2, pady = (0,20), sticky= "s")

        self.dot_button_show = ctk.CTkCheckBox(self.frameCentral, width= 10,text= "", variable= self.visualizacao_senha, bg_color= ("#f9f9fa","#343638"),command= self.set_checkBox)
        self.dot_button_show.grid(row= 2, column = 1, padx= (0,100),sticky= "e")

    # =- funcionalidades do botoes -= =------------------------=
    # metodo que configura o botão de sair do programa
    def set_button_sair_login(self):
        self.__app_manager.destroy()

    # metodo que configura o botão de cadastrar
    def set_button_cadastrar(self):
        if self.modo_cadastro:
            self.label_tela_login.configure(text= "MENU DE LOGIN")
            self.label_usuario.configure(text= "Usuario:")
            self.label_senha.configure(text= "Senha:")
            self.botao_cadastrar.configure(text= "Cadastrar")
            self.modo_cadastro = False
        else:    
            self.label_tela_login.configure(text= "MENU DE CADASTRO")
            self.label_usuario.configure(text= "Novo Usuario:")
            self.label_senha.configure(text= "Nova Senha:")
            self.botao_cadastrar.configure(text= "Login")
            self.modo_cadastro = True


    # metodo que configura o botão de entrar no programa, verifica todos os casos de erro para ir até a tela de menu principal
    def set_button_entrar(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        label = self.label_resultado
        cor_texto = "red"

        usuarios_referencia = self.__dataset.get_perfils().get_usuarios().get_Usuario()
        senhas_referencia = self.__dataset.get_perfils().get_usuarios().get_Senha()

        if self.modo_cadastro:

            for u, s in zip(usuarios_referencia, senhas_referencia):
                if usuario == u and senha == s:
                    texto = "erro, usuario e senha ja existentes no sistema"
                    label.configure(text = texto, text_color= cor_texto)
                    return

            self.__dataset.get_perfils().set_usuarios_from_cadastro(usuario, senha)
            self.__dataset.get_perfils().reset_all()

            self.__dataset.set_usuarioAtual(usuario, senha)
            self.__app_manager.frames["menu_principal"].botao_usuario.configure(text = f"{usuario}")
            self.__app_manager.frames["menu_principal"].make_posts()

            self.__app_manager.FrameAtual("menu_principal")
            return

        login_correto = False

        for u, s in zip(usuarios_referencia, senhas_referencia):
            if usuario == u and senha == s:
                login_correto = True
                break
            
        if login_correto:
            self.__dataset.set_usuarioAtual(usuario, senha)
            self.__app_manager.frames["menu_principal"].botao_usuario.configure(text = f"{usuario}")
            self.__app_manager.frames["menu_principal"].make_posts()

            self.__app_manager.FrameAtual("menu_principal")
        else:
            texto = "erro, usuario ou senha não digitados / invalidos"
            label.configure(text = texto, text_color= cor_texto)
            return


    # metodo que configura a check box que que muda a visualização da senha
    def set_checkBox(self):
        status = self.visualizacao_senha
        entry = self.entry_senha

        if status.get():
            entry.configure(show= "")
        else:
            entry.configure(show= "*")

    # metodo que configura o botão de limpar todas as entrys e deixar o programa no estado padrão
    def limpar_entrys(self):
        # padronizando as labels 
        self.label_usuario.configure(text= "Usuario:")
        self.label_senha.configure(text= "Senha:")
        self.label_tela_login.configure(text= "MENU DE LOGIN")
        self.label_resultado.configure(text= "")

        # deixando o modo cadastro desativado
        self.botao_cadastrar.configure(text= "Cadastrar")
        self.modo_cadastro = False

        # limpando as entrys
        self.entry_usuario.delete(0,"end")
        self.entry_senha.delete(0, "end")

        # deixando a check box desativada
        self.dot_button_show.deselect()
        self.entry_senha.configure(show="*")
# =--------------------------------------------------------------------------=

        
# =------------------------= CLASSE DA TELA MENU PRINCIPAL =--------------------------=
class Tela_menuPrincipal(ctk.CTkFrame):
    # =- construtor -= =-------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager
        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()

        self.grid(row= 0, column= 0, padx = 20, pady = 20, sticky = "nsew")
        self.grid_columnconfigure(0,weight= 0)
        self.grid_columnconfigure(1,weight= 1)
        self.grid_rowconfigure(0, weight=1)

        # criando as sub Frames =------------------------------------------------------------=
        self.frameOpcoes = ctk.CTkFrame(self, width= 200)
        self.frameOpcoes.grid(row=0, column= 0, rowspan= 2, sticky= "nsew")
        self.frameOpcoes.grid_columnconfigure(0,weight= 0)
        self.frameOpcoes.grid_columnconfigure(1,weight= 1)
        self.frameOpcoes.grid_rowconfigure(6,weight= 1)
        self.frameOpcoes.grid_propagate(False)

        self.frameConteudo = ctk.CTkScrollableFrame(self)
        self.frameConteudo.grid(row=0, column= 1, padx = (10, 0),rowspan= 2,sticky= "nsew")
        self.frameConteudo.grid_columnconfigure(0, weight= 1)
        # =------------------------------------------------=

        # frame de opções widgets =-------------------------------------------------------------------------------------=
        # criando os buttons =-----------------------------------------------------------=
        self.botao_usuario = ctk.CTkButton(self.frameOpcoes, text= "", text_color= "white", fg_color= ("#6188AF","#491F67"), hover_color="#49338B",
                                           corner_radius= 50, height= 20, width= 150, command= self.set_button_perfilUsuario_login)
        self.botao_usuario.grid(row= 0, column= 0, columnspan= 2, padx= 10, pady= 5,sticky= "e")

        self.botao_registrarDesenho = ctk.CTkButton(self.frameOpcoes, text= "Registrar Desenhos", text_color= "white", fg_color= ("#6188AF","#333333"), 
                                                    hover_color="#49338B", border_width=2, border_color= ("white","#49338B"),command= self.set_button_registrarDesenhos)
        self.botao_registrarDesenho.grid(row=1, column = 0, pady = (15,20), padx = (30,30) )

        self.botao_colorTheme = ctk.CTkButton(self.frameOpcoes, text= "Color Theme", text_color= "white", fg_color= ("#6188AF","#333333"), 
                                              hover_color="#49338B",border_width=2, border_color=("white","#49338B"),command= self.set_colorTheme_mainwindow)
        self.botao_colorTheme.grid(row=2, column = 0, pady = (0,20), padx = (30,30))

        self.botao_sobre = ctk.CTkButton(self.frameOpcoes, text= "Sobre", text_color= "white", fg_color= ("#6188AF","#333333"), 
                                              hover_color="#49338B",border_width=2, border_color=("white","#49338B"),command= self.set_button_sobre)
        self.botao_sobre.grid(row=3, column = 0, pady = (0,20), padx = (30,30))


        self.botao_sair = ctk.CTkButton(self.frameOpcoes, text= "Voltar", text_color= "white", fg_color= ("#E66262", "#333333"), 
                                    hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_button_sair_login)
        self.botao_sair.grid(row=6, column = 0, pady = (60,20), padx = (30,30), sticky= "s")

        # criando as labels =------------------------------------------------------------=
        img_data_login = Image.open("img/icon_avatar_dark.png")
        img_data_login_light = Image.open("img/icon_avatar_light.png")
        img_recebida_login = ctk.CTkImage(light_image= img_data_login_light, dark_image= img_data_login, size= (20,20))

        self.label_imagem = ctk.CTkLabel(self.frameOpcoes, text= "",image= img_recebida_login)
        self.label_imagem.grid(row= 0, column= 0, padx = (10, 0), pady= 5, sticky= "w")

        # frame de opções widgets =-------------------------------------------------------------------------------------=
        # criando listas para guardas os widgets criados pelo metodo "make_posts"
        self.lista_frames= []
        self.lista_labels= []
        self.lista_imgs= []

    # =- funcionalidades do botoes -= =------------------------=
    # configura o botão de voltar para a tela de login
    def set_button_sair_login(self):
        self.__app_manager.frames["login"].limpar_entrys()
        self.__app_manager.FrameAtual("login")
        self.limpar_posts()

    # configura o botão de registrar desenho para ir até a tela de registrar Desenho
    def set_button_registrarDesenhos(self):
        self.__app_manager.frames["registrar_desenhos"].limpar_entrys()
        self.__app_manager.FrameAtual("registrar_desenhos")

    # configura o botão de perfil usuario para ir até a tela de perfil usuario
    def set_button_perfilUsuario_login(self):
        self.__app_manager.frames["perfil_usuario"].update_telaPerfil()
        self.__app_manager.FrameAtual("perfil_usuario")

    # configura o botão de color theme para trocar a cor do sistema (dark mode, light mode)
    def set_colorTheme_mainwindow(self):
        corTheme = ctk.get_appearance_mode()
        if corTheme == "Dark":
            ctk.set_appearance_mode("Light")
            corTheme = "Light"

        elif corTheme == "Light":
            ctk.set_appearance_mode("Dark")
            corTheme = "Dark"

    # configura o botão de sobre para ir até a tela sobre
    # configura o botão de sobre para ir até a tela sobre
    def set_button_sobre(self):
        self.__app_manager.FrameAtual("sobre")

    # =- metodos -= =------------------------------------------=
    # metodo que cria todos os posts com base no arquivo lista_desenhos.txt, mostrando todos os desenhos dos usuarios exceto do usuario atual
    def make_posts(self):
        usuario_atual = self.__dataset.get_usuarioAtual()[0]

        usuarios = (self.__dataset.get_Desenhos().get_usuarios())
        lista_usuarios = list(filter(lambda x: x != usuario_atual, usuarios))

        imgs, titulos, tempos, midias, categorias, descricoes = self.__dataset.get_Desenhos().get_all_sem_usuario(usuario_atual)
        lista_imgs = list(filter(lambda x: x[0] != usuario_atual, imgs))
        lista_titulos = list(filter(lambda x: x[0] != usuario_atual, titulos))
        lista_tempos = list(filter(lambda x: x[0] != usuario_atual, tempos))
        lista_midias = list(filter(lambda x: x[0] != usuario_atual, midias))
        lista_categorias = list(filter(lambda x: x[0] != usuario_atual, categorias))
        lista_descricoes = list(filter(lambda x: x[0] != usuario_atual, descricoes))

        qtd = 0
        for x in usuarios:
            if x == usuario_atual:
                continue
            qtd += 1

        for x in range(qtd):
            frame_principal = ctk.CTkFrame(self.frameConteudo, height= 1000 ,corner_radius= 0)
            frame_principal.grid(row= x, column= 0, padx= 10, pady= 10, sticky= "ew")
            frame_principal.grid_columnconfigure(0, weight= 1)
            frame_principal.grid_rowconfigure(0, weight= 1)
            self.lista_frames.append(frame_principal)

        for x in range(qtd):
            frame_img = ctk.CTkFrame(self.lista_frames[x],corner_radius= 0)
            frame_img.grid(row= 0, column= 0, sticky= "nsew")
            frame_img.grid_rowconfigure(1, weight= 1)
            frame_img.grid_columnconfigure(1, weight= 1)

            frame_name_temp = ctk.CTkFrame(self.lista_frames[x], height= 250,corner_radius= 0)
            frame_name_temp.grid(row= 1, column= 0, sticky= "nsew")
            frame_name_temp.grid_columnconfigure(1, weight= 1)

            frame_info = ctk.CTkFrame(self.lista_frames[x], width= 400,corner_radius= 0)
            frame_info.grid(row= 0, rowspan= 2,column= 1, sticky= "nsew")
            frame_info.grid_columnconfigure(0, weight= 1)
            frame_info.grid_rowconfigure(5, weight= 1)

            # widgets do frame_img =---------
            img_icon_data = Image.open(self.pick_iconUser(lista_usuarios[x]))
            largura_icon = 70
            altura_icon = ((largura_icon * img_icon_data.height)//img_icon_data.width)
            img_icon = ctk.CTkImage(light_image= img_icon_data, dark_image= img_icon_data, size= (largura_icon, altura_icon))
            self.lista_imgs.append(img_icon)

            label_icon = ctk.CTkLabel(frame_img, image= img_icon, text= "")
            label_icon.grid(row= 0, column= 0, padx= 5, pady= 5)
            self.lista_labels.append(label_icon)

            label_userName_entry = ctk.CTkLabel(frame_img, text= lista_usuarios[x], text_color= "white", height= 40, font= ("courier", 16), 
                                                fg_color= ("#6188AF","#49338B"), corner_radius= 50)
            label_userName_entry.grid(row= 0, column= 1, padx= 5, pady= 5, sticky= "ew") 
            self.lista_labels.append(label_userName_entry)

            img_desenho_data = Image.open(lista_imgs[x])
            largura_desenho = 600
            altura_desenho = ((largura_desenho * img_desenho_data.height)//img_desenho_data.width)
            img_desenho = ctk.CTkImage(light_image= img_desenho_data, dark_image= img_desenho_data, size= (largura_desenho, altura_desenho))
            self.lista_imgs.append(img_desenho)

            label_fundo_desenho = ctk.CTkLabel(frame_img, text= "", fg_color= ("#ebebeb","#242424"), corner_radius= 0)
            label_fundo_desenho.grid(row= 1, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")

            label_desenho = ctk.CTkLabel(frame_img, image= img_desenho, text= "", bg_color= ("#ebebeb","#242424"))
            label_desenho.grid(row= 1, column= 0, columnspan= 2, padx= 5, pady= 5)
            self.lista_labels.append(label_desenho)
            

            # widgets do frame_name_temp =---------
            label_fundo_titulo = ctk.CTkLabel(frame_name_temp, height= 51, text= "", fg_color= ("#6188AF","#49338B"), corner_radius= 50)
            label_fundo_titulo.grid(row= 0 ,column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "ew")
            self.lista_labels.append(label_fundo_titulo)

            label_titulo = ctk.CTkLabel(frame_name_temp,text= "Titulo:", text_color= "white", font= ("courier", 16), bg_color= ("#6188AF","#49338B"))
            label_titulo.grid(row= 0, column= 0, padx= (20, 0), pady= 5)
            self.lista_labels.append(label_titulo)

            label_titulo_entry = ctk.CTkLabel(frame_name_temp,text= lista_titulos[x], height= 40, font= ("courier", 16), 
                                                bg_color= ("#6188AF","#49338B"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
            label_titulo_entry.grid(row= 0, column= 1, padx= (5, 20), pady= 5, sticky= "ew") 
            self.lista_labels.append(label_titulo_entry)


            label_fundo_tempo = ctk.CTkLabel(frame_name_temp, height= 51, text= "", fg_color= ("#6188AF","#49338B"), corner_radius= 50)
            label_fundo_tempo.grid(row= 1 ,column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "ew")
            self.lista_labels.append(label_fundo_tempo)

            label_tempo = ctk.CTkLabel(frame_name_temp,text= "Tempo:",  text_color= "white", font= ("courier", 16), bg_color= ("#6188AF","#49338B"))
            label_tempo.grid(row= 1, column= 0, padx= (20, 0), pady= 5)
            self.lista_labels.append(label_tempo)

            label_tempo_entry = ctk.CTkLabel(frame_name_temp, height= 40, text= lista_tempos[x], font= ("courier", 16), 
                                                bg_color= ("#6188AF","#49338B"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
            label_tempo_entry.grid(row= 1, column= 1, padx= (5, 20), pady= 5, sticky= "ew")    
            self.lista_labels.append(label_tempo_entry)

            # widgets do frame_info =---------
            label_fundo_midias = ctk.CTkLabel(frame_info, text= "", fg_color= ("#6188AF","#49338B"), corner_radius= 20)
            label_fundo_midias.grid(row= 0, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")
            self.lista_labels.append(label_fundo_midias)

            label_midias = ctk.CTkLabel(frame_info,text= "Midias", font= ("courier", 16), bg_color= ("#6188AF","#49338B"))
            label_midias.grid(row= 0, column= 0, columnspan= 2, padx= 10, pady= 5)
            self.lista_labels.append(label_midias)

            textBox_midias = ctk.CTkTextbox(frame_info, height= 100, state= "disabled", bg_color= ("#6188AF","#49338B"))
            textBox_midias.grid(row= 1, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "ew")
            self.lista_labels.append(textBox_midias)


            label_fundo_categorias = ctk.CTkLabel(frame_info, text= "", fg_color= ("#6188AF","#49338B"), corner_radius= 20)
            label_fundo_categorias.grid(row= 2, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")
            self.lista_labels.append(label_fundo_categorias)

            label_categorias = ctk.CTkLabel(frame_info,text= "Categorias", font= ("courier", 16), bg_color= ("#6188AF","#49338B"))
            label_categorias.grid(row= 2, column= 0, columnspan= 2, padx= 10, pady= 5)
            self.lista_labels.append(label_categorias)

            textBox_categorias = ctk.CTkTextbox(frame_info, height= 100, state= "disabled", bg_color= ("#6188AF","#49338B"))
            textBox_categorias.grid(row= 3, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "ew")
            self.lista_labels.append(textBox_categorias)


            label_fundo_descricao = ctk.CTkLabel(frame_info, text= "", fg_color= ("#6188AF","#49338B"), corner_radius= 20)
            label_fundo_descricao.grid(row= 4, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")
            self.lista_labels.append(label_fundo_descricao)

            label_descricao = ctk.CTkLabel(frame_info,text= "Descricao", font= ("courier", 16), bg_color= ("#6188AF","#49338B"))
            label_descricao.grid(row= 4, column= 0, columnspan= 2, padx= 10, pady= 5)
            self.lista_labels.append(label_descricao)

            textBox_descricao = ctk.CTkTextbox(frame_info, height= 100, state= "disabled", bg_color= ("#6188AF","#49338B"))
            textBox_descricao.grid(row= 5, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "nsew")
            self.lista_labels.append(textBox_descricao)


            textBox_midias.configure(state= "normal")
            textBox_categorias.configure(state= "normal")
            textBox_descricao.configure(state= "normal")

            textBox_midias.delete(0.0, "end")
            textBox_categorias.delete(0.0, "end")
            textBox_descricao.delete(0.0, "end")

            textBox_midias.insert(0.0, text= "\n".join(lista_midias[x]))
            textBox_categorias.insert(0.0, text= "\n".join(lista_categorias[x]))
            if lista_descricoes[x] != "vazio":
                textBox_descricao.insert(0.0, text= lista_descricoes[x])

            textBox_midias.configure(state= "disabled")
            textBox_categorias.configure(state= "disabled")
            textBox_descricao.configure(state= "disabled")

    # metodo que limpa o frame dos posts inteiro
    def limpar_posts(self):
        for widget in self.frameConteudo.winfo_children():
            widget.destroy()
        
        self.lista_frames.clear()
        self.lista_labels.clear()
        self.lista_imgs.clear()

    # metodo que pega a foto de perfil com base no usuario recebido
    def pick_iconUser(self, usuario):
        usuarios = self.__dataset.get_perfils().get_usuarios().get_Usuario()
        icones = self.__dataset.get_perfils().get_fotoPerfil()
        
        for pos, usuario_referencia in enumerate(usuarios):
            if usuario == usuario_referencia:
                return icones[pos]
            
    # metodo que pega a img do desenho com base no usuario recebido
    def pick_img_from_user(self, usuario):
        usuarios = self.__dataset.get_perfils().get_usuarios().get_Usuario()
        icones = self.__dataset.get_perfils().get_fotoPerfil()
        
        for pos, usuario_referencia in enumerate(usuarios):
            if usuario == usuario_referencia:
                return icones[pos]
    
# =-----------------------------------------------------------------------------------=

# =------------------------= CLASSE DA TELA CADASTRO DE CLIENTES =--------------------------=
class Tela_registrarDesenhos(ctk.CTkFrame):
    # =- construtor -= =-----------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager
        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()

        self.grid(row= 0, column= 0, padx = 20, pady = 20, sticky = "nsew")
        self.grid_columnconfigure(0,weight= 0)
        self.grid_columnconfigure(1,weight= 1)
        self.grid_rowconfigure(0, weight= 1)

        # criando as sub Frames =------------------------------------------------------------=
        self.frameOpcoes = ctk.CTkFrame(self, width= 500, corner_radius= 0)
        self.frameOpcoes.grid(row=0, column= 0, rowspan= 2, sticky= "nsew")

        self.frameArquivoImg = ctk.CTkFrame(self, width= 900, corner_radius= 0)
        self.frameArquivoImg.grid(row=0, column=1, sticky= "nsew")

        # configurando elas
        self.frameOpcoes.grid_columnconfigure(1,weight= 1)
        self.frameOpcoes.grid_rowconfigure(7, weight= 1)
        self.frameOpcoes.grid_propagate(False)

        self.frameArquivoImg.grid_rowconfigure(0, weight= 1)
        self.frameArquivoImg.grid_columnconfigure(0, weight=1)
        self.frameArquivoImg.grid_propagate(False)

        # widgets fora dos subframes =-------------------------------------------------------------------------------------=
        self.label_resultado = ctk.CTkLabel(self, text= "", font = ("courier", 16), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.label_resultado.grid(row= 1, column= 1, columnspan= 2, padx= 20, pady = 10, sticky= "ew")

        # frame de opções widgets =-------------------------------------------------------------------------------------=
        # criando as labels / textboxs =------------------------------------------------------------=

        self.label_fundo_titulo = ctk.CTkLabel(self.frameOpcoes, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_titulo.grid(row= 0,column= 0, columnspan= 4, pady= 5, padx= 5, sticky= "nsew")
        
        self.label_titulo_desenho = ctk.CTkLabel(self.frameOpcoes, width= 70, text= "Titulo:", text_color= "white", font= ("courier", 12), bg_color= ("#979da2","#565b5e"))
        self.label_titulo_desenho.grid(row= 0, column= 0, pady= 10, padx = (10,0))


        self.label_fundo_tempo = ctk.CTkLabel(self.frameOpcoes, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_tempo.grid(row= 1,column= 0, columnspan= 4, pady= 5, padx= 5, sticky= "nsew")

        self.label_qtd_tempo = ctk.CTkLabel(self.frameOpcoes, width= 70, text= "Tempo(horas):", text_color= "white", font= ("courier", 12), bg_color= ("#979da2","#565b5e"))
        self.label_qtd_tempo.grid(row= 1, column= 0, pady= 10, padx = (10,0))

        
        self.label_fundo_midia = ctk.CTkLabel(self.frameOpcoes, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.label_fundo_midia.grid(row= 2, rowspan= 2, column= 0, columnspan= 2, pady= 5, padx= 5, sticky= "nsew")

        self.label_midia = ctk.CTkLabel(self.frameOpcoes, text= "Midia:", text_color= "white",font= ("courier", 12), bg_color= ("#979da2","#565b5e"))
        self.label_midia.grid(row= 2, column= 0, pady= 10, padx = (10,0))

        self.text_midia_resposta = []
        self.textBox_midia_resposta = ctk.CTkTextbox(self.frameOpcoes, width= 100, font= ("courier", 16), state= "disable", 
                                                     fg_color= ("#ebebeb","#242424"), bg_color= ("#979da2","#565b5e"))
        self.textBox_midia_resposta.grid(row= 3, column= 0, columnspan= 2, pady= (10, 20), padx = 20, sticky= "ew")


        self.label_fundo_categoria = ctk.CTkLabel(self.frameOpcoes, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.label_fundo_categoria.grid(row= 2, rowspan= 2, column= 2, columnspan= 2, pady= 5, padx= 5, sticky= "nsew")

        self.label_categoria = ctk.CTkLabel(self.frameOpcoes, text_color= "white", text= "Categoria:", font= ("courier", 12), bg_color= ("#979da2","#565b5e"))
        self.label_categoria.grid(row= 2, column= 2, pady= 10, padx = (10,0), )

        self.text_categoria_resposta = []
        self.textBox_categoria_resposta = ctk.CTkTextbox(self.frameOpcoes, font= ("courier", 16), state= "disable", 
                                                         fg_color= ("#ebebeb","#242424"), bg_color= ("#979da2","#565b5e"))
        self.textBox_categoria_resposta.grid(row= 3 , column= 2, columnspan= 2, pady= (10, 20), padx = 20, sticky= "ew")


        self.label_fundo_descricao = ctk.CTkLabel(self.frameOpcoes, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_descricao.grid(row= 6, rowspan= 2,column= 0, columnspan= 4, pady= 5, padx= 5, sticky= "nsew")

        self.label_descricao = ctk.CTkLabel(self.frameOpcoes, text= "Descrição", text_color= "white", bg_color= ("#979da2","#565b5e"), font= ("courier", 16))
        self.label_descricao.grid(row= 6, column= 0, columnspan= 4, pady= 5, padx= 5, sticky= "n")

        self.textBox_descricao = ctk.CTkTextbox(self.frameOpcoes, fg_color= ("#ebebeb","#242424"), bg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.textBox_descricao.grid(row= 7, column= 0, columnspan= 4, pady= (5,20), padx= 20, sticky= "nsew")

        # criando as entrys/comboBox =-----------------------------------------------------------=
        self.entry_titulo_desenho = ctk.CTkEntry(self.frameOpcoes, width= 200,placeholder_text= "titulo do desenho", corner_radius= 50, bg_color= ("#979da2","#565b5e"))
        self.entry_titulo_desenho.grid(row= 0, column=1, columnspan= 3, pady = 10, padx = (0, 20), sticky= "ew")

        self.entry_qtd_tempo = ctk.CTkEntry(self.frameOpcoes, width= 200,placeholder_text= "quantidade de tempo gasta", corner_radius= 50, bg_color= ("#979da2","#565b5e"))
        self.entry_qtd_tempo.grid(row= 1, column= 1,columnspan= 3,pady = 10, padx = (0, 20), sticky= "ew")

        lista_midias = ["...","Adobe Photoshop", "Adobe Ilustrator", "Procreate", "Adobe After Effects", 
                        "Grafite/Lapis", "Aquarela", "Nanquim", "Pintura a Oleo/Acrilica"]
        self.comboBox_midia = ctk.CTkComboBox(self.frameOpcoes, width= 100, corner_radius= 50, bg_color= ("#979da2","#565b5e"),
                                              values= lista_midias, command= self.selecionar_midias)
        self.comboBox_midia.grid(row=2,column=1,pady = 10, padx = 5)

        lista_categorias = ["...","Illustration", "Drawing", "Digital paiting", "Character Design", "Concept Art", "Storyboarding"]
        self.comboBox_categoria = ctk.CTkComboBox(self.frameOpcoes, width= 100, corner_radius= 50, bg_color= ("#979da2","#565b5e"),
                                                  values= lista_categorias, command= self.selecionar_categorias)
        self.comboBox_categoria.grid(row=2,column=3,pady = 10, padx = 5)

        # criando os buttons =-----------------------------------------------------------=
        self.botao_registrar = ctk.CTkButton(self.frameOpcoes, width= 200, text= "registrar",text_color= "white", fg_color=("#52CF6F","#333333"),
                                            hover_color= ("#208761","green"), border_color= ("white","green"), border_width=2, corner_radius= 50, command= self.set_button_registrar)
        self.botao_registrar.grid(row= 8, column= 0, columnspan=4, pady= 5, padx= 10)

        self.botao_clear = ctk.CTkButton(self.frameOpcoes, width= 200, text= "Limpar", text_color= "white", fg_color= ("#6188AF", "#333333"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B") ,command= self.limpar_entrys)
        self.botao_clear.grid(row=9, column= 0, columnspan=4,pady= 5, padx= 10)

        self.botao_sair = ctk.CTkButton(self.frameOpcoes, width= 200, text= "Voltar", text_color= "white", fg_color= ("#E66262","#333333"),
                                                        hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_button_MenuPrincipal)
        self.botao_sair.grid(row= 10, column= 0, columnspan=4,pady= 5, padx= 10)

        # frame de imagem widgets =-------------------------------------------------------------------------------------=
        # criando as labels =------------------------------------------------------------=
        self.label_ArquivoPath = ctk.CTkLabel(self.frameArquivoImg, width= 800,text="Nenhum arquivo selecionado",text_color= "white", anchor= "w",
                                              height= 36, font= ("courier", 10), corner_radius= 50, fg_color=("#6188AF","#491F67"))
        self.label_ArquivoPath.grid(row=1, column=0, pady = 5, padx=10, sticky= "ew")

        self.label_fundo_imagem = ctk.CTkLabel(self.frameArquivoImg, text= "", width= 800, height= 800,fg_color= ("#ebebeb","#242424"), corner_radius= 30)
        self.label_fundo_imagem.grid(row=0, column=0, pady= 5, padx= 10, sticky= "ew")

        self.label_imagem = ctk.CTkLabel(self.frameArquivoImg, width= 700, height= 100,text= "", bg_color= ("#ebebeb","#242424"))
        self.label_imagem.grid(row= 0,column = 0, pady= 10, padx = 10)

        # criando os buttons =-----------------------------------------------------------=
        self.botao_abrirArquivo = ctk.CTkButton(self.frameArquivoImg, text= "Abrir arquivo", height= 30,text_color= "white", fg_color=("#6188AF","#491F67"), bg_color=("#6188AF","#491F67"),
                                                hover_color="#49338B", border_width=2, border_color=("#dbdbdb","#2b2b2b"), corner_radius=50, command= self.selecionar_arquivo)
        self.botao_abrirArquivo.grid(row= 1, column= 0, pady = (5,0),padx = (0,30),sticky= "e")

    # =- funcionalidades do botoes -= =------------------------=
    # configurando o botao de voltar para voltar para o menu principal
    def set_button_MenuPrincipal(self):
        self.__app_manager.FrameAtual("menu_principal")

    # metodo que configura o botão de limpar todas as entrys e deixar o programa no estado padrão
    def limpar_entrys(self):
        self.label_ArquivoPath.configure(text="Nenhum arquivo selecionado")
        self.label_resultado.configure(text="")
        self.label_imagem.configure(image= "")

        self.entry_titulo_desenho.delete(0,"end")
        self.entry_qtd_tempo.delete(0,"end")

        self.text_midia_resposta = []
        self.text_categoria_resposta = []

        self.comboBox_midia.set(value= "...")
        self.comboBox_categoria.set(value= "...")

        self.textBox_categoria_resposta.configure(state= "normal")
        self.textBox_midia_resposta.configure(state= "normal")

        self.textBox_categoria_resposta.delete(0.0,"end")
        self.textBox_midia_resposta.delete(0.0,"end")
        self.textBox_descricao.delete(0.0,"end")

        self.textBox_categoria_resposta.configure(state= "disabled")
        self.textBox_midia_resposta.configure(state= "disabled")

    # configurando o botão de abrir arquivo para selecionar o arquivo da imagem
    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename (
        title = "Selecione um arquivo",
        filetypes = (("Imagens", "*.jpg;*.png"), ("Todos os arquivos", "*.*"))
        )

        if caminho:
            self.label_ArquivoPath.configure(text=f"{caminho}")
        else:
            self.label_ArquivoPath.configure(text="Nenhum arquivo selecionado")

        if self.label_ArquivoPath._text != "Nenhum arquivo selecionado":
            img_data = Image.open(self.label_ArquivoPath._text)
            img_recebida = ctk.CTkImage(light_image= img_data, dark_image= img_data, size= (img_data.width//2.5, img_data.height//2.5))

            self.label_imagem.configure(image= img_recebida)

    # comando que mostra as midias selecionadas
    def selecionar_midias(self, escolha):
        textbox = self.textBox_midia_resposta
        
        if escolha not in self.text_midia_resposta:
            if escolha == "...":
                textbox.delete("0.0", "end")
                return
            
            self.text_midia_resposta.append(escolha)
            

            textbox.configure(state="normal")
            
            textbox.delete("0.0", "end") 
            
            texto_final = "\n".join(self.text_midia_resposta)
            textbox.insert("0.0", texto_final)
            
            textbox.configure(state="disabled")

    # comando que mostra as categorias selecionadas
    def selecionar_categorias(self, escolha):
        textbox = self.textBox_categoria_resposta
        
        if escolha not in self.text_categoria_resposta:
            if escolha == "...":
                textbox.delete("0.0", "end")
                return
            self.text_categoria_resposta.append(escolha)
            
            textbox.configure(state="normal")
            
            textbox.delete("0.0", "end") 
            
            texto_final = "\n".join(self.text_categoria_resposta)
            textbox.insert("0.0", texto_final)
            
            textbox.configure(state="disabled")

    # comando que mostra as categorias selecionadas
    def set_button_registrar(self):
        usuario_atual = self.__dataset.get_usuarioAtual()[0]
        caminho_arquivo = self.label_ArquivoPath._text
        titulo = self.entry_titulo_desenho.get()
        qtd_tempo = self.entry_qtd_tempo.get()
        midias = self.text_midia_resposta
        categorias = self.text_categoria_resposta
        descricao = self.textBox_descricao.get("0.0", "end").strip().replace("\n", " ")

        label = self.label_resultado

        if titulo == "":
            label.configure(text = "Erro: campo titulo nao preenchido", text_color= "red")
            return

        if qtd_tempo == "none":
            qtd_tempo = "sem_resposta"
        elif qtd_tempo == "" or qtd_tempo.isalpha():
            label.configure(text = "Erro: campo tempo nao preenchido / nao é numero", text_color= "red")
            return
        
        if midias == []:
            label.configure(text = "Erro: nenhuma midia selecionada", text_color= "red")
            return
        
        if categorias == []:
            label.configure(text = "Erro: nenhuma categoria selecionada", text_color= "red")
            return
        
        if descricao == "":
            descricao = "vazio"

        if caminho_arquivo == "Nenhum arquivo selecionado":
            label.configure(text = "Erro: nenhum arquivo selecionado", text_color= "red")
            return

        self.__dataset.get_Desenhos().register_Drawing(usuario_atual, caminho_arquivo, titulo, qtd_tempo, midias, categorias, descricao)
        label.configure(text = "Registro feito com sucesso", text_color= "green")

        self.__dataset.get_perfils().update_Desenhos(usuario_atual, caminho_arquivo)
# =-----------------------------------------------------------------------------------=

# =--------------------------= CLASSE DA TELA SOBRE =----------------------------=
class Tela_Sobre(ctk.CTkFrame):
    # =- construtor -= =------------------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager

        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()

        self.grid(row= 0, column= 0, padx= 20, pady= 20, sticky= "nsew")
        self.grid_rowconfigure(0, weight= 1)
        self.grid_columnconfigure(0, weight= 1)

        # =- ScrollableFrame Principal -= =---------------------------------=
        self.Frame = ctk.CTkScrollableFrame(self, width= 1920, height= 700)
        self.Frame.grid(row=0, column= 0, sticky= "nsew")
        self.Frame.grid_columnconfigure(0, weight= 1)

        # =- Criando os sub frames -= =---------------------------------=
        self.frame_sobreMim = ctk.CTkFrame(self.Frame, height= 700, corner_radius= 0)
        self.frame_sobreMim.grid(row= 0, column= 0, padx= 10, pady= (10,0), sticky= "ew")
        self.frame_sobreMim.grid_columnconfigure(1, weight= 1)
        self.frame_sobreMim.grid_rowconfigure(1, weight= 1)

        self.frame_AppObjetivo = ctk.CTkFrame(self.Frame, height= 700, corner_radius= 0)
        self.frame_AppObjetivo.grid(row= 1, column= 0, padx= 10, sticky= "ew")
        self.frame_AppObjetivo.grid_columnconfigure(0, weight= 1)
        self.frame_AppObjetivo.grid_rowconfigure(1, weight= 1)
        self.frame_AppObjetivo.grid_propagate(False)

        self.frame_UsandoApp = ctk.CTkFrame(self.Frame, height= 700, corner_radius= 0)
        self.frame_UsandoApp.grid(row= 2, column= 0, padx= 10, pady= (0,10), sticky= "ew")
        self.frame_UsandoApp.grid_columnconfigure(0, weight= 1)
        self.frame_UsandoApp.grid_rowconfigure(1, weight= 1)
        self.frame_UsandoApp.grid_propagate(False)

        # =- Criando os widgets do frame SobreMim -= =---------------------------------------------------=
        # =- Criando as labels -= =---------------------------------=
        img_data = Image.open("img/foto_cracha.jpg")

        largura = 300
        altura = ((largura * img_data.height)//img_data.width)
        img = ctk.CTkImage(light_image= img_data, dark_image= img_data, size= (largura, altura))

        self.label_img = ctk.CTkLabel(self.frame_sobreMim, text= "", image= img)
        self.label_img.grid(row= 0, column= 0, padx= 20, pady= 20)

        self.label_nome = ctk.CTkLabel(self.frame_sobreMim, width= 300, text= "Gustavo Henrique Gonçalves", text_color= "white", 
                                       fg_color=("#6188AF","#49338B"), font= ("courier", 16), corner_radius= 50)
        self.label_nome.grid(row= 1, column= 0, padx= 5, pady= (0, 5))


        self.label_fundo_descricao = ctk.CTkLabel(self.frame_sobreMim, text= "", fg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_fundo_descricao.grid(row= 0, rowspan= 3, column= 1, padx= 20, pady= 20, sticky= "nsew")

        self.label_descricao = ctk.CTkLabel(self.frame_sobreMim,text= "Um pouco sobre mim...", text_color= "white", font= ("courier", 32),
                                            bg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_descricao.grid(row= 0, rowspan= 3, column= 1, padx = 20, pady= (30, 0), sticky= "n")


        texto_sobreMim = """        Olá, muito prazer! Eu sou o Gustavo Henrique Gonçalves, tenho 19 anos e sou um grande entusiasta do mundo da programação. Atualmente, curso Engenharia de Computação na Universidade Tecnológica Federal do Paraná (UTFPR), onde venho construindo uma base sólida para me tornar o profissional que desejo ser no futuro. 
        Meu principal objetivo hoje é me consolidar no desenvolvimento de softwares. Tenho uma afinidade maior pela área de Front-End, pois gosto muito da parte visual e da experiência de transformar ideias em algo que as pessoas podem ver e interagir. É o que mais me desperta interesse e onde dedico boa parte dos meus estudos atuais. No entanto, minha formação como engenheiro me dá uma visão ampla sobre a tecnologia. Por isso, não tenho dificuldades em lidar com o Back-End e, sempre que o projeto exige, consigo atuar como Full-Stack."""
        self.TextBox_descricao = ctk.CTkTextbox(self.frame_sobreMim,  font= ("courier", 16),
                                            bg_color= ("#6188AF", "#49338B"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.TextBox_descricao.grid(row= 0, rowspan= 3, column= 1, padx = 40, pady= (80, 40), sticky= "nsew")

        self.TextBox_descricao.configure(state= "normal")
        self.TextBox_descricao.insert(0.0, texto_sobreMim)
        self.TextBox_descricao.configure(state= "disabled")

        # =- Criando os buttons -= =---------------------------------=
        self.botao_sair = ctk.CTkButton(self.frame_sobreMim, text= "Voltar", text_color= "white", fg_color= ("#E66262","#333333"),
                                                        hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_button_MenuPrincipal)
        self.botao_sair.grid(row= 2, column= 0, pady= (5, 10), padx= 10)

        # =- Criando os widgets do frame AppObjetivo -= =---------------------------------------------------=
        # =- Criando as labels -= =---------------------------------=
        self.label_fundo_objetivo = ctk.CTkLabel(self.frame_AppObjetivo, text= "", fg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_fundo_objetivo.grid(row= 0, rowspan= 2, column= 0,padx= 20, pady= 20, sticky= "nsew")

        self.label_objetivo = ctk.CTkLabel(self.frame_AppObjetivo,text= "Objetivo do Projeto", text_color= "white", font= ("courier", 32),
                                            bg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_objetivo.grid(row= 0, column= 0, padx = 20, pady= (30, 0), sticky= "n")

        texto_sobreApp = """        Este projeto nasceu da vontade de criar um espaço dedicado à organização e exposição de trabalhos criativos. A ideia original e o objetivo final para este software é que ele funcione como uma rede social voltada para artistas, permitindo que vários usuários se conectem, compartilhem suas obras e interajam em um ambiente comum.

        Por estar nos estágios iniciais de desenvolvimento e como ainda estou explorando a implementação de servidores e bancos de dados externos, o projeto atualmente funciona de forma local. Isso significa que, por enquanto, ele foca na experiência individual do usuário e na gestão de seus próprios conteúdos, servindo como um protótipo sólido do que virá a ser a plataforma completa.

        Para a construção da interface e das funcionalidades, busquei inspiração em grandes referências que admiro, como o Behance e o ArtStation, pelo foco profissional em portfólios, além do Pinterest e Instagram, pela forma dinâmica e visual de navegar por imagens. Este software é, acima de tudo, um laboratório onde aplico meus conhecimentos de Engenharia de Computação para criar uma ferramenta que une funcionalidade e estética para a comunidade artística."""

        self.TextBox_objetivo = ctk.CTkTextbox(self.frame_AppObjetivo,  font= ("courier", 16),
                                            bg_color= ("#6188AF", "#49338B"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.TextBox_objetivo.grid(row= 1, column= 0, padx = 40, pady= (30, 40), sticky= "nsew")

        self.TextBox_objetivo.configure(state= "normal")
        self.TextBox_objetivo.insert(0.0, texto_sobreApp)
        self.TextBox_objetivo.configure(state= "disabled")

        # =- Criando os widgets do frame AppObjetivo -= =---------------------------------------------------=
        # =- Criando as labels -= =---------------------------------=
        self.label_fundo_modoUso = ctk.CTkLabel(self.frame_UsandoApp, text= "", fg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_fundo_modoUso.grid(row= 0, rowspan= 2, column= 0,padx= 20, pady= 20, sticky= "nsew")

        self.label_modoUso = ctk.CTkLabel(self.frame_UsandoApp,text= "Como utilizar o app", text_color= "white", font= ("courier", 32),
                                            bg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_modoUso.grid(row= 0, column= 0, padx = 20, pady= (30, 0), sticky= "n")

        texto_modoUso = """Este software foi projetado para ser simples e intuitivo. Abaixo, explico como aproveitar cada funcionalidade das nossas telas:

Acesso e Cadastro: Tudo começa na tela de Login. Se você já possui uma conta, basta entrar com suas credenciais. Caso contrário, o proprio sistema ja garante pelo menos um novo usuario caso não exista um anterior, mas caso o usuario ainda queira cadastrar um novo, a tela de Login permite que você crie um novo perfil para começar a organizar sua galeria, basta antes de clicar em entrar, clicar no botão de cadastrar que ele então deixara você colocar um novo usuario e uma nova senha para ser salva.
Uma obsercação importante é que para que o programa realmente funcione, as pastas "database" e "img" precisam existir, o "database" para que o sistema salve os arquivos dentro dela as informações dos perfils e da lista de desenhos, e "img" para guardar as imagens que serão utilizadas.

Usuario já existente no sistema: usuario: usuario1 // senha: senha1 
Modo Cadastro: Ao clicar no botão cadastro, ele muda para o modo cadastro, a partir disso, ele pede um novo usuario e senha para serem digitados, depois ao clicar no botão de entrar, esse novo usuario e senha é salvo n o sistema

Menu Principal: É o seu painel de controle. A partir daqui, você pode visualizar os desenhos já registrados dos outros usuarios e acessar as outras áreas do sistema.

Registro de Desenhos: Esta é a área onde você imortaliza sua arte. Ao cadastrar um novo trabalho, você pode dar um título, quantidade de tempo gasta em horas, selecionar as mídias utilizadas, definir as categorias e uma descrição a sua arte.
Dicas de Preenchimento: Tempo Gasto: Se você não se lembra ou não marcou o tempo levado para concluir o desenho, não se preocupe! Basta escrever 'none' no campo de tempo e o sistema registrará automaticamente como 'sem_resposta'.
Descrição: A descrição é opcional. Se quiser deixar o foco apenas no visual, pode registrar seu desenho sem texto descritivo que o sistema processará normalmente.

Navegação e Portfólio: Na tela de perfil, você pode dar uma olhada na sua galeria, sendo os post ordenados do ultimo registro até o primeiro registro. Ao clicar em um dos desenhos do seu portfólio, você verá as informações registradas por você, além de poder passar para os desenhos anteriores/seguintes a ele.

Perfil: Ainda na tela do seu perfil, você também pode personalizar seu espaço, editando sua bio e foto de perfil para que o app tenha a sua cara, além de mudar o nome do seu usuario e da sua senha.

O objetivo é que você foque na sua arte, enquanto o sistema cuida da organização!"""

        self.TextBox_modoUso = ctk.CTkTextbox(self.frame_UsandoApp,  font= ("courier", 16),
                                            bg_color= ("#6188AF", "#49338B"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.TextBox_modoUso.grid(row= 1, column= 0, padx = 40, pady= (30, 40), sticky= "nsew")

        self.TextBox_modoUso.configure(state= "normal")
        self.TextBox_modoUso.insert(0.0, texto_modoUso)
        self.TextBox_modoUso.configure(state= "disabled")

    # =- funcionalidade dos botoes -= =---------------------------------=
    # configurando o botao de voltar para voltar para o menu principal
    def set_button_MenuPrincipal(self):
        self.__app_manager.FrameAtual("menu_principal")


# =--------------------------= CLASSE DA TELA DE PERFIL DO USUARIO =----------------------------=
class Tela_perfilUsuario(ctk.CTkFrame):
    # =- construtor -= =------------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager

        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()

        self.grid(row= 0, column= 0, padx = 20, pady = 20, sticky = "nsew")
        self.grid_columnconfigure(0, weight= 1)
        self.grid_rowconfigure(0, weight= 1)

        # =- criando o scrowllableFrame e colocando ele no frame inteiro do perfilUsuario -= =----------------------------------------=
        self.Frame = ctk.CTkScrollableFrame(self, width= 1920, height= 700)
        self.Frame.grid(row=0, column= 0, sticky= "nsew")
        self.Frame.grid_columnconfigure(0, weight= 1)
        self.Frame.grid_rowconfigure(1, weight= 1)

        # =- criando os sub Frames (dividindo entre os dados do usuario e os posts dele) -= =----------------------------------------=
        self.frameInfoAccount = ctk.CTkFrame(self.Frame, height= 300)
        self.frameInfoAccount.grid(row=0, column=0, sticky= "ew")
        self.frameInfoAccount.grid_columnconfigure(2, weight= 1)
        self.frameInfoAccount.grid_propagate(True)

        self.framePostDesenhos = ctk.CTkFrame(self.Frame)
        self.framePostDesenhos.grid(row=1, column= 0, sticky= "nsew")
        self.framePostDesenhos.grid_rowconfigure(0, weight= 1)
        self.framePostDesenhos.grid_propagate(True)

        # =- criando os widgets do Frame Info Account -= =----------------------------------------=
        # =- criando as labels / textboxs -= =----------------------------------------=
        self.label_icon = ctk.CTkLabel(self.frameInfoAccount, text= "", corner_radius= 100)
        self.label_icon.grid(row=0, rowspan= 2, column=0, padx= 20, pady= 20, sticky= "w")

        self.label_nome_usuario = ctk.CTkLabel(self.frameInfoAccount, width= 200, text="", text_color= "white", font= ("courier", 32), fg_color= ("#6188AF", "#49338B"),
                                               corner_radius= 50)
        self.label_nome_usuario.grid(row=2, column= 0, padx= 20, pady= (0,20))


        self.label_fundo_descricao = ctk.CTkLabel(self.frameInfoAccount, text= "", fg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_fundo_descricao.grid(row= 0, rowspan= 3, column= 2, padx= 20, pady= 10,sticky= "nsew")

        self.label_descricao = ctk.CTkLabel(self.frameInfoAccount, text= "Descrição", text_color= "White", font= ("courier", 16), bg_color= ("#6188AF", "#49338B"))
        self.label_descricao.grid(row= 0, rowspan= 3, column= 2, padx= 20, pady= 20, sticky= "n")

        self.textbox_bio = ctk.CTkTextbox(self.frameInfoAccount, font= ("courier", 16), bg_color= ("#6188AF", "#49338B"),corner_radius= 50)
        self.textbox_bio.grid(row= 0, rowspan= 3, column= 2, padx= 40, pady= (50, 20), sticky= "nsew")

        # =- criando as buttons -= =----------------------------------------=
        self.botao_alterarFoto_perfil = ctk.CTkButton(self.frameInfoAccount, width= 200, text= "Editar foto de Perfil", text_color= "white", fg_color= ("#6188AF", "#333333"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B"), command= self.set_botao_editarIcon)
        self.botao_alterarFoto_perfil.grid(row=0, rowspan= 2, column= 1, pady= (0,60))

        self.botao_alterarInfoPerfil = ctk.CTkButton(self.frameInfoAccount, width= 200, text= "Editar Perfil", text_color= "white", fg_color= ("#6188AF", "#333333"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B"), command= self.set_botao_editarPerfil)
        self.botao_alterarInfoPerfil.grid(row=0, rowspan= 2, column= 1)

        self.botao_sair = ctk.CTkButton(self.frameInfoAccount, width= 200, text= "Voltar", text_color= "white", fg_color= ("#E66262","#333333"),
                                                        hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_botao_sair)
        self.botao_sair.grid(row=0, rowspan= 2, column= 1, pady= (60,0))

        # =- criando as variaveis necessarias do FramePostDesenhos -= =----------------------------------------=
        self.frames_colunas = []
        self.posts_images = []
        self.posts_buttons = []

    # =- funcionalidades do botoes -= =------------------------=
    # configurando o botao de voltar para voltar para o menu principal
    def set_botao_sair(self):
        self.update_Bio()
        self.limpar_posts()

        self.__app_manager.FrameAtual("menu_principal")

    # configurando o botao de editar perfil para ir para a tela de editar perfil 
    def set_botao_editarPerfil(self):
        self.update_Bio()
        self.__app_manager.frames["perfil_usuario_edicao"].limpar_entrys()
        self.__app_manager.FrameAtual("perfil_usuario_edicao")

    # configurando o botao de editar foto de perfil para escolher uma foto nova de perfil 
    def set_botao_editarIcon(self):
        caminho = filedialog.askopenfilename (
        title = "Selecione um arquivo",
        filetypes = [("Imagens", "*.jpg;*.png")]
        )

        if caminho:
            img_data = Image.open(caminho)
            img_recebida = ctk.CTkImage(light_image= img_data, dark_image= img_data, size= (img_data.width//4, img_data.height//4))

            self.label_icon.configure(image= img_recebida)
        else:
            print("=- erro ao abrir a foto do arquivo")
            return
        
        usuario_atual = self.__dataset. get_usuarioAtual()[0]
        
        self.__dataset.get_perfils().set_fotoPerfil(usuario_atual, caminho)

    # configurando o botao dos posts para que ele mude para a tela das informações dos posts 
    def set_botao_posts(self, img, desenhos):
        self.__app_manager.frames["posts_info"].set_img_info(img, desenhos)
        self.__app_manager.FrameAtual("posts_info")
        

    # =- metodos -= =------------------------=
    # metodo que atualiza a bio nos arquivos 
    def update_Bio(self):
        usuario_atual = self.__dataset. get_usuarioAtual()[0]
        bio = self.textbox_bio.get(0.0, "end").strip()

        self.__dataset.get_perfils().set_Bio(usuario_atual, bio)

    # metodo que escolhe a foto de usuario com base no usuario atual 
    def pick_iconUser(self):
        usuarios = self.__dataset.get_perfils().get_usuarios().get_Usuario()
        icones = self.__dataset.get_perfils().get_fotoPerfil()
        usuario_atual = self.__dataset.get_usuarioAtual()[0]
        if usuario_atual == None:
            print("=- usuario atual nao existente no momento")
            return None
        
        for pos, usuario in enumerate(usuarios):
            if usuario_atual == usuario:
                return icones[pos]
            
    # metodo que atualiza a tela de perfil 
    def update_telaPerfil(self):
        img_icon_usuario_data = Image.open(self.pick_iconUser())

        largura= 300
        altura = ((largura * img_icon_usuario_data.height)//img_icon_usuario_data.width)

        img_icon_usuario = ctk.CTkImage(light_image= img_icon_usuario_data, dark_image= img_icon_usuario_data, size= (largura, altura))
        self.label_icon.configure(image= img_icon_usuario)

        usuarios = self.__dataset.get_perfils().get_usuarios().get_Usuario()
        usuario_atual = self.__dataset.get_usuarioAtual()[0]
        bios = self.__dataset.get_perfils().get_bio()
        self.textbox_bio.delete(0.0,"end")
        self.desenhos = []

        for pos, usuario in enumerate(usuarios):
            if usuario_atual == usuario:
                self.label_nome_usuario.configure(text= usuario)
                if bios[pos] == "...":
                    return
                else:
                    self.textbox_bio.insert("0.0",bios[pos])

        self.__app_manager.frames["menu_principal"].botao_usuario.configure(text= usuario_atual)
        self.add_posts()

    # metodo que adiciona os post na tela 
    def add_posts(self):
        column_limit = 3
        usuario_atual = self.__dataset.get_usuarioAtual()[0]
        desenhos = []
        desenhos = self.__dataset.get_perfils().get_desenhos_from_usuario(usuario_atual)

        if desenhos[0] == "None":
            return

        largura = 482
        for x in range(column_limit):
            self.frames_colunas.append(ctk.CTkFrame(self.framePostDesenhos, width= largura, corner_radius= 0))
            self.frames_colunas[x].grid(row= 0, column= x, sticky= "ns")

        y = 0
        for x in range(len(desenhos)):
            img_data = Image.open(desenhos[-(x+1)]) # --> fazendo isso para que os primeiros post sejam os ultimos registros feitos pelo usuario
            img_post = ctk.CTkImage(light_image= img_data, dark_image= img_data, 
                                            size= (largura, (img_data.height * largura)//img_data.width))


            button_img = ctk.CTkButton(self.frames_colunas[y], text= "", image= img_post, fg_color=("#6188AF","#49338B"), 
                                       hover_color= "white", corner_radius= 0, command= lambda p=desenhos[-(x+1)]: self.set_botao_posts(p, desenhos))
            button_img.pack()

            self.posts_images.append(img_post) 
            self.posts_buttons.append(button_img)
            y += 1
            if y == column_limit:
                y = 0

    # metodo que limpa o frame inteiro dos posts 
    def limpar_posts(self):
        for widget in self.framePostDesenhos.winfo_children():
            widget.destroy()
        
        self.posts_buttons.clear()
        self.posts_images.clear()
        self.frames_colunas.clear()

# =-----------------------------------------------------------------------------------=
 
# =--------------------------= CLASSE DA TELA DE EDIÇÃO DAS INFORMAÇÕES DO USUARIO =----------------------------=
class Tela_perfilUsuario_Editar(ctk.CTkFrame):
    # =- construtor -= =--------------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager

        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()

        self.grid(row=0,column=0, padx= 20, pady= 20, sticky= "nsew")
        self.grid_columnconfigure(1, weight= 1)
        self.grid_columnconfigure(2, weight= 1)
        self.grid_rowconfigure(9,weight= 1)

        # =- criando as labels -= =----------------------------------------=
        self.label_Tela_Edicao = ctk.CTkLabel(self, width= 900,height= 100, text= "INFORMAÇÕES DO USUARIO", text_color= "White", font= ("courier", 48), 
                                              fg_color= ("#6188AF", "#49338B"), corner_radius= 50)
        self.label_Tela_Edicao.grid(row= 0, column= 0, columnspan= 2, pady= 20, sticky= "w")

        self.label_preenchimento= ctk.CTkLabel(self, width= 120, height=100, text= "",bg_color= ("#6188AF", "#49338B"))
        self.label_preenchimento.grid(row= 0, column= 0, sticky= "w")

        self.label_detalhe = ctk.CTkLabel(self, text= "", bg_color= ("#6188AF", "#49338B"))
        self.label_detalhe.grid(row= 0, rowspan= 10, column= 2, sticky= "nsew")


        self.label_fundo_usuario_antigo = ctk.CTkLabel(self,height= 52,width= 780,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_usuario_antigo.grid(row= 1, column= 0, columnspan= 2, pady= (20, 5), padx= (20, 0), sticky= "w")

        self.label_preenchimento_userAntigo = ctk.CTkLabel(self, width= 50, height=51, text= "",bg_color= ("#979da2","#565b5e"))
        self.label_preenchimento_userAntigo.grid(row= 1, column= 0, pady= (20, 5) ,sticky= "w")

        self.label_usuario_antigo = ctk.CTkLabel(self, text= "Usuario Antigo:", text_color= "white", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_usuario_antigo.grid(row= 1, column= 0, padx= (20,10), pady= (20, 5))

        self.label_fundo_usuario_novo = ctk.CTkLabel(self,height= 52,width= 780,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_usuario_novo.grid(row= 2, column= 0, columnspan= 2, pady= (5, 20), padx= (20, 0), sticky= "w")

        self.label_preenchimento_userNovo = ctk.CTkLabel(self, width= 50, height=51, text= "",bg_color= ("#979da2","#565b5e"))
        self.label_preenchimento_userNovo.grid(row= 2, column= 0, pady= (5, 20) ,sticky= "w")

        self.label_usuario_novo = ctk.CTkLabel(self, text= "Usuario Novo:", text_color= "white", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_usuario_novo.grid(row= 2, column= 0, padx= (20,10), pady= (5, 20))


        self.label_fundo_senha_antiga = ctk.CTkLabel(self,height= 52,width= 780,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_senha_antiga.grid(row= 3, column= 0, columnspan= 2,pady= (20, 5), padx= (20, 0), sticky= "w")

        self.label_preenchimento_senhaAntiga = ctk.CTkLabel(self, width= 50, height=51, text= "",bg_color= ("#979da2","#565b5e"))
        self.label_preenchimento_senhaAntiga.grid(row= 3, column= 0, pady= (20, 5) ,sticky= "w")

        self.label_senha_antiga = ctk.CTkLabel(self, text= "senha antiga:", text_color= "white", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_senha_antiga.grid(row= 3, column= 0, padx= (20,10),pady= (20, 5))

        self.label_fundo_senha_nova = ctk.CTkLabel(self,height= 52,width= 780,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_senha_nova.grid(row= 4, column= 0, columnspan= 2,pady= (5, 5), padx= (20, 0), sticky= "w")

        self.label_preenchimento_senhaNova = ctk.CTkLabel(self, width= 50, height=51, text= "",bg_color= ("#979da2","#565b5e"))
        self.label_preenchimento_senhaNova.grid(row= 4, column= 0, pady= (5, 5) ,sticky= "w")

        self.label_senha_nova = ctk.CTkLabel(self, text= "senha Nova:", text_color= "white", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_senha_nova.grid(row= 4, column= 0, padx= (20,10),pady= (5, 5))

        self.label_fundo_senha_nova_confirma = ctk.CTkLabel(self,height= 52,width= 780,text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_senha_nova_confirma.grid(row= 5, column= 0, columnspan= 2,pady= (5, 5), padx= (20, 0), sticky= "w")

        self.label_preenchimento_senhaConfirma = ctk.CTkLabel(self, width= 50, height=51, text= "",bg_color= ("#979da2","#565b5e"))
        self.label_preenchimento_senhaConfirma.grid(row= 5, column= 0, pady= (5, 5) ,sticky= "w")

        self.label_senha_nova_confirma = ctk.CTkLabel(self, text= "Confirma Senha:", text_color= "white", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_senha_nova_confirma.grid(row= 5, column= 0, padx= (20,10),pady= (5, 5))

        self.label_resultado = ctk.CTkLabel(self, text= "", height= 30, font= ("courier", 16))
        self.label_resultado.grid(row=8, column= 0, columnspan= 2, pady= (5,5), padx= (200, 50), sticky= "w")

        # =- criando as entrys -= =----------------------------------------=
        self.entry_usuario_antigo = ctk.CTkEntry(self, width= 600, height= 50, placeholder_text= "Digite o Usuario Antigo", corner_radius= 50, font= ("courier", 16),
                                                 bg_color= ("#979da2","#565b5e"))
        self.entry_usuario_antigo.grid(row= 1, column= 1, pady= (20, 5), padx= (0, 20), sticky= "w")

        self.entry_usuario_novo = ctk.CTkEntry(self, width= 600, height= 50, placeholder_text= "Digite o Usuario Novo", corner_radius= 50, font= ("courier", 16),
                                               bg_color= ("#979da2","#565b5e"))
        self.entry_usuario_novo.grid(row= 2, column= 1, pady= (5, 20), padx= (0, 20), sticky= "w")


        self.entry_senha_antiga = ctk.CTkEntry(self, width= 600, height= 50, placeholder_text= "Digite a senha antiga", corner_radius= 50, font= ("courier", 16),
                                                 bg_color= ("#979da2","#565b5e"), show= "*")
        self.entry_senha_antiga.grid(row= 3, column= 1, pady= (20, 5), padx= (0, 20), sticky= "w")
        self.visualizacao_senha_antiga = ctk.BooleanVar(value=False)

        self.entry_senha_nova = ctk.CTkEntry(self, width= 600, height= 50, placeholder_text= "Digite a senha nova", corner_radius= 50, font= ("courier", 16),
                                               bg_color= ("#979da2","#565b5e"), show= "*")
        self.entry_senha_nova.grid(row= 4, column= 1, pady= (5, 5), padx= (0, 20), sticky= "w")
        self.visualizacao_senha_nova = ctk.BooleanVar(value=False)

        self.entry_senha_confirma = ctk.CTkEntry(self, width= 600, height= 50, placeholder_text= "Confirme a senha nova", corner_radius= 50, font= ("courier", 16),
                                               bg_color= ("#979da2","#565b5e"), show= "*")
        self.entry_senha_confirma.grid(row= 5, column= 1, pady= (5, 5), padx= (0, 20), sticky= "w")
        self.visualizacao_senha_confirma = ctk.BooleanVar(value=False)

        # =- criando as buttons -= =----------------------------------------=
        self.botao_registrar = ctk.CTkButton(self, width= 400, height= 30, text= "Salvar Alterações",text_color= "white", fg_color=("#52CF6F","#333333"),
                                            hover_color= ("#208761","green"), border_color= ("white","green"), border_width=2, command= self.set_botao_salvarAlteracoes)
        self.botao_registrar.grid(row= 6, column= 0, columnspan= 2,pady= (5,5), padx= (200, 50), sticky= "w")

        self.botao_clear = ctk.CTkButton(self, width= 400, height= 30, text= "Limpar", text_color= "white", fg_color= ("#6188AF", "#333333"),
                                         hover_color="#49338B", border_width= 2, border_color=("white","#49338B"), command= self.limpar_entrys)
        self.botao_clear.grid(row=7, column= 0, columnspan= 2,pady= (5,5), padx= (200, 50), sticky= "w")

        self.botao_sair = ctk.CTkButton(self, width= 400, height= 30, text= "Voltar", text_color= "white", fg_color= ("#E66262","#333333"),
                                                        hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_botao_sair)
        self.botao_sair.grid(row=9, column= 0, columnspan= 2,pady= (5,10), padx= (200, 50), sticky= "sw")

        self.dot_button_show_antiga = ctk.CTkCheckBox(self, width= 10,text= "", variable= self.visualizacao_senha_antiga, bg_color= ("#f9f9fa","#343638"),
                                                      command= self.set_checkBox_antiga)
        self.dot_button_show_antiga.grid(row= 3, column = 1, pady= (20, 5), padx= (540,0),sticky= "w")

        self.dot_button_show_nova = ctk.CTkCheckBox(self, width= 10,text= "", variable= self.visualizacao_senha_nova, bg_color= ("#f9f9fa","#343638"),
                                                    command= self.set_checkBox_nova)
        self.dot_button_show_nova.grid(row= 4, column = 1, pady= (5,5), padx= (540,0),sticky= "w")

        self.dot_button_show_confirma = ctk.CTkCheckBox(self, width= 10,text= "", variable= self.visualizacao_senha_confirma, bg_color= ("#f9f9fa","#343638"),
                                                        command= self.set_checkBox_confirma)
        self.dot_button_show_confirma.grid(row= 5, column = 1, pady= (5,20), padx= (540,0),sticky= "w")

    # =- funcionalidades do botoes -= =------------------------=
    # configurando o botão de voltar para voltar para a tela de perfil
    def set_botao_sair(self):
        self.__app_manager.FrameAtual("perfil_usuario")

    # configurando o botão de salvar para salvar as alterações feitas
    def set_botao_salvarAlteracoes(self):
        usuario_antigo = self.entry_usuario_antigo.get()
        usuario_novo = self.entry_usuario_novo.get()

        senha_antiga = self.entry_senha_antiga.get()
        senha_nova = self.entry_senha_nova.get()
        senha_confirma = self.entry_senha_confirma.get()

        texto = "Alteracoes salvas com sucesso"

        if usuario_antigo == "":
            texto = "Erro: campo Usuario antigo nao preenchido"
            self.label_resultado.configure(text= texto, text_color= "red")
            return
        if usuario_antigo != self.__dataset.get_usuarioAtual()[0]:
            texto = "Erro: campo Usuario antigo esta incorreto"
            self.label_resultado.configure(text= texto, text_color= "red")
            return

        if usuario_novo == "":
            texto = "Erro: campo Usuario novo nao preenchido"
            self.label_resultado.configure(text= texto, text_color= "red")
            return


        if senha_antiga == "":
            texto = "Erro: campo Senha antiga nao preenchida"
            self.label_resultado.configure(text= texto, text_color= "red")
            return
        if senha_antiga != self.__dataset.get_usuarioAtual()[1]:
            texto = "Erro: campo Senha antiga esta incorreta"
            self.label_resultado.configure(text= texto, text_color= "red")
            return

        if senha_nova == "":
            texto = "Erro: campo Senha nova nao preenchida"
            self.label_resultado.configure(text= texto, text_color= "red")
            return
        if senha_confirma == "":
            texto = "Erro: campo Confirma Senha nao preenchida"
            self.label_resultado.configure(text= texto, text_color= "red")
            return
        if senha_nova != senha_confirma:
            texto = "Erro: campo Confirma Senha diferente do campo Senha nova"
            self.label_resultado.configure(text= texto, text_color= "red")
            return

        self.__dataset.get_perfils().update_usuarios(usuario_antigo, senha_antiga, usuario_novo, senha_nova)
        self.__dataset.get_Desenhos().update_userName_inListaDesenhos(usuario_antigo, usuario_novo)

        self.label_resultado.configure(text= texto, text_color= "green")
        self.__dataset.set_usuarioAtual(usuario_novo, senha_nova)
        self.__app_manager.frames["perfil_usuario"].update_telaPerfil()


    # configurando a check box da senha antiga
    def set_checkBox_antiga(self):
        status = self.visualizacao_senha_antiga
        entry = self.entry_senha_antiga

        if status.get():
            entry.configure(show= "")
        else:
            entry.configure(show= "*")

    # configurando a check box da senha nova
    def set_checkBox_nova(self):
        status = self.visualizacao_senha_nova
        entry = self.entry_senha_nova

        if status.get():
            entry.configure(show= "")
        else:
            entry.configure(show= "*")

    # configurando a check box da confirmação da senha
    def set_checkBox_confirma(self):
        status = self.visualizacao_senha_confirma
        entry = self.entry_senha_confirma

        if status.get():
            entry.configure(show= "")
        else:
            entry.configure(show= "*")

    # metodo que configura o botão de limpar todas as entrys e deixar o programa no estado padrão
    def limpar_entrys(self):
        self.entry_usuario_antigo.delete(0,"end")
        self.entry_usuario_novo.delete(0,"end")

        self.entry_senha_antiga.delete(0, "end")
        self.entry_senha_nova.delete(0, "end")
        self.entry_senha_confirma.delete(0, "end")

        self.dot_button_show_antiga.deselect()
        self.entry_senha_antiga.configure(show="*")

        self.dot_button_show_nova.deselect()
        self.entry_senha_nova.configure(show="*")

        self.dot_button_show_confirma.deselect()
        self.entry_senha_confirma.configure(show="*")

        self.label_resultado.configure(text= "")

# =-----------------------------------------------------------------------------------=

# =--------------------------= CLASSE DA TELA DE EDIÇÃO DAS INFORMAÇÕES DO USUARIO =----------------------------=
class Tela_PostsInfo(ctk.CTkFrame):
    # =- construtor -= =----------------------=
    def __init__(self, app_manager):
        self.__app_manager = app_manager

        super().__init__(self.__app_manager)

        self.__dataset = self.__app_manager.get_Dataset()
        self.lista_desenhos = []
        self.indice_atual = 0
        self.indice_ant = 0
        self.indice_pos = 0

        self.grid(row= 0, column = 0, padx= 20, pady= 20, sticky= "nsew")
        self.grid_columnconfigure(0, weight= 0)
        self.grid_columnconfigure(1, weight= 1)
        self.grid_columnconfigure(2, weight= 0)
        self.grid_rowconfigure(0, weight= 1)
 
        # =- Criando sub Frame -= =-----------------------------------------------=
        self.Frame_post = ctk.CTkFrame(self)
        self.Frame_post.grid(row= 0, column= 1, padx= 40, pady= 40,sticky= "nsew")
        self.Frame_post.grid_rowconfigure(0, weight= 1)
        self.Frame_post.grid_columnconfigure(0, weight= 1)
        self.Frame_post.grid_columnconfigure(1, weight= 0)

        self.Frame_img = ctk.CTkScrollableFrame(self.Frame_post, corner_radius= 0, fg_color= ("#ebebeb","#242424"))
        self.Frame_img.grid(row= 0, column= 0, sticky= "nsew")
        self.Frame_img.grid_columnconfigure(0, weight= 1)

        self.Frame_Conteudo = ctk.CTkScrollableFrame(self.Frame_post, width= 400,corner_radius= 0)
        self.Frame_Conteudo.grid(row= 0, column= 1,sticky= "nse")
        self.Frame_Conteudo.grid_columnconfigure(1, weight= 1)
        self.Frame_Conteudo.grid_rowconfigure(7, weight= 1)

        # =- Criando labels no frame_img -= =-----------------------------------------------=
        self.label_img = ctk.CTkLabel(self.Frame_img, width= 600, text= "", image= None)
        self.label_img.grid(row= 0, column= 0, padx = 10, pady= 10)

        # =- Criando labels no frame_conteudo -= =-----------------------------------------------=
        self.label_fundo_titulo = ctk.CTkLabel(self.Frame_Conteudo, height= 51, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_titulo.grid(row= 0 ,column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "ew")

        self.label_titulo = ctk.CTkLabel(self.Frame_Conteudo,text= "Titulo:", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_titulo.grid(row= 0, column= 0, padx= (20, 0), pady= 5)

        self.label_titulo_entry = ctk.CTkLabel(self.Frame_Conteudo,text= "", height= 40, font= ("courier", 16), 
                                               bg_color= ("#979da2","#565b5e"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.label_titulo_entry.grid(row= 0, column= 1, padx= (5, 20), pady= 5, sticky= "ew") 


        self.label_fundo_tempo = ctk.CTkLabel(self.Frame_Conteudo, height= 51, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 50)
        self.label_fundo_tempo.grid(row= 1 ,column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "ew")

        self.label_tempo = ctk.CTkLabel(self.Frame_Conteudo,text= "Tempo:", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_tempo.grid(row= 1, column= 0, padx= (20, 0), pady= 5)

        self.label_tempo_entry = ctk.CTkLabel(self.Frame_Conteudo, height= 40, text= "", font= ("courier", 16), 
                                              bg_color= ("#979da2","#565b5e"), fg_color= ("#ebebeb","#242424"), corner_radius= 50)
        self.label_tempo_entry.grid(row= 1, column= 1, padx= (5, 20), pady= 5, sticky= "ew")    


        self.label_fundo_midias = ctk.CTkLabel(self.Frame_Conteudo, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.label_fundo_midias.grid(row= 2, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")

        self.label_midias = ctk.CTkLabel(self.Frame_Conteudo,text= "Midias", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_midias.grid(row= 2, column= 0, columnspan= 2, padx= (20, 0), pady= 5)

        self.textBox_midias = ctk.CTkTextbox(self.Frame_Conteudo, height= 100, state= "disabled", bg_color= ("#979da2","#565b5e"))
        self.textBox_midias.grid(row= 3, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "ew")


        self.label_fundo_categorias = ctk.CTkLabel(self.Frame_Conteudo, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.label_fundo_categorias.grid(row= 4, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")

        self.label_categorias = ctk.CTkLabel(self.Frame_Conteudo,text= "Categorias", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_categorias.grid(row= 4, column= 0, columnspan= 2, padx= (20, 0), pady= 5)

        self.textBox_categorias = ctk.CTkTextbox(self.Frame_Conteudo, height= 100, state= "disabled", bg_color= ("#979da2","#565b5e"))
        self.textBox_categorias.grid(row= 5, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "ew")


        self.label_fundo_descricao = ctk.CTkLabel(self.Frame_Conteudo, text= "", fg_color= ("#979da2","#565b5e"), corner_radius= 20)
        self.label_fundo_descricao.grid(row= 6, rowspan= 2, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= "nsew")

        self.label_descricao = ctk.CTkLabel(self.Frame_Conteudo, height= 50,text= "Descricao", font= ("courier", 16), bg_color= ("#979da2","#565b5e"))
        self.label_descricao.grid(row= 6, column= 0, columnspan= 2, padx= (20, 0), pady= 5)

        self.textBox_descricao = ctk.CTkTextbox(self.Frame_Conteudo, height= 100, state= "disabled", bg_color= ("#979da2","#565b5e"))
        self.textBox_descricao.grid(row= 7, column= 0, columnspan= 2, padx= 10, pady= (0,20), sticky= "nsew")

        # =- Criando buttons -= =-----------------------------------------------=
        self.botao_sair = ctk.CTkButton(self, width= 400, height= 30, text= "Voltar", text_color= "white", fg_color= ("#E66262","#333333"), 
                                                        hover_color= ("#A00F0F","red"), border_color= ("white","red"), border_width=2, command= self.set_botao_sair)
        self.botao_sair.grid(row=1, column= 1,pady= 20, padx= 5, sticky= "s")

        self.botao_left = ctk.CTkButton(self, width= 50, height= 50, text= "<", font= ("Arial", 32), text_color= "white", fg_color= ("#6188AF", "#333333"),
                                        hover_color= "#49338B", border_width= 2, border_color= ("White", "#49338B"), command= self.set_botao_left)
        self.botao_left.grid(row= 0, column= 0, padx= (30, 0), pady= 10, sticky= "e")
        
        self.botao_right = ctk.CTkButton(self, width= 50, height= 50, text= ">", font= ("Arial", 32), text_color= "white", fg_color= ("#6188AF", "#333333"),
                                        hover_color= "#49338B", border_width= 2, border_color= ("White", "#49338B"), command= self.set_botao_right)
        self.botao_right.grid(row= 0, column= 2, padx= (0, 30), pady= 10, sticky= "w")

    # =- Funcionalidade do botões -= =------------------------=
    # configurando o botão de voltar para voltar para a tela de perfil
    def set_botao_sair(self):
        self.__app_manager.FrameAtual("perfil_usuario")

    # configurando o botão de left para que ele va para o post posterior
    def set_botao_left(self):
        self.set_img_info(self.lista_desenhos[self.indice_ant], self.lista_desenhos)

    # configurando o botão de right para que ele va para o post anterior
    # configurando o botão de right para que ele va para o post anterior
    def set_botao_right(self):
        self.set_img_info(self.lista_desenhos[self.indice_pos], self.lista_desenhos)

    # =- metodos -= =------------------------=
    # metodo que pega todas as informações das artes e as coloca na tela
    def set_img_info(self, img, desenhos):
        self.lista_desenhos = desenhos

        self.setting_buttons_left_right(img)

        # recebendo a imagem e abrindo ela =---
        img_data = Image.open(img)
        largura = 600
        altura = ((largura * img_data.height)//img_data.width)

        img_post = ctk.CTkImage(light_image= img_data, dark_image= img_data, size= (largura, altura))  

        # pegando todos os arquivos e variaveis necessarias =---
        usuario_atual = self.__dataset.get_usuarioAtual()[0]
        titulo = ""
        tempo = ""
        midias = []
        categorias = []
        descricao = ""

        # recebendo as informações dos desenhos com base na imagem recebida =---
        titulo, tempo, midias, categorias, descricao = self.__dataset.get_Desenhos().get_all_com_usuario(usuario_atual, img)

        self.label_img.configure(image= img_post)

        self.label_titulo_entry.configure(text= titulo)
        self.label_tempo_entry.configure(text= tempo)

        self.textBox_midias.configure(state= "normal")
        self.textBox_categorias.configure(state= "normal")
        self.textBox_descricao.configure(state= "normal")

        self.textBox_midias.delete(0.0, "end")
        self.textBox_categorias.delete(0.0, "end")
        self.textBox_descricao.delete(0.0, "end")

        self.textBox_midias.insert(0.0, text= "\n".join(midias))
        self.textBox_categorias.insert(0.0, text= "\n".join(categorias))
        if descricao != "vazio":
            self.textBox_descricao.insert(0.0, text= descricao)

        self.textBox_midias.configure(state= "disabled")
        self.textBox_categorias.configure(state= "disabled")
        self.textBox_descricao.configure(state= "disabled")

    # metodo que define a direção que cada botão vai ter e se existe um post anterior ou proximo a ele
    def setting_buttons_left_right(self,img):
        for pos, x in reversed(list(enumerate(self.lista_desenhos))):
            if x == img:
                self.indice_atual = pos

        self.indice_ant = self.indice_atual + 1
        self.indice_pos = self.indice_atual - 1

        if self.indice_ant >= len(self.lista_desenhos):
            self.botao_left.configure(state= "disabled")
        else:
            self.botao_left.configure(state= "normal")

        if self.indice_pos < 0:
            self.botao_right.configure(state= "disabled")
        else:
            self.botao_right.configure(state= "normal")
# =-----------------------------------------------------------------------------------=
# =--------------------------------------------------------------------------------------------------------------------------------------------------------= #

# =---------------------------------------------= MAIN =---------------------------------------------= #
# inicializa a variavel gerenciador
app_manager = Gerenciador_Telas()   # Cria apenas uma janela
app_manager.StartScreen()           # inicia a janela
# =--------------------------------------------------------------------= 