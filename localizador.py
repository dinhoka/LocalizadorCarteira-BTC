# Importa as bibliotecas necessárias
import bitcoin
import requests

# Chave privada inicial em formato hexadecimal
private_key_sequence = "000000000000000000000000000000000000000000000001a838b13505b20067"

# Número de carteiras a serem geradas e verificadas
num_wallets = 10000000

# Endereço alvo que você deseja encontrar
target_address = "18ZMbwUFLMHoZBbfpCjUJQTCMCbktshgpe"

# Flag para verificar se a carteira foi encontrada
found = False

# Armazena a última chave privada gerada
last_private_key = None

# Loop através do número especificado de carteiras
for i in range(num_wallets):
    # Gera a chave privada incrementalmente
    private_key_int = int(private_key_sequence, 16) + i
    private_key_hex = hex(private_key_int)[2:].zfill(64)

    # Converte a chave privada para o formato WIF comprimido
    wif_key = bitcoin.encode_privkey(private_key_int, 'wif_compressed')

    # Deriva a chave pública e os endereços correspondentes
    public_key = bitcoin.privkey_to_pubkey(private_key_hex)
    uncompressed_address = bitcoin.pubkey_to_address(public_key)
    compressed_public_key = bitcoin.compress(public_key)
    compressed_address = bitcoin.pubkey_to_address(compressed_public_key)

    # Verifica se algum dos endereços corresponde ao endereço alvo
    if uncompressed_address == target_address or compressed_address == target_address:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Carteira encontrada!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Endereço: " + target_address)
        print("Chave Privada: " + private_key_hex)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Carteira encontrada!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        found = True
        break

    # Armazena a última chave privada gerada
    last_private_key = private_key_hex

# Se a carteira não for encontrada, exibe uma mensagem
if not found:
    print("Carteira não encontrada após verificar", num_wallets, "carteiras.")

# Exibe a última chave privada gerada
if last_private_key:
    print("Última chave privada gerada:", last_private_key)
