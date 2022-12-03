# Entendendo NumPy Arrays

Pandas, SciPy e Matplotlib são construídas com base em API de NumPy, assim como bibliotecas de _machine learning_ como TensorFlow e scikit-learn;

O array é o principal objeto em NumPy, é uma estrutura tipo grade que armazena dados que pode ter N dimensões e cada dimensão pode ter qualquer tamanho.

> para utilizarmos o NumPy, devemos fazer seu import e ,por convenção, damos a ele o _alias_  **np** .

```python
import numpy as np
```

### Criando arrays 1D a partir de listas :

```python
python_list = [3, 2, 5, 8, 4, 9, 7, 6, 1]
array = np.array(python_list)
array
```
_saída_ : array([3, 2, 5, 8, 4, 9, 7, 6, 1])

```python
type(array)
```

_saída_ : numpy.ndaarray

### Criando arrays 2D 
Basta passarmos uma lista de listas como argumento em _np.array_. Da mesma forma, um array 3D é criado passando uma lista, de listas de listas e assim por diante.

```python
python_list_of_lists = [[3, 2, 5],
                        [9, 7, 1],
                        [4, 3, 6]]
np.array(python_list_of_lists)
```

### Array vs Python lists

Por que devemos usar arrays ao invés de Python lists ? Enquanto Python lists podem conter diferentes tipos de dados, todos os elementos em um NumPy array devem ser do mesmo tipo. 

Isto torna NumPy muito eficiente : não há necessidade de checagem do tipo de dado de cada elemento em um array já que todos precisam ser do mesmo tipo. Tendo apenas um tipo de dado também significa que um array NumPy ocupa menos espaço em memória do que se a mesma informação fosse armazenada em uma Python list.

### Criando arrays do zero

Há várias funções para criar arrays do zero em NumPy, incluindo :

* np.zeros() - cria um array preenchido por zeros, que pode ser utilizado como uma lista vazia em Python, preenchendo os dados posteriormente. O formato deste array é informado por meio de uma tupla de interios. Exemplo :

```python
# cria um array de 3 linhas com duas colunas
np.zeros((3,2))
array([ [0.,0.],
        [0.,0.],
        [0.,0.]])
```
* np.random.random() - também recebe como argumento uma tupla para o formato desejado. Este array é criado com número reais (float) entre 0 e 1. Esta é uma função dentro do módulo random do NumPy, por isso np.random.random() e não np.random() apenas.

```python
np.random.random((2,4))
array([[0.88524516, 0.87653402, 0.33456478, 0.45790124],
        0.69783451, 0.79040218, 0.22309183, 0.93018363])
```

* np.arange() - cria um array igualmente espaçado dados um valor inicial e um valo final. Por padrão, cria um avlor sequencial de inteiros, sendo que o valor inicial é incluído e o final não. O valor inicial pode ser omitido caso ele seja igual a 0. Caso um terceiro valor seja passado, este é interpretado como o valor de passo.
```python
np.arange(-3,4)
array([-3, -2, -1, 0, 1, 2, 3])

np.arange(4)
array([0, 1, 2, 3])

np.arange(-3, 4, 3)
array([-3, 0 , 3])
```

### Dimensões de um array

Podemos criar um array 2D como uma lista de listas e um array 3D como um array de arrays 2D. Um array 3D pode ser interpretado como um grupo de arrays 2D com mesmo formato empilhados uns sobre os outros.

Um array 4D pode ser imaginado como um array 2D preenchido por arrays 3D.

Algumas documentações referem-se a arrays como vetores, matrizes e tensores, que são termos matemáticos que distinguem os arrays pelo seu número de dimensões :
* vector - 1D array;
* matriz - 2D array;
* tensor - 3D array;

### Mudança de formato

Mudanças na disposição dos dados de um array podem facilitar nossa análise.

* atributo de array
**.shape** - atributo de uma instância de um array que retorna uma tupla com o seu tamanho em cada dimensão.
```python
array = np.zeros((2,3))
print(array)
array([[0., 0., 0.],
       [0., 0., 0.]])
array.shape
(2,3)
```

* métodos de array - são chamados diretamente no objeto array
**.flatten()** - pega todos os elementos de um array e os coloca em um array 1D.
```python
array = np.array([[1,2], [5,7], [6,6]])
array.flatten()
array([1, 2, 5, 7, 6, 6])
```

**.reshape()** - permite que alteremos o formato de um array sem alterar seus elementos. A tupla passada como argumento deve ser compatível com o número de elementos do array.
```python
array = np.array([[1,2], [5,7], [6,6]])
array.reshape((2,3))
array([[1, 2, 5],
       [7, 6, 6]])
```

### NumPy tipos de dados

Tipos de dados em NumPy são mais específicos do que em Python, pois em NumPy são inclusos tipo de dado e quantidade de memória disponível em bits. O tipo de dado em NumPy pode ser otimizado em termos de quantidade de memória quando o dado utilizado não requer um tamanho grande de memória (em bits).

Lembrando que com 32 bits nós conseguimos representar um número igual a 2 ^ 32 = 4.294.967.296.

* atributo **.dtype** - obtém o tipo de dados em um array :
```python
np.array([1.32, 5.78, 175.55]).dtype
dtype('float64')
```
NumPy escolhe o tipo de dado baseado nos dados contidos no array quando este é criado.

É possível declarar o tipo de dado quando criamos um array usando a _keyword_ dtype, que é um argumento opcional. 

```python
float32_array = np.array([1.32, 5.78, 175.55], dtype=np.float32)
float32_array.dtype
dtype('float32')
```

* método **.astype()** - permite que façamos a conversão de tipo de dados de um array.

```python
boolean_array = np.array([[True, False], [False, False]])
boolean_array.astype(np.int32)
array([[1, 0], 
       [0, 0]], dtype=int32 )
```
Quando criamos um array a partir de uma Python list que contém diversos tipos de dados, ocorre o que chamamos de coerção de tipo.
```python
np.array([True, "Boop", 42, 42.42])
array(['True', 'Boop', '42', '42.42'], dtype='<U5)
# todos os elementos foram convertidos para string
```
Desta forma, se adicionarmos um float a um array de inteiros, isto mudará todos os inteiros para float, assim como adicionar um inteiro a um array de booleans mudará todos os booleans para inteiros ( False=0 e True=1).
___
# Selecionando e atualizando dados

### Indexação e fatiamento de arrays

**Indexação** (_indexing_) é um método baseado em ordem para acesssar dados. Indexação de NumPy é _zero-based_ , significando que primeiro índice é zero. A indexação utiliza colchetes, assim como em Python lists.
```python
array = np.array([2, 4, 6, 8, 10])
array[3]
8
```
Em um array 2D, passamos a informação de linha e coluna do elemento a ser retornado da seguinte forma:
```python
sudoku_game[2,4]
# retornará o elemento da linha 3, coluna 5
```
Se passarmos apenas um índice quando o array for 2D, será assumido que o índice refere-se à linha :
```python
sudoku_game[0]
array([0, 0, 4, 3, 0, 0, 2, 0, 9])
```
Podemos também selecionar uma coluna específica de um array 2D :
```python
sudoku_game[:, 3]
array([3, 0, 0, 0, 0, 0, 0, 5, 9])
```
**Fatiamento** (_slicing_) extrai um subconjunto de dados baseado em índices fornecidos de um array e cria um novo array com os dados fatiados. Passamos um valor de índice inicial e um final, sendo que o inicial será contido no fatiamento e o final não.

```python
array = np.array([2, 4, 6, 8, 10])
array[2:4]
array([6,8])
```
* podemos fazer um fatiamento 2D, informando como o fatiamento será feito nas linhas e nas colunas :
```python
sudoku_game[3:6, 3:6]
# informamos os índices de slicing das linhas e depois das colunas
```
* podemos também fornecer um terceiro número a um slicing, o passo (step). Isto pode ser feito tantos nas linhas quanto colunas ou em uma das dimensões apenas:
```python
sudoku_game[3:6:2, 3:6:2]
```
**np.sort()** - função que ordena um array dado um eixo:
* axis0 - refere-se a linhas;
* axis1 - refere-se a colunas;
O eixo (axis) padrão da função **np.sort** é o último do array, ou seja, um array 2D será ordenado pela coluna, eixo1.
```python
# ordenando pela coluna um array 2D
np.sort(sudoku_game)
# ordenando pela linha
np.sort(sudoku_game, axis=0)
```
### Filtrando arrays

Podemos filtrar dados conforme estes se encontrem sob determinadas condições ( filtro condicional ).

* boolean masks - o código para criar uma máscara checa se uma condição é verdadeira para cada elemento do array. A própria máscara é um array de _Booleans_ com o mesmo formato que o array avaliado. 
```python
# vamos selecionar os números pares de um array
one_to_five = np.arange(1,6)
one_to_five
array([1, 2, 3, 4, 5]) #saída
# criamos um array de Booleans que atende a condição procurada ( máscara )
mask = one_to_five % 2 == 0
mask
array([False, True, False, True, False])
```
* filtrando com fancy indexing - utilizamos a máscara para indexar o array avaliado. Este método é útil quando estamos interessados apenas nos elementos que encontram uma determinada condição. A máscara retorna apenas os elementos em que a condição é True no array avaliado.
```python
# utilizando o array mask
one_to_five[mask]
array([2,4])  #saída
```
* 2D fancy indexing - podemos retornar valores de uma coluna fazendo baseado em critérios verificados por outra coluna :
```python
# dado um array 2D com IDs das classes na primeira coluna e número de alunos na segunda coluna, vamos retornar os IDs das classes com quantidade par de alunos
classroom_ids_and_sizes = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
classroom_ids_and_sizes

array([[1, 22],
       [2, 21],
       [3, 27],
       [4, 26]]) # saída

classrrom_ids_and_sizes[:, 0][classroom_ids_and_sizes[:, 1] % 2 == 0]
array([1, 4]) # saída
```
**np.where()** - retorna um array de índices de elementos que atendem a uma condição. Isto é útil quando os índices são necessários posteriormente para direcionar o Numpy onde aplicar algum código. É possível também inserir elementos em um novo array conforme estes atendam a uma determinada condição.
```python
# a função np.where() retorna uma tupla de arrays de índices
np.where(classroom_ids_and_sizes[:, 1] % 2 == 0)
(array([0, 3]),) # saída

# podemos retornar dois sets de índices 
row_ind, column_ind = np.where(sudoku_game == 0)
row_ind, column_ind 
(array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4,
4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
 8, 8]), 
array([0, 1, 4, 5, 7, 0, 1, 3, 4, 6, 7, 0, 2, 3, 5, 6, 0, 1, 3, 4, 6, 2,
 3, 4, 7, 8, 0, 2, 3, 6, 7, 8, 1, 2, 3, 4, 5, 7, 0, 1, 4, 8, 0, 5,
7, 8]))

```
* o real poder do **np.where()** está na habilidade de checar se os elementos em uma linha ou coluna que atendam a uma condição e então inserir um elemento caso a condição seja encontrada ou não.
```python
# substituindo os elementos 0 do array pela string ''
# o primeiro argumento é a condição
# o segundo argumento é o caracter inserido caso a condição seja encontrada
# o terceiro argumento é o que será preenchido caso a condição não seja encontrada
np.where(sudoku_game == 0, "", sudoku_game)
array([['', '', '4', '3', '', '', '2', '', '9'],
       ['', '', '5', '', '', '9', '', '', '1'],
       ['', '7', '', '', '6', '', '', '4', '3'],
       ['', '', '6', '', '', '2', '', '8', '7'],       
       ['1', '9', '', '', '', '7', '4', '', ''],
       ['', '5', '', '', '8', '3', '', '', ''],
       ['6', '', '', '', '', '', '1', '', '5'], 
       ['', '', '3', '5', '', '8', '6', '9', ''],       
       ['', '4', '2', '9', '1', '', '3', '', '']])

```

### Adicionando e removendo dados

Em NumPy, concatenar arrays refere-se a adicionar dados a um array ao longo de qualquer eixo existente, como adicionar colunas a um array 2D. Nós concatenamos usando a função **np.concatenate()**. Os arrays a serem concatenados são passados na forma de uma tupla de arrays:
```python
# o padrão de concatenar do np.concatenate() é pelo primeiro eixo (adiciona linhas)
classroom_ids_and_sizes = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
new_classrooms = np.array([[5, 30], [5, 17]])
np.concatenate((classroom_ids_and_sizes, new_classrooms))
array([[ 1, 22],       
       [ 2, 21],       
       [ 3, 27],       
       [ 4, 26],       
       [ 5, 30],       
       [ 5, 17]])  # saída
```
* para concatenar ao longo de outras dimensões, devemos fazer uso do argumento _axis keyword_.
```python
classroom_ids_and_sizes = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
grade_levels_and_teachers = np.array([[1, "James"], [1,"George"], [3,"Amy"],
                                      [3, "Meehir"]])
np.concatenate((classroom_ids_and_sizes,grade_levels_and_teachers), axis=1)

array([['1', '22', '1', 'James'],
       ['2', '21', '1', 'George'],
       ['3', '27', '3', 'Amy'],
       ['4', '26', '3', 'Meehir']]) # saída
```
* compatibilidade de formato - as dimensões dos arrays a serem concatenados tem que ser as mesmas, exceto a dimensão ao longo da qual eles serão concatenados. Exemplo : um array 3x3 pode ser concatenado a um 3x2 ao longo da segunda dimensão(coluna).

* compatibilidade de dimensões - os dois arrays devem ter o mesmo número de dimensões. Quando estivermos, por exemplo, adicionando uma coluna a um array 2D com dados que estão em um array 1D, devemos utilizar o método reshape para converter o array 1D em 2D.
```python
array_1D = np.array([1, 2, 3])
column_array_2D = array_1D.reshape((3, 1))
column_array_2D
array([[1],       
       [2],       
       [3]])  # saída 
                     
row_array_2D = array_1D.reshape((1, 3))
row_array_2
Darray([[1, 2, 3]])  # saída

```

**np.delete()** - recebe três argumentos : 
* o array do qual devemos deletar dados;
* slice, índice ou array de índices a serem deletados;
* eixo ao longo do qual deve ser deletado;

```python
# deletando a segunda linha do array 2D classroom_data
# a deleção se dá pela linha índice=1 eaxis=0 (primeira dimensão - linha)
classroom_data
array([['1', '22', '1', 'James'],       
       ['2', '21', '1', 'George'],       
       ['3', '27', '3', 'Amy'],       
       ['4', '26', '3', 'Meehir']],)

np.delete(classroom_data, 1, axis=0)

array([['1', '22', '1', 'James'],       
       ['3', '27', '3', 'Amy'],       
       ['4', '26', '3', 'Meehir']]) # saída

# deletando a segunda coluna, índice=1 e axis=1(segunda dimensão - coluna)

np.delete(classroom_data, 1, axis=1)

array([['1', '1', 'James'],       
       ['2', '1', 'George'],       
       ['3', '3', 'Amy'],       
       ['4', '3', 'Meehir']]')  # saída

```
Se o argumento axis não for especificado ao fazer uma deleção, NumPy deletará o índice indicado ou índices ao longo de uma versão "achatada" ( 1D ) do array original.
___

# Matemática de arrays

### Resumindo dados
```python
security_breaches
array([[0, 5, 1],
       [0, 2, 0],
       [1, 1, 2],
       [2, 2, 1],
       [0, 0, 0]])
```
**.sum()** - soma todos os valores do array. podemos controlar qual eixo a somar com o argumento _axis_.
```python
security_breaches.sum()
17 # saída

# soma ao longo da primeira dimensão - linhas
security_breaches.sum(axis=0)
array([3, 10, 4])

#soma ao longo da segunda dimensão - colunas
security_breaches.sum(axis=1)
array([6, 2, 4, 5, 0])
```
**.min()** e **.max()** - retornam os valores mínimo e máximo de um array, respectivamente. Assim como em **.sum()**, podemos controlar o eixo a ser avaliado com o argumento _axis_.

```python
security_breaches.min()
0 #saída

security_breaches.max()
5 # saída

security_breaches.min(axis=1)
array([0, 0, 1, 1, 0]) # saída
```

**.mean()** - calcula a média de todo o array ou podemos calcular ao longo de uma dimensão com o argumento _axis_.
```python
security_breaches.mean()
1.1333333333333333 # saída

security_breaches.mean(axis=1)
array([2., 0.6667, 1.3333, 1.6667, 0.]) #saída

```
**argumento keepdims** - .sum(), .min(), .max() e .mean() possuem todos o argumento _keepdims keyword_. Se ele for passado como True, as dimensões que são colapsadas quando fazemos uso dos métodos citados, são mantidas no array de saída e passadas como um. Além de ser útil para compatibilidade dimensional ao concatenar, ele nos auxilia na visualização do eixo que originou os dados agregados.
```python
security_breaches.sum(axis=1, keepdims = True)
array([[6],
       [2],
       [4],
       [5],
       [0]]) # saída
```
**.cumsum()** - faz a soma cumulativa ao longo de um eixo do array.
```python
# soma cumulativa ao longo da dimensão zero - linhas
security_breaches.cumsum(axis=0)
array([[0, 5, 1],
       [0, 7, 1],
       [1, 8, 3],
       [3, 10, 4],
       [3, 10, 4]])  # saída
```

### Operações vetorizadas

NumPy realiza operações por meio de código em C, o que explica sua maior velocidade em relação a operações feitas em Python. Este uso da linguagem C pelo NumPy é chamado de _vetorização_. A operação desejada é realizada em todos os elementos do array de uma só vez.

**comparação de velocidade com Python** 
```python
# uma simples soma de um escalar a cada elemento de um array
# em Python puro - laço for é mais lento 
array = np.array([[1, 2, 3], [4, 5, 6]])
for row in range(array.shape[0]):
       for column in range(array.shape[1]):
              array[row][column] += 3

array([[4, 5, 6],
       [7, 8, 9]]) # saída

# com NumPy
array = np.array([[1, 2, 3], [4, 5, 6]])
array += 3

array([[4, 5, 6],
       [7, 8, 9]]) # saída

```
**somando/multiplicando/subtraindo ou dividindo dois arrays** - os arrays devem ter o mesmo formato para que isso seja possível. A operação é realizada entre os elementos em cada posição dos arrays.
```python
array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[0, 1, 0], [1, 0, 1]])
array_a + array_b

array([[1, 3, 3],
       [5, 5, 7]]) # saída
```
**vetorizando código Python** - operações vetorizadas são usadas ao criarmos máscaras, gerando um array de Booleans. 
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
array > 2

array([[False, False, True],
       [True, True, True]]) # saída
```
* Podemos vetorizar funções de Python com o comando **np.vetorize**

```python
# checar se cada elemento do array tem comprimento maior que 2
array = np.array(["NumPy", "is", "aewsome"])
len(array) > 2 # len() é uma função Python

True # saída

vectorized_len = np.vectorize(len) # vetorizando a função len()
vectorized_len(array) > 2

array([True, False, True])

```

### Broadcasting

Podemos fazer operações com arrays de diferentes formatos através de _broadcasting_ desde que suas dimensões sejam compatíveis.
**regras para checar compatibilidade para broadcasting**
* NumPy compara sets de dimensões da direita para a esquerda
* duas dimensões são compatíveis quando 
       * uma delas tem comprimento igual a um;
       * elas tem comprimentos iguais;
* todos os sets de dimensão precisam ser compatíveis

arrays _"broadcastable"_ | arrays não "_broadcastable_" 
:-----------------------:|:---------------------------:   
(10, 5) e (10, 1) | (10, 5) e (5, 10) 
(10, 5) e (5,) | (10, 5) e (10, )

```python
array = np.arange(10).reshape((2, 5))
array + np.array([0, 1, 2, 3, 4])

array([[0, 2, 4, 5, 8],
       [5, 7, 9, 11, 13]]) # saída
```
___
# Transformações de array

### Salvando e carregando arrays

Arrays NumPy podem ser salvos em vários formatos como:
* .cvs;
* .txt;
* .pkl;
* .npy - em termos de eficiência de memória e velocidade é o melhor;

**loading** - para carregar um arquivo **.npy** 
```python
# open tem dois argumentos
# primeiro é o nome do arquivo
# segundo é o modo em que será aberto. rb - read binary
with open("logo.npy", "rb") as f:
       logo_rgb_array = np.load(f)

```
**saving arrays como arquivos .npy** - o nome do arquivo em _open_ é o nome com o qual o arquivo em _np.save_ será salvo. O arquivo **.npy** não precisa existir e , caso exista, será sobrescrito.

```python
# wb - writ binary
with open("dark_logo.npy", "wb") as f
       np.save(f, dark_logo_array)
```
### Array acrobatics

Podemos rearranjas um array mudando a ordem de seus eixos ou de seus alementos array.

* data augmentation - em machine learning é o processo pelo qual podemos adicionar novos dados fazendo pequenas alterações em dados já existentes.

**flipping um array** - **np.flip** inverte a ordem dos elementos de um array. Por padrão isto é feito ao longo de todos os eixos, mas podemos determinar ao longo de qual eixo o processo será realizado.
```python
# flipping ao longo de todos os eixos
flipped_logo = np.flip(logo_rgb_array)

# flipping ao longo do eixo da primeira dimensão 
flipped_rows_logo = np.flip(logo_rgb_array, axis =0)

# flipping ao longo de múltiplos eixos
flipped_rows_logo = np.flip(logo_rgb_array, axis = (0, 1))
```
**transposing um array** - flipa a ordem dos eixos mantendo a ordem nos elementos em cada um dos mesmos. Podemos especificar a ordem dos eixos usando o argumento _axes_ , devendo ser passado todos os eixos do array, mesmo que algum deles não mude de posição.
```python
# diferença entre flipping e transposing
array = np.array([[1.1, 1.2, 1.3],                   
                  [2.1, 2.2, 2.3],                   
                  [3.1, 3.2, 3.3],                   
                  [4.1, 4.2, 4.3]])
np.flip(array)

array([[4.3, 4.2, 4.1],       
       [3.3, 3.2, 3.1],       
       [2.3, 2.2, 2.1],       
       [1.3, 1.2, 1.1]]) #saída

array = np.array([[1.1, 1.2, 1.3],
                  [2.1, 2.2, 2.3],                   
                  [3.1, 3.2, 3.3],                   
                  [4.1, 4.2, 4.3]])
np.transpose(array)

array([[1.1, 2.1, 3.1, 4.1],
       [1.2, 2.2, 3.2, 4.2],       
       [1.3, 2.3, 3.3, 4.3]]) # saída

# transposing configurando a ordem dos eixos - mudança de 0,1 para 1,0 , mantendo o 2
transposed_logo = np.transpose(logo_rgb_array, axes=(1, 0, 2))

```


### Stacking e splitting

**slicing dimensions** 

```python
# o array rgb é 3D formado por arrays 2D referentes às cores vermelha, verde e azul

rgb = np.array([[[255, 0, 0], [255, 255, 0], [255, 255, 255]],
                [[255, 0, 255], [0, 255, 0], [0, 255, 255]],
                [[0, 0, 0], [0, 255, 255], [0, 0, 255]]])
red_array = rgb[:, :, 0]
green_array = rgb[:, :, 1]
blue_array = rgb[:, :, 2]
red_array

array([[255, 255, 255],   
       [255,   0,   0],       
       [0,   0,   0]]) # saída

```

**splitting arrays** - desempacotando arrays. Aceita três argumentos : o array origem, número de arrays de tamanhos iguais desejados após o split e o eixo ao longo do qual será feito o split. Caso não seja possível para o NumPy criar o número de arrays de tamanhos iguais desejado, é retornado um erro.
```python
red_array, green_array, blue_array = np.split(rgb, 3, axis=2)
red_arrayarray([[[255], [255], [255]],       
                [[255], [  0], [  0]],       
                [[  0], [  0], [  0]]])
red_array.shape
(3, 3, 1) # saída
```
**trailing dimensions** - se uma das dimensões do array resultante for igual a um, podemos removê-la com _reshape_.

```python
red_array_2D = red_array.reshape((3, 3))
red_array_2Darray([[255, 255, 255],       
                   [255,   0,   0],       
                   [  0,   0,   0]]) # saída
red_array_2D.shape
(3, 3) #saída
```
**stacking arrays** - é mais fácil trabalhar em arrays com menos dimensões. Após fazermos _split_ e _slice_ em um array, podemos usar **np.stack** para reagrupar o array. np.stack precisa que todos os arrays tenham o mesmo formato e número de dimensões.

```python
stacked_rgb = np.stack([red_array, green_array, blue_array], axis=2)
plt.imshow(stacked_rgb)
plt.show()

```
