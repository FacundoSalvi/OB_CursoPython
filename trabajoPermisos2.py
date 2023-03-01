import pickle
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

v = Vehiculo("Toyota")
with open('vehiculo.pkl', 'wb') as f:
    pickle.dump(v,f)

with open('vehiculo.pkl', 'rb') as f:
    v_cargado = pickle.load(f)

print(v_cargado.marca)

