#Calcula a AREA do terreno da cultura
def calcular_area(base, altura):
    area = base * altura
    return area

#Calcula a quantidade de fertilizante que sera gasto por metro de linha
def insumo_cana(metros_linha):
    fertilizante = metros_linha * 2
    return fertilizante

#Calcula a puverização, ou seja pega a quantidade de plantas
 #e mutiplica pelos 500 MLs que será usado pra cada uma.
def insumo_laranja(numero_plantas):
    pulverizacao = numero_plantas * 500
    return pulverizacao