quest = float(input('Qual seu nível de experiência?'))
experiencia = quest
if experiencia <= 5 :
    mensagem = 'Nível de conhecimento Júnior.'
elif experiencia > 5:
    mensagem = 'Nível de conhecimento Pleno.'
print(str(mensagem))