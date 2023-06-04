def converter_notas(notas):
    notas_musicais = {'Dó': 'I', 'Ré': 'II', 'Mi': 'III', 'Fá': 'IV', 'Sol': 'V', 'Lá': 'VI', 'Si': 'VII'}
    graus = []

    for nota_atual in notas:
        grau_romano = notas_musicais.get(nota_atual)
        if grau_romano:
            graus.append(grau_romano)
    return graus


# Entrada
notas = ['Ré', 'Sol', 'Dó']
resultado = converter_notas(notas)
print(resultado)
