filmes = [
{"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
{"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
{"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]


#A média das avaliações dos filmes.
somafilmes=0#Testar sum
for i in range (len(filmes)):
    somafilmes= somafilmes+filmes[i]['avaliacao']
mediafilmes=somafilmes/len(filmes)

#O título do filme com a maior avaliação.
maior_avaliação=max(filmes, key=lambda filme:filme['avaliacao'])

#O ano de lançamento do filme com a menor avaliação.
menor_avaliação=min(filmes, key=lambda filme:filme['avaliacao'])



print(f' A média das avaliações dos filmes:', mediafilmes,'\n',
       'O título do filme com a maior avaliação:', maior_avaliação['titulo'],'\n',
       'O ano de lançamento do filme com a menor avaliação:', menor_avaliação['ano'])