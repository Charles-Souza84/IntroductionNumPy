import numpy as np
# o arquivo tree_census contém informações sobre o censo de árvores da cidade de Nova Iorque com informações
# de ID da árvore, ID do bloco, diâmetro do tronco, diâmetro do toco, nesta ordem. Importante lembrar que NumPy não trabalha
# com nomes das colunas.

# importando o arquivo tree_census 
tree_census = np.load('tree_census.npy')

"""
# selecionando todos os elementos da segunda coluna de tree_census
block_ids = tree_census[:, 1]

# imprimindo os cinco primeiros elementos de block_ids
print(block_ids[0:5,])

# selecionando e imprimindo o décimo block_id de block_ids
tenth_block_id = block_ids[9]
print(tenth_block_id)

# selecionando cinco IDs de bloco de block_ids inciando pelo décimo
block_id_slice = block_ids[9:14]
print(block_id_slice)

#criando um array com os 100 primeiros diâmetros de tronco (terceira coluna) de tree_census
hundred_diameters = tree_census[0:100, 2]
print(hundred_diameters)

# criando um array de diâmetros de tronco com índices pares, iniciando na linha 50 até 100(inclusive)
every_other_diameter = tree_census[50:100:2, 2]
print(every_other_diameter)

# extraindo informação de diâmetro de tronco e ordenando do menor para o maior
sorted_trunk_diameters = np.sort(tree_census[:, 2])
print(sorted_trunk_diameters)

# criando um array que contenha os dados de linha da árvore 
# com maior diâmetro de tronco ( 51 - informação conhecida )em tree_census
largest_tree_data = tree_census[tree_census[:, 2]==51]
print(largest_tree_data)

# por meio de slicing, obter apenas o ID do bloco do array largest_tree_data
largest_tree_block_id = largest_tree_data[: , 1]
print(largest_tree_block_id)

# criando um array que contenha dados de todas as árvores com ID de bloco igual a largest_tree_bloc_id
trees_on_largest_tree_block = tree_census[tree_census[:, 1] == largest_tree_block_id]
print(trees_on_largest_tree_block)

# Conclusão - a árvore mais grossa é a única árvore realmente grande do seu bloco ( com base no diâmetro de tronco )
# criando um array contendo árvores do bloco 313879
block_313879 = tree_census[:, :][tree_census[:, 1]==313879]
print(block_313879)

# utilizando np.where(), criar um array de índices de linha das árvores do bloco 313879
row_indices = np.where(tree_census[:, 1]==313879)

# criando um array que contenha somente dados das árvores do bloco 313879
block_313879 = tree_census[row_indices]
print(row_indices)

# criando um array 1D com informações de diâmetro de toco e de tronco em uma mesma coluna. Lembrando que árvore vivas não tem 
# diâmetro de toco, assim como árvores mortas não tem diâmetro de tronco
trunk_stump_diameters = np.where(tree_census[:, 2]==0, tree_census[:,3], tree_census[:,2])
print(trunk_stump_diameters)

# imprimindo os formatos de tree_census e new_tress
new_trees = np.array([[1211, 227386, 20, 0 ], [1212, 227386, 8, 0]])
print(tree_census.shape, new_trees.shape)

# adicionando linhas ao array tree_census obtidas do array new_trees ( concatenar ao longo do eixo 0 - linha)
updated_tree_census = np.concatenate((tree_census, new_trees))
print(updated_tree_census)

# imprimindo os formatos dos arrays tree_census e trunk_stump_diameters
trunk_stump_diameters = np.where(tree_census[:, 2]==0, tree_census[:,3], tree_census[:,2])
print(trunk_stump_diameters.shape, tree_census.shape)

# reformatando o array trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((1000, 1))

# adicionando o conteúdo de reshaped_diameters à última coluna de tree_census
concatenated_tree_census = np.concatenate((tree_census, reshaped_diameters), axis=1)
print(concatenated_tree_census)

"""
# deletando o diâmetro de toco ( coluna 3) do array tree_census
tree_census_no_stumps = np.delete(tree_census, 3, axis=1)

# salvando os índices das árvores no bloco 313879 ( áreas privadas - informação conhecida )
private_block_indices = np.where(tree_census[:, 1] == 313879)

# deletando as linhas das árvores do bloco 313879 do array tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps, private_block_indices, axis = 0)

# imprimindo o formato do array tree_census_clean
print(tree_census_clean.shape)