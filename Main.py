import datetime as date
from Block import Block

#crea el bloque inicial
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block Data", "")


#crea un bloque
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Datos de transacción " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)


#creamos el arreglo blockchain donde iremos agregando nuestros bloques
blockchain = [create_genesis_block()]
#seleccionamos el bloque genesis
previous_block = blockchain[0]

#numero de bloques a añadir
num_of_blocks_to_add = 20

#Agregamos bloques a la cadena
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  print("Bloque #{} ha sigo agregado al blockchain!".format(block_to_add.index))
  print("Hash: {}\n".format(block_to_add.hash))



