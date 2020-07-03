import os
import re

alvo = str(input("Digite o site alvo, sem o http:// https:// ou www: "))

os.environ["TESTSITE"] = alvo
os.environ["DESTINY"] = str(alvo)

os.system('~/Programacao/HTTrack_lab/httrack.sh')
