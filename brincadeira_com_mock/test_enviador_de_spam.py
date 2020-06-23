from brincadeira_com_mock.enviador_de_spam import EnviadorDeSpam


def test_criacao_enviador_de_spam():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    assert enviador.destinatarios == ['renzo@email.com']
    enviador.adicionar_destinatario('river@email.com')
    assert enviador.destinatarios == [
        'renzo@email.com', 'river@email.com'
        ]

class CanalMock:
    def __init__(self):
        self.enviar_foi_chamado = False
        self.enviar_argumentos=[]

    def enviar(self, destinatario, msg):
        self.enviar_argumentos=[destinatario, msg]
        self.enviar_foi_chamado = True
        return ('renzo@email.com', 'Renzo se liga que tem plantão Python Pro!')

def test_envio_de_spam():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    enviador.canais_de_envio=[CanalMock()]
    assert list(
        enviador.enviar_spam('se liga que tem plantão Python Pro!'))==[
            ('renzo@email.com', 'Renzo se liga que tem plantão Python Pro!'),
    ]

def test_canal_foi_executado():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    canal = CanalMock()
    enviador.canais_de_envio=[canal]
    list(enviador.enviar_spam('se liga que tem plantão Python Pro!'))
    assert canal.enviar_foi_chamado
    assert canal.enviar_argumentos == ['renzo@email.com', 'se liga que tem plantão Python Pro!']


