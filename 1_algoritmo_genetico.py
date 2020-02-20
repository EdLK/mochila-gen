class Mochila():
    capacidad = 35;

    def __init__(self):
        self.peso = 0;
        self.ganancia = 0;

    def esta_llena(self):
        if self.peso > self.capacidad: return True;

    def meter(self, objeto):
        if not self.esta_llena():
            self.peso += objeto[0];
            self.ganancia += objeto[1];

class Individuo():
    def __init__(self, cromosoma):
        self.cromosoma = cromosoma;
        self.mochila = Mochila();

    def aptitud(self, objetos):
        for i in range(0, len(self.cromosoma)):
            if self.cromosoma[i] == '1':
                self.mochila.meter(objetos[i]);

        if self.mochila.esta_llena(): return 0;
        else: return self.mochila.ganancia;

    def cruza(self, pareja1, pareja2):
        self.cromosoma = pareja1.cromosoma[:3]+pareja2.cromosoma[3:];

    def mutacion(self, gen):
        cromosoma = list(self.cromosoma);
        _cromosoma = "";

        if self.cromosoma[gen] == '1': cromosoma[gen] = 0;
        else: cromosoma[gen] = 1;

        for gen in cromosoma: _cromosoma += str(gen);

        self.cromosoma = _cromosoma


#            o1       o2        o3        o4       o5
objetos = [[8, 15], [7, 15], [15, 30], [10, 30], [5, 10]];

individuo_a = Individuo("11010");
individuo_b = Individuo("01010");
individuo_c = Individuo("10100");
individuo_d = Individuo("00111");

individuo_c.cruza(individuo_a, individuo_b);

generacion_1 = [individuo_a, individuo_b, individuo_c, individuo_d];

for individuo in generacion_1:
    print(individuo.aptitud(objetos));

individuo_e = Individuo("cruza"); individuo_e.cruza(individuo_a, individuo_c);
individuo_f = Individuo("cruza"); individuo_f.cruza(individuo_c, individuo_a);
individuo_g = Individuo("cruza"); individuo_g.cruza(individuo_a, individuo_d);
individuo_h = Individuo("cruza"); individuo_h.cruza(individuo_d, individuo_a);

generacion_2 = [individuo_e, individuo_f, individuo_g, individuo_h];

for individuo in generacion_2:
    print(individuo.aptitud(objetos));

individuo_e.mutacion(4);
individuo_h.mutacion(1);
individuo_h.mutacion(2);

mutantes = [individuo_e, individuo_h];

for individuo in mutantes:
    print(individuo.aptitud(objetos));
