# The Farmer Was replaced

[Click here](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) to check out the game on steam.

## Features

- Season 1: Polyculture (grass,bush,tree,carrot)
  |- Default is to plant regularly in sets of 3, but after planting get_companion and store it in a dict.
  |- Before planting check and plant if there is a more optimal crop.

## Files

Plant_Planner.py

## Approach

- Splitting the field with different crops allows for all kinds of plants to be harvested, but it may not the most optimal way to grow each plant.
- Instead a seasonal approach may be better where plants of similar condiitons should be allowed to grow together so that harvesting is easier.

## Plants

- Pumpkins get a cubic multiper up to n=6.
  |- for n > 6, yield = 6n^2 (e.g. for n=7, yield = 294)
  |- n = 12, yield = 864 = 4 n =6 plots
