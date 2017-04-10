
# Jeu de roulette

fonctionnalité : jouer à la roulette
  En tant que joueur

  Je veux
      jouer à  la roulette
      et miser une somme d'argent
      sur un numéro de la roulette compris entre 0 et 49
  afin de gagner
     3 fois ma mise si mon numéro sort
    la moitié de ma mise si ma couleur sort.
  ou bien
    ne rien gagner dans les autres cas

Scenario: Je commence à jouer à la roulette
Etant donné que
    je n'ai pas encore joué à la roulette
quand 
    je lance l'application
et 
    avant de jouer la première partie 
alors
    le croupier me souhaite la bienvenue à la table

Scenario: j'ai fini ma partie
Etant donné que
    j'ai gagné ou perdu à la roulette
et que
    j'ai autant d'argent que je veux
quand
    on me demande si je veux rejouer
alors
    je rejoue autant de fois que je le veux
et 
    j'arrête quand je le décide
 
Scenario: Je mise une somme sur un numéro
Etant donné que 
    j'ai décidé de jouer une partie à la roulette 
Quand 
    le croupier annonce "Faites vos jeu !"
Alors 
    je mise la somme que je veux
et
    je choisi un numéro entre 0 et 49
et
    la couleur du numéro est annoncée, 
    noir si le numero est pair,
    rouge si le numéro est impair,
et
    pour finir la roulette est lancée automatiquement


Scénario: La roulette donne le numéro gagnant 
Etant donné que
    La roulette à été lancée
et que
    Le croupier à annoncé "rien ne va plus"
Quand
    elle s'arrête 
Alors
    la roullette donne un numéro aléatoire entre 0 et 49
et    
    Le croupier annonce le numéro gagnant 
et
    il annonce la couleur gagnante.



Contexte : J'ai joué et un numéro est gagnant 
Etant donné que
    j'ai joué un numéro
Et que 
    j'ai misé une somme sur ce numéro
Et que
    la roulette a donné un numéro gagant
Et qu'
    une couleur gagante est associée au numéro gagnant 


Scenario: J'ai joué le numéro gagnant
Etant donné que
    J'ai joué et un numéro est gagnant
Quand 
    mon numéro est égal au numéro gagnant
Alors
    mon gain est de trois fois ma mise
et
    le croupier annonce mon gain


Scenario: J'ai jouée la couleur gagante
Etant donné  que
    J'ai joué et un numéro est gagnant
quand 
    ma couleur jouée est egale à la couleur gagante
Alors
    mon gain est la moitié de ma mise
et
   le croupier annonce mon gain


Scénario : J'ai joué un numéro et une couleur perdantsMon numéro et ma couleur sont perdants
Etant donné  que
    J'ai joué et un numéro est gagnant
Quand
    mon numéro n'est pas égal au numero gagnant 
et que
    ma couleur n'est pas la couleur gagnante
alors
    mon gain est de zéro 
et
    je me dis que "j'ai perdu !"
