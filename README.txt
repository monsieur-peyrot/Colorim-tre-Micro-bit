Colorimètre à Micro-Bit :

* Le programme "colorimetre.py" permet de mesurer l'absorbance d'une solution.
Lors du lancement du programme, l'écran de la Micro-bit affiche un point d'interrogation. La console série affiche le menu suivant :

A : Etalonnage
B : Mesures

Si on veut étalonner le colorimètre, on positionne la cuve d'eau distillée, puis on appuie sur le bouton A de la M:B. L'écran intégré
affiche "0" et la console série affiche "Veuillez insérer le blanc puis appuyez sur A". Lorsque la cuve de blanc est en place, appuyez
sur le bouton A. La console série affiche "Etalonnage OK" et on revient au menu.

Pour faire une mesure, on insère la cuve contenant la solution à étudier, et on appuie sur "B". L'écran intégré affiche "M" pendant
environ une seconde, puis la console série affiche la valeur de l'absorbance, et on revient au menu.

N.B.: pour éviter les fluctuations, la M:B effectue mille mesures successives, puis calcule une moyenne.

* Le programme "cinetique.py" fonctionne de la même façon pour la partie étalonnage.
Lorsqu'on veut effectuer le suivi de la cinétique, on positionne la cuve, puis on appuie sur le bouton B.L'écrzn intégré affiche "M"
et la console série affiche "Début des mesures : appuyez sur B pour arrêter". La M:B va alors réaliser une mesure d'absorbance toutes
les secondes, et affiche dans la console série le temps en seconde et la valeur de l'absorbance pour chaque mesure.
Il suffit de capturer le flux de la console série afin de transférer les données dans un tableur / grapheur.
