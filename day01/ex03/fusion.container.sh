#!/bin/bash

# SELECT id, prenom, nom, utilisateur_id, date_achat, num_facture
# FROM utilisateur
# FULL JOIN commande ON utilisateur.id = commande.utilisateur_id

# psql -U trobin piscineds << END
#     SELECT * FROM customers
#     FULL JOIN items ON customers.product_id = items.product_id
# END
