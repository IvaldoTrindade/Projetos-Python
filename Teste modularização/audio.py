
class Audio:
    
    def __init__(self, volume):
        self.volume = volume

    def aumentar_volume(self, aumento):
        self.volume += aumento
        print(f'Volume aumentado {aumento}. Volume atual: {self.volume}')

    def diminuir_volume(self, diminuir):
        self.volume -= diminuir
        print(f'Volume diminuido em {diminuir}. Volume atual: {self.volume}')    

audio = Audio(volume)