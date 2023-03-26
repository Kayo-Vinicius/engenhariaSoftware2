from typing import Dict, Set, List

class Publicador:
    def __init__(self, remetente, pub_sub):
        self.remetente = remetente
        self.mensagens = []
        self.pub = pub_sub

    def publicar(self, mensagem):
        msg = {'remetente': self.remetente, 'mensagem': mensagem}
        self.pub.receberMensagem(msg)

class Inscrito:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, remetente, mensagem):
        print(f"#{remetente}#\t{self.nome} recebeu: {mensagem}")

class PubSub:
    def __init__(self):
        self.inscritos: Dict[str, Set] = {}
        self.filaMensagens: List[Dict[str, str]] = []

    def adicionarInscrito(self, remetente, inscrito):
        if remetente in self.inscritos:
            self.inscritos[remetente].add(inscrito)
        else:
            self.inscritos[remetente] = {inscrito}

    def receberMensagem(self, mensagem: Dict[str, str]):
        self.filaMensagens.append(mensagem)

    def enviarMensagem(self, remetente, mensagem):
        for inscrito in self.inscritos[remetente]:
            inscrito.atualizar(remetente, mensagem)

    def broadcast(self):
        for msg in self.filaMensagens:
            self.enviarMensagem(msg['remetente'], msg['mensagem'])

        self.filaMensagens = []


kayo = Inscrito('Kayo')
vinicius = Inscrito('Vinicius')
silva = Inscrito('Silva')
mendes = Inscrito('Mendes')

euMesmo = PubSub()
email = Publicador('EuMesmo', euMesmo)

euMesmo.adicionarInscrito('EuMesmo', kayo)
euMesmo.adicionarInscrito('EuMesmo', vinicius)
euMesmo.adicionarInscrito('EuMesmo', silva)
euMesmo.adicionarInscrito('EuMesmo', mendes)

email.publicar('Hoje é domingo')
euMesmo.broadcast()