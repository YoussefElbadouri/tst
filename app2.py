import os

# 🔥 Commande système dangereuse
user_cmd = input("Entrez une commande système : ")
os.system(user_cmd)

# 🔥 Injection de code via eval
user_code = input("Entrez une expression à exécuter : ")
eval(user_code)

print("Bienvenue")
