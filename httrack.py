import os

alvo = str(input("Digite o site alvo, incluindo o http:// ou https:// : "))

os.environ["TESTSITE"] = alvo

os.system('~/Programacao/HTTrack_lab/httrack.sh')
