
from random  import seed, randint

INIT_RND = None
NUM_MIN = 0
NUM_MAX = 49
COULEUR = ['noir','rouge']
GAIN_NUMERO = 3
GAIN_COULEUR = 0.5

message = \
	   {
	   "debut partie": "Bonjour!\nBienvenue à la table de la roulette!",
    "question arret" : "\nVoulez vous arrêter de jouer ?\nOuï : O+<enter> ou pour continuer <enter> : ",
    "fin partie" : "\nJ'ai fini de jouer.\nAurevoir !",
    "debut mise" : "\nFaite vos jeux !\n",
    "question mise": "Je vais miser : ",
    "question numero" : "sur le numéro : ",
    "mise couleur" : "et la couleur : {0}",
    "recap mise" : "\nJ'ai donc misé {0}€ sur le {1} et le {2}!\n",
    "rien va plus" : "\nLes jeux sont faits!\n...\nrien ne va plus !\n...",
    "numero roulette" : "le {0} {1} est gagnant !\n",
    "numero gagnant" : "Vous gagnez {0}€\nSuper!Je gagne {1} fois ma mise!",
    "couleur gagnant" : "Vous gagnez {0}€\nOuf !\nJe récupère la moitié de ma mise!",
    "numero perdant" : "C'est con ! J'ai perdu !"
    }
def estSommeMiseValide(montant):
    try:
        maMise = int (montant)
    except ValueError:
        print ("Erreur ! Saisir un nombre entier !")
        maMise = 0
    else:
        if (maMise < 0) or (montant % 1 != 0):
            maMise = 0
    finally:
        return maMise

        
def estNumeroMiseValide(numero):
    try:
        monNumero = int (numero)
    except ValueError:
        print ("Erreur ! Saisir un chiffre  entier compris entre {0} et {1}".format(NUM_MIN, NUM_MAX))
        monNumero = -1
    else:
        if ((monNumero < NUM_MIN) or (monNumero > NUM_MAX) or (numero % 1 != 0)):
            print ("Erreur ! Saisir un numero compris entre {0} et {1}".format(NUM_MIN, NUM_MAX))
            monNumero = -1         
    finally:
        return monNumero
        
def couleurNumero(leNumero):
    try:
        laCouleur = COULEUR[leNumero % 2]
    except TypeError:
        laCouleur = "n.c."
    finally:
        return laCouleur
            
def miseSomme():
    
    maMise = 0
    while not (maMise > 0):
        saisie = input(message ['question mise'])
        maMise = estSommeMiseValide(saisie) 
    return maMise
    
def miseNumero ():
    monNumero = -1
    while monNumero == -1:
        monNumero = estNumeroMiseValide(input(message ['question numero']))
    maCouleur = couleurNumero(monNumero)
    print (message['mise couleur'].format (maCouleur)) 
    return monNumero
    
  
    
def numeroRoulette(initRandom = None):
    if initRandom != None:
        seed (initRandom)
    return randint(NUM_MIN,NUM_MAX)
    
def numeroGagnantRoulette(initRandom = None):
    print(message ['rien va plus'])
    numeroGagnant = numeroRoulette(initRandom)
    couleurGagnante = couleurNumero(numeroGagnant)
    print (message ['numero roulette'].format(numeroGagnant, couleurGagnante))
    return numeroGagnant
    
def gainPartie(mise, numero, numeroGagnant):
    gaïn=0
    if numero == numeroGagnant:
        gain = GAIN_NUMERO * mise
        print(message['numero gagnant'].format(gain, GAIN_NUMERO))
        
    elif couleurNumero(numero) == couleurNumero(numeroGagnant) :
       gain = GAIN_COULEUR * mise 
       print(message['couleur gagnant'].format(gain))
    else:
        gain = 0
        print(message['numero perdant'].format(gain))
    return gain
     
def jouerUnePartie():
    # Je mise une somme sur un numéro
    print (message ['debut mise'])
    mise = miseSomme()
    numero = miseNumero()
    # récapitulatif de la mise
    print (message ['recap mise'].format(mise, numero, couleurNumero(numero)))
    
    # Annonce du numéro et de la couleur gagants
    numeroGagnant = numeroGagnantRoulette(INIT_RND)
    # annonce du gain si gagné
    gain = gainPartie (mise, numero, numeroGagnant)
    
def jouer():
    # je commence à jouer
    print(message['debut partie'])
    while True:
        # Faire une partie
        jouerUnePartie()
        # jusqu'à ce que je veuille arrêter      
        if input (message['question arret']) == "O":
            print(message ['fin partie'])
            break

if __name__ == '__main__' :
    #INIT_RND =1 
    jouer()