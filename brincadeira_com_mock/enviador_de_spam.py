class CanalEmail:
    def enviar(self, destinatario, msg):
        nome=destinatario.split('@')[0].capitalize()
        msg_final = f'{nome} {msg}'
        print('Enviando msg de vdd')
        return destinatario, msg_final
 
class EnviadorDeSpam:
    def __init__(self, destinatarios=None):
        self.destinatarios = destinatarios if destinatarios else []
        self.canais_de_envio=[CanalEmail()]

    def adicionar_destinatario(self, destinatario):
        self.destinatarios.append(destinatario)

    def enviar_spam(self, msg):
        for destinatario in self.destinatarios:
            for canal in self.canais_de_envio:
                yield canal.enviar(destinatario, msg)