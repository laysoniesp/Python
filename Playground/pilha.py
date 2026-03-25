class pilha:
    def __init__ (self):
        seft.items = []
    def empilhar (self, item):
        self.items = self.items + [item]
    def desempilhar (self):
        if not self.is_vazio ():
            item_removidoc=cself.items[-1]
            self.items = self.items [:-1]
            return item_removido
        else:
            print("A pilha esta vazia, não é possivel desempilhar")
