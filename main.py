from KeyGenerator import KeyGenerator

from bitcoin import BitcoinWallet

kg = KeyGenerator()

btc=BitcoinWallet()

kg.seed_input("Truly random string. I rolled a dice and got 4.")

private_key=kg.generate_key()

address=btc.generate_compressed_address(private_key)

print(address)

