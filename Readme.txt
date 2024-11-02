les instructions pour lancer le Projet:
1-lancez le serveur Django : py manage.py runserver
2-lancez React : npm run start


L'application se compose de trois composants principaux :

Record.jsx : Ce composant gère l'état des enregistrements et réalise les appels API pour effectuer des opérations telles que la récupération, l'ajout, la mise à jour et la suppression d'enregistrements.

RecordForm.jsx : Ce composant est dédié à l'ajout de nouveaux enregistrements. Il utilise l'état local pour stocker temporairement les données saisies par l'utilisateur et appelle la fonction d'ajout lors de la soumission du formulaire.

RecordList.jsx : Ce composant affiche la liste des enregistrements et permet aux utilisateurs d'éditer ou de supprimer des entrées.



Le fichier views.py contient des vues Django pour gérer des requêtes HTTP liées au modèle Record:

Fonction records_list: 
- Gère la requête GET pour renvoyer la liste de tous les enregistrements de type Record et POST pour crée un nouvel enregistrement.

Fonction record_detail:
-Gère les requêtes GET DELETE et PUT pour un enregistrement spécifique identifié par son id.