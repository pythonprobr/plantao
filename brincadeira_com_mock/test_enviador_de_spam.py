from brincadeira_com_mock.enviador_de_spam import EnviadorDeSpam
from unittest.mock import Mock


def test_criacao_enviador_de_spam():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    assert enviador.destinatarios == ['renzo@email.com']
    enviador.adicionar_destinatario('river@email.com')
    assert enviador.destinatarios == [
        'renzo@email.com', 'river@email.com'
        ]


def test_envio_de_spam():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    canal=aMock()
    canal.enviar.return_vlue=('renzo@email.com', 'Renzo se liga que tem plantão Python Pro!')
    enviador.canais_de_envio=[canal]
    assert list(
        enviador.enviar_spam('se liga que tem plantão Python Pro!'))==[
            ('renzo@email.com', 'Renzo se liga que tem plantão Python Pro!'),
    ]

def test_canal_foi_executado():
    enviador = EnviadorDeSpam(['renzo@email.com'])
    canal=Mock()
    enviador.canais_de_envio=[canal]
    list(enviador.enviar_spam('se liga que tem plantão Python Pro!'))
    canal.enviar.assert_called_once_with('renzo@email.com', 'se liga que tem plantão Python Pro!')


