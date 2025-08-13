import random

def cumprimento(texto):
    return f"Olá, {texto}"

print(cumprimento("Antonio Francisco Batista Filho"))

def sortear_e_calcular_media():
  nums = random.sample(range(1, 101), 7)
  soma = sum(nums)
  media = soma / 7
  
  return media

print(sortear_e_calcular_media())
