class Programa:
    def __init__(self, nome, ano):
        # Inicializa um novo objeto Programa com o nome, ano de lançamento e número de likes
        self._nome = nome.title()  # O nome é convertido para o formato de título (primeira letra maiúscula)
        self.ano = ano  # Define o ano de lançamento do programa
        self._likes = 0  # Inicializa o número de likes como zero

    @property
    def likes(self):
        # Propriedade de leitura apenas para acessar o número de likes
        return self._likes

    def dar_likes(self):
        # Método para adicionar um like ao programa
        self._likes += 1

    @property
    def nome(self):
        # Propriedade de leitura apenas para acessar o nome do programa
        return self._nome

    @nome.setter
    def nome(self, nome):
        # Propriedade de escrita para definir o nome do programa
        self._nome = nome.title()  # O novo nome é convertido para o formato de título (primeira letra maiúscula)

    def __str__(self):
        # Método para representação em string do programa
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # Inicializa um novo objeto Filme com o nome, ano de lançamento, duração e número de likes
        super().__init__(nome, ano)  # Chama o construtor da classe pai para inicializar atributos comuns
        self.duracao = duracao  # Define a duração do filme em minutos

    def __str__(self):
        # Método para representação em string do filme
        return f'Nome: {self.nome} - {self.duracao} min - {self.ano} - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # Inicializa um novo objeto Serie com o nome, ano de lançamento, número de temporadas e número de likes
        super().__init__(nome, ano)  # Chama o construtor da classe pai para inicializar atributos comuns
        self.temporadas = temporadas  # Define o número de temporadas da série

    def __str__(self):
        # Método para representação em string da série
        return f'Nome: {self.nome} - {self.temporadas} temporadas - {self.ano} - Likes: {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        # Inicializa um novo objeto Playlist com um nome e uma lista de programas
        self.nome = nome  # Define o nome da playlist
        self._programas = programas  # Define a lista de programas na playlist

    def __getitem__(self, item):
        # Método de indexação para acessar programas pelo índice
        return self._programas[item]

    def __len__(self):
        # Método para obter o tamanho da playlist
        return len(self._programas)


# Instanciando objetos Filme e Série
skyfall = Filme('007 – Operação Skyfall', 2012, 143)
vikings = Serie('vikings', 2013, 6)
gump = Filme('forrest gump', 1991, 118)
peaky = Serie('peaky blinders', 2013, 6)
seven = Filme('seven - os sete crimes capitais', 1995, 127)
crown = Serie('the crown', 2016, 5)
poderoso = Filme('o poderoso chefao', 1972, 175)
mindhunter = Serie('mindhunter', 2019, 2)
samurai = Filme('ultimo samurai', 2003, 154)
bad = Serie('breaking bad', 2008, 5)
missao = Filme('missao impossivel - nação secreta', 2015, 131)
narcos = Serie('narcos', 2015, 3)

# Adicionando likes aos programas
skyfall.dar_likes()
skyfall.dar_likes()
skyfall.dar_likes()
vikings.dar_likes()
vikings.dar_likes()
gump.dar_likes()
gump.dar_likes()
peaky.dar_likes()
peaky.dar_likes()
seven.dar_likes()
seven.dar_likes()
crown.dar_likes()
crown.dar_likes()
crown.dar_likes()
crown.dar_likes()
poderoso.dar_likes()
poderoso.dar_likes()
poderoso.dar_likes()
mindhunter.dar_likes()
mindhunter.dar_likes()
mindhunter.dar_likes()
samurai.dar_likes()
samurai.dar_likes()
samurai.dar_likes()
samurai.dar_likes()
bad.dar_likes()
bad.dar_likes()
missao.dar_likes()
missao.dar_likes()
missao.dar_likes()
missao.dar_likes()
missao.dar_likes()
narcos.dar_likes()
narcos.dar_likes()
narcos.dar_likes()
narcos.dar_likes()


# Criando uma lista de programas
listinha = [skyfall, vikings, gump, peaky, seven, crown, poderoso, mindhunter, samurai, bad, missao, narcos]  # Adicione mais programas se necessário

# Criando uma playlist
minha_playlist = Playlist('fim de semana', listinha)

# Iterando sobre a playlist e imprimindo cada programa
for programa in minha_playlist:
    print(programa)

# Imprimindo o tamanho da playlist
print(f'Tamanho: {len(minha_playlist)}')