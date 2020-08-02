# python-plexlibrary-list-generator
Simple script to bulk generate yml list to import in [python-plexlibrary](https://github.com/adamgot/python-plexlibrary) by `adamgot`. Great if you have a lot of custom lists. 

See `createlist.py` and modify the following to your needs
```
# Placeholder in the YML file to replace, change this to your need
TRAKT_USERNAME = 'd-sync' # trakt. username
SRC_MEDIA_PATH = '/mnt/downloads/media-staging/' # location to your original video file
NEW_LIB_PATH = '/mnt/downloads/python-plexlibrary-lib' # location to the new lib, this will contain soft link to the original media path above
```

Once the recipe is generated, move them to your `python-plexlibrary\recipes` path and run `python3 plexlibrary -l` to view the recipes

Examples
```
deluge23@server663:~/python-plexlibrary$ python3 plexlibrary/ -l
Available recipes:
    movies_d-sync_action
    movies_d-sync_action_comedy
    movies_d-sync_action_police
    movies_d-sync_adventure
    movies_d-sync_airplane
    movies_d-sync_alien
    movies_d-sync_alien_invasion
    movies_d-sync_animation
    movies_d-sync_apocalypse
    movies_d-sync_bollywood
    movies_d-sync_camcorder_mockumentary
    movies_d-sync_cg
    movies_d-sync_collection_set
    movies_d-sync_comedy
    movies_d-sync_comedy_horror
    movies_d-sync_crime
    movies_d-sync_dinosaur
    movies_d-sync_drama
    movies_d-sync_family
    movies_d-sync_fantasy
    movies_d-sync_favorite
    movies_d-sync_forest
    movies_d-sync_hijacking
    movies_d-sync_horror
    movies_d-sync_interesting_plot
    movies_d-sync_island
    movies_d-sync_kidnapping
    movies_d-sync_magic_sorcery_witchcraft
    movies_d-sync_marvel_heroes
    movies_d-sync_mummies
    movies_d-sync_murder_mystery
    movies_d-sync_mystery
    movies_d-sync_pandemic
    movies_d-sync_possessed_doll
    movies_d-sync_psychological_thriller
    movies_d-sync_robots
    movies_d-sync_romance
    movies_d-sync_sci_fi
    movies_d-sync_seduction
    movies_d-sync_shapeshifter
    movies_d-sync_slasher
    movies_d-sync_space
    movies_d-sync_space_travel
    movies_d-sync_superheroes
    movies_d-sync_supernatural_and_paranormals
    movies_d-sync_template
    movies_d-sync_thriller
    movies_d-sync_time_loop
    movies_d-sync_time_travel
    movies_d-sync_train
    movies_d-sync_vacation
    movies_d-sync_vampires
    movies_d-sync_video_game_character_adaptation
    movies_d-sync_watchlist
    movies_d-sync_zombies

```

## Optional
To sync **ALL** the recipes to Plex, run the following
```
./sync_all_recipes /path/to/python-plexlibrary
```

My trakt.tv list if you're interested:
https://trakt.tv/users/d-sync/lists
