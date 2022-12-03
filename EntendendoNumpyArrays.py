import numpy as np
import sudoku_list
import matplotlib.pyplot as plt


######## Entendendo NumPy Arrays  ###########

# convertendo a lista sudoku_list em um array
sudoku_array = np.array(sudoku_list)
# imprimindo o tipo do array
print(type(sudoku_array))


# criando um array de zero com 2 linhas e 4 colunas
zero_array = np.zeros((2,4))
print(zero_array)


# criando um array de random com 3 linhas e 6 colunas
random_array = np.random.random((3,6))
print(random_array)

# criando um scatter plot com um array criado por np.arange()
doubling = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
doubling_array = np.array(doubling)

one_to_ten = np.arange(1, 11)

plt.scatter(one_to_ten, doubling_array)
plt.show()


# lendo o arquivo sudoku_game.pny
sudoku_game_loaded = np.load('sudoku_game.npy')
# transformando em um array 1D 
flattened_game = sudoku_game_loaded.flatten()

# imprimindo o formato do array 1D
# por algum motivo, o arquivo original estava com 72 elementos e não 81 como deveria
print(flattened_game.shape)

# retornando o array ao formato original 
reshaped_game = flattened_game.reshape((8,9))

# imprimindo o array original e o refeito
print(sudoku_game_loaded)
print(reshaped_game)


# criando um array de zeros com 3 linhas e 2 colunas
zero_array = np.zeros((3,2))

# imprimindo o tipo de dados de zero_array
print(zero_array.dtype)

# criando um novo array de int32 zeros com 3 linhas e 2 colunas
zero_int_array = np.zeros((3,2), dtype=np.int32)

# imprimindo o dipo de dados de zero_int_array
print(zero_int_array.dtype)

