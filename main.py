from bip44 import Wallet
from bip44.utils import get_eth_addr
from mnemonic import Mnemonic

mnemo = Mnemonic("english")
words = mnemo.generate()
wallet_words = Wallet(words)

print("\n\nMnemonic: {}".format(words))
print("\nAddresses and private keys:\n")

for i in range(20):
    sk, pk = wallet_words.derive_account("eth", address_index=i)
    print("{} {} {}".format(i, get_eth_addr(pk), sk.hex()))
    
print("\n")
