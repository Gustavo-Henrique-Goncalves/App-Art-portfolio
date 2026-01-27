# =------------------------= CLASSE DO GERENCIADOR DE DADOS =--------------------------=
class Gerenciador_Dados():
    def __init__(self):
        # pega todos os dados de cada uma das classes e coloca no gerenciador =---------
        # =- dados da classe Usuario:
        self.__perfils = Perfil()
        self.__usuarios = self.__perfils.get_usuarios()

        self.__usuario_atual = [None, None]

        # =- dados da classe Desenho:
        self.__desenhos = Desenho()

    # =- getters -= =-----------------------------------=
    def get_usuarios(self):
        return self.__usuarios
    
    def get_usuarioAtual(self):
        return self.__usuario_atual
    
    def get_Desenhos(self):
        return self.__desenhos
    
    def get_perfils(self):
        return self.__perfils

    # =- setters -= =-----------------------------------=
    def set_usuarioAtual(self, usuario, senha):
        self.__usuario_atual = (usuario, senha)

    # =- metodos -= =-----------------------------------=
# =-----------------------------------------------------------------------------------=

# =------------------------= CLASSE DE USUARIOS =--------------------------=
class Usuario():
    def __init__(self):
        arquivo = "database/usuarios_dados.txt"
        self.__usuarios = []
        self.__senhas = []

        try:
            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()
                for linha in f:
                    linha = linha.split("|")
                    self.__usuarios.append(linha[0])
                    self.__senhas.append(linha[1])
        except FileNotFoundError:
            print(f"=- Arquivo de usuarios não encontrado, reecriando um... -=")

            with open(arquivo, "w", encoding="utf-8-sig") as f:
                f.write("usuario|senha|img_perfil|bio|desenho\n")
                f.write("usuario1|senha1|img/icon_avatar_dark.png||None\n")

            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()
                for linha in f:
                    linha = linha.split("|")
                    self.__usuarios.append(linha[0])
                    self.__senhas.append(linha[1])

        except Exception as error:
            print(f"=- Ocorreu um erro: {error} -=")
            exit()

    # =- getters -= =-----------------------------------=
    def get_Usuario(self):
        return self.__usuarios
    
    def get_Senha(self):
        return self.__senhas
    # =- metodos -= =-----------------------------------=
# =-----------------------------------------------------------------------------------=

# =------------------------= CLASSE DE DESENHOS =--------------------------=
class Desenho():
    def __init__(self):
        self.__arquivo = "database/lista_desenhos.txt"
        self.__caminho = []
        self.__titulo = []
        self.__tempo = []
        self.__categoria = []
        self.__midia = []
        self.__descricao = []

        try:
            with open(self.__arquivo, "r", encoding="utf-8-sig") as f:
                f.readline()
                for linha in f:
                    linha = linha.split("|")

                    self.__caminho.append(linha[1]) 
                    self.__titulo.append(linha[2])
                    self.__tempo.append(linha[3])
                    self.__midia.append(linha[4])
                    self.__categoria.append(linha[5])
                    self.__descricao.append(linha[6].replace("\n", ""))
        except Exception as error:
            print(f"=- Arquivo não existente, criando arquivo de listagem dos desenhos, {error} -=")
            with open(self.__arquivo, "w", encoding="utf-8-sig") as f:
                f.write("usuario|caminho|titulo|qtd_tempo|midia|categoria|descricao\n")

    # =- getters -= =-----------------------------------=

    def get_usuarios(self):
        arquivo_listaDesenhos = self.get_Arquivo_ListaDesenhos()
        usuarios = []

        try:
            with open(arquivo_listaDesenhos, "r", encoding= "utf-8-sig") as f:
                header = f.readline()

                for x in f:
                    dados = x.strip().split("|")

                    usuarios.append(dados[0])

        except Exception as error:
            print(f"=- {error} -=")
            exit()

        return usuarios

    def get_Caminho(self):
        return self.__caminho

    def get_Titulo(self):
        return self.__titulo
    
    def get_Tempo(self):
        return self.__tempo
    
    
    def get_Midia(self):
        return self.__midia
    
    def get_Categoria(self):
        return self.__categoria
    
    def get_Descricao(self):
        return self.__descricao
    
    def get_Caminho_onlyName(self):
        caminho_onlyname = []

        for x in self.__caminho:
            caminho_onlyname.append(x.split("/")[-1])

        return caminho_onlyname
    
    def get_all_com_usuario(self, usuario_atual, img):

        arquivo_listaDesenhos = self.get_Arquivo_ListaDesenhos()

        try:
            with open(arquivo_listaDesenhos, "r", encoding= "utf-8-sig") as f:
                header = f.readline()

                for x in f:
                    dados = x.strip().split("|")

                    if dados[0] == usuario_atual and dados[1] == img:
                        titulo = dados[2]
                        tempo = dados[3]
                        midias = dados[4].strip().replace("[","").replace("]","").replace("'","").split(", ")
                        categorias = dados[5].strip().replace("[","").replace("]","").replace("'","").split(", ")
                        descricao = dados[6]

        except Exception as error:
            print(f"=- {error} -=")
            exit()

        return titulo, tempo, midias, categorias, descricao
    
    def get_all_sem_usuario(self, usuario_atual):

        arquivo_listaDesenhos = self.get_Arquivo_ListaDesenhos()
        imgs = []
        titulo = []
        tempo = []
        midias = []
        categorias = []
        descricao = []


        try:
            with open(arquivo_listaDesenhos, "r", encoding= "utf-8-sig") as f:
                header = f.readline()

                for x in f:
                    dados = x.strip().split("|")

                    if dados[0] != usuario_atual:
                        imgs.append(dados[1])
                        titulo.append(dados[2])
                        tempo.append(dados[3])
                        midias.append(dados[4].strip().replace("[","").replace("]","").replace("'","").split(", "))
                        categorias.append(dados[5].strip().replace("[","").replace("]","").replace("'","").split(", "))
                        descricao.append(dados[6])

        except Exception as error: 
            print(f"=- {error} -=")
            exit()

        return imgs, titulo, tempo, midias, categorias, descricao

    def get_Arquivo_ListaDesenhos(self):
        return self.__arquivo

    # =- metodos -= =-----------------------------------=
    def register_Drawing(self, usuario_atual, caminho_arquivo, titulo, qtd_tempo, midias, categorias, descricao):

        arquivo_listaDesenhos = self.get_Arquivo_ListaDesenhos()

        with open(arquivo_listaDesenhos, "a", encoding="utf-8-sig") as f:
            f.write(f"{usuario_atual}|{caminho_arquivo}|{titulo}|{qtd_tempo}|{midias}|{categorias}|{descricao}\n")

    def update_userName_inListaDesenhos(self, usuario_antigo, usuario_novo):
         
        arquivo = self.get_Arquivo_ListaDesenhos()
        header = ""
        linha_atualizada = []

        try:
            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()
                for x in f:
                    dado = x.strip().split("|")

                    if dado[0] == usuario_antigo:
                        dado[0] = usuario_novo

                    linha_atualizada.append("|".join(dado) + "\n")
        except Exception as error:
            print(f"=- {error} -=")
            exit()

        with open(arquivo, "w", encoding="utf-8-sig") as f:
            f.write(header)
            f.writelines(linha_atualizada)


class Perfil():
    def __init__(self):

        # declarando todos os atributos da classe perfil, contendo o usuario, foto de perfil, bio e os desenhos do usuario
        self.__usuarios = Usuario()
        self.__foto_perfil = []
        self.__bio = []
        self.__desenhos = []

        self.__arquivo = "database/usuarios_dados.txt"

        try:
            with open(self.__arquivo, "r", encoding="utf-8-sig") as f:
                linha = f.readline()

                for x in f:
                    linha = x.split("|")
                    self.__foto_perfil.append(linha[2])
                    self.__bio.append(linha[3])
                    self.__desenhos.append(linha[4].strip().replace("\n", ""))

        except Exception as error:
            print(f"=- Erro ao Receber os perfis: {error} -=")
            exit()

    # =- getters -= =-----------------------------------=
    def get_usuarios(self):
        return self.__usuarios

    def get_fotoPerfil(self):
        return self.__foto_perfil
    
    def get_bio(self):
        return self.__bio
    
    def get_desenhos(self):
        return self.__desenhos

    def get_arquivo_perfilUsuarios(self):
        return self.__arquivo
    
    def get_desenhos_from_usuario(self, usuario_atual):
        arquivo = self.get_arquivo_perfilUsuarios()

        try:
            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()

                for x in f:
                    dados = x.strip().split("|")

                    if dados[0] == usuario_atual:
                        return dados[-1].split(",")
        except Exception as error:
            print(f"=- {error} -=")
            exit()

    # =- setters -= =-----------------------------------=
    def set_usuarios(self):
        self.__usuarios = Usuario()

    def set_usuarios_from_cadastro(self, novo_usuario, nova_senha):
        arquivo = self.get_arquivo_perfilUsuarios()

        with open(arquivo, "a", encoding="utf-8-sig") as f:
            f.write(f"{novo_usuario}|{nova_senha}|img/icon_avatar_dark.png||None\n")

        self.set_usuarios()

    def set_fotoPerfil(self, usuario, fotoPerfil):
        arquivo = self.get_arquivo_perfilUsuarios()
        
        header = ""
        linha_atualizada = []

        try:
            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()
                for pos, x in enumerate(f):
                    dado = x.strip().split("|")

                    if dado[0] == usuario:
                        dado[2] = fotoPerfil

                        self.__foto_perfil[pos] = fotoPerfil

                    linha_atualizada.append("|".join(dado) + "\n")
        except Exception as error:
            print("=- {error} -=")
            exit()

        with open(arquivo, "w", encoding="utf-8-sig") as f:
            f.write(header)
            f.writelines(linha_atualizada)

    def set_Bio(self, usuario, bio):
        arquivo = self.get_arquivo_perfilUsuarios()
        
        header = ""
        linha_atualizada = []

        try:
            with open(arquivo, "r", encoding="utf-8-sig") as f:
                header = f.readline()
                for pos,x in enumerate(f):
                    dado = x.strip().split("|")

                    if dado[0] == usuario:
                        dado[3] = bio

                        self.__bio[pos] = bio

                    linha_atualizada.append("|".join(dado) + "\n")
        except Exception as error:
            print(f"=- {error} -=")
            exit()

        with open(arquivo, "w", encoding="utf-8-sig") as f:
            f.write(header)
            f.writelines(linha_atualizada)

    # =- metodos -= =-----------------------------------=
    def reset_all(self):
        self.__foto_perfil.clear()
        self.__bio.clear()
        self.__desenhos.clear()

        with open(self.__arquivo, "r", encoding="utf-8-sig") as f:
                linha = f.readline()

                for x in f:
                    linha = x.split("|")
                    self.__foto_perfil.append(linha[2])
                    self.__bio.append(linha[3])
                    self.__desenhos.append(linha[4].strip().replace("\n", ""))

    def update_Desenhos(self, usuario_atual, caminho_arquivo):
        arquivo_perfilUsuarios = self.get_arquivo_perfilUsuarios()

         # 2. Atualização do Perfil do Usuário
        linhas_atualizadas = []
        header = ""
        usuario_encontrado = False

        with open(arquivo_perfilUsuarios, "r", encoding="utf-8-sig") as f:
            header = f.readline()
            for linha in f:
                dados = linha.strip().split("|")
                
                if dados[0] == usuario_atual:
                    usuario_encontrado = True
                    # Supomos que a última coluna guarda os caminhos dos desenhos
                    # Se estiver vazio ou for "None", começamos uma string nova
                    if dados[-1] == "" or dados[-1] == "None":
                        dados[-1] = caminho_arquivo
                    else:
                        # Adicionamos o novo caminho separado por vírgula (ou outro separador)
                        dados[-1] = f"{dados[-1]},{caminho_arquivo}"
                
                # Guardamos a linha como string novamente
                linhas_atualizadas.append("|".join(dados) + "\n")

        # 3. Escrita final (Sobrescrevendo com os dados novos)
        if usuario_encontrado:
            with open(arquivo_perfilUsuarios, "w", encoding="utf-8-sig") as f:
                f.write(header)
                f.writelines(linhas_atualizadas)

    def update_usuarios(self, usuario_antigo, senha_antiga, usuario_novo, senha_nova):
        arquivo = self.get_arquivo_perfilUsuarios()
        linhas_atualizadas = []
        dados = []
        header = ""
        usuario_encontrado = False

        with open(arquivo, "r", encoding="utf-8-sig") as f:
            header = f.readline()
            for linha in f:
                dados = linha.strip().split("|")
                
                if dados[0] == usuario_antigo and dados[1] == senha_antiga:
                    usuario_encontrado = True
                    # Supomos que a última coluna guarda os caminhos dos desenhos
                    # Se estiver vazio ou for "None", começamos uma string nova
                    dados[0] = usuario_novo
                    dados[1] = senha_nova
                
                # Guardamos a linha como string novamente
                linhas_atualizadas.append("|".join(dados) + "\n")

        # 3. Escrita final (Sobrescrevendo com os dados novos)
        if usuario_encontrado:
            with open(arquivo, "w", encoding="utf-8-sig") as f:
                f.write(header)
                f.writelines(linhas_atualizadas)

        self.set_usuarios()