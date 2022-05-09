#Petite application pour replacer ensemble des pages numérisées#
J'ai créé ce script Python pour pouvoir directement réunir deux fichiers contenant les pages de droite et les pages de gauche d'une numérisation faite en deux morceaux.

Il faut placer un fichier à la racine dans lequel il faut créer deux fichiers : un fichier appelé pages de droite impaires et un fichier pages de gauche paires à la racine, chacun contenant la bonne moitié des scans.

Un nouveau fichier appelé "complet" sera créé au même niveau que les fichiers de page de droite et de page de gauche.

Il suffit simplement de modifier les variables (path contenant le nom du fichier contenant les fichiers de moitié de scans, à modifier dans scri1 et scri2).

Il faut lancer le scri1, qui appelera également scri2. 
