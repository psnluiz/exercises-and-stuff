import random
words = ['swordfish', 'owen', 'passw', 'wordis']
s_words = ['LighT', 'FiRe', 'PaSS', 'theWorD']
try:
    user_choice = input("\nHow strong should be your password?(weak/medium/strong)\n")
except ValueError:
    print("Use the answers between the parentheses.")
if user_choice == 'weak':
    pw = random.choice(words)
    print(pw)
elif user_choice == 'medium':
    pw = random.choice(words) + str(random.randint(0, 10))
    print(pw)
elif user_choice  == 'strong':
    pw = random.choice(s_words) + str(random.randint(0, 10))
    print(pw)
    
                        
