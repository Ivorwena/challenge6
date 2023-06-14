#!/bin/bash

cd /home/administrator
mkdir Recipes
cd Recipes

mkdir Desert
mkdir Meat
mkdir Pasta
mkdir Salad

cd Desert
touch Brownies.txt

cat <<EOT>> Brownies.txt
Could not find the perfect one...

EOT


touch Cheesecake.txt

cat <<EOT>> Cheesecake.txt
All of them seems delicious~
https://www.foodandwine.com/desserts/cheesecakes/cheesecake-recipes

EOT



cd ../Meat
touch Grilled_chicken.txt

cat <<EOT>> Grilled_chicken.txt
Still working on this one~

EOT

touch Pork_chops.txt

cat <<EOT>> Pork_chops.txt
There were 27 recipes, choose whichever you like: https://www.foodandwine.com/meat-poultry/pork/pork-chop/pork-chop-recipes 

EOT

cd ../Pasta
touch Baked_spaghetti.txt

cat <<EOT>> Baked_spaghetti.txt
I think it is gonna be too dry, but some people like it. 

EOT

touch Penne_ala_vodka.txt

cat <<EOT>> Penne_ala_vodka.txt
Have no idea what it is, but it is not important~ 

EOT

cd ../Salad
touch Coleslaw.txt

cat <<EOT>> Coleslaw.txt
For recipe go to:
https://www.bbcgoodfood.com/recipes/classic-homemade-coleslaw

EOT

touch Greek_salad.txt

cat <<EOT>> Greek_salad.txt
Place 4 large vine tomatoes, cut into wedges, 1 peeled, deseeded and chopped cucumber, half of a thinly sliced red onion, 16 Kalamata olives, 1 table spoon of dried oregano, 85g feta cheese chunks and 4 tbsp Greek extra virgin olive oil in a large bowl. Lightly season, serve it with crusty bread to mop up all of the juices.

EOT

cd ../..
chmod -R 777 Recipes
