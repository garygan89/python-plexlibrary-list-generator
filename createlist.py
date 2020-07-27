import os
import shutil
import re

INPUT_LIST = 'list.txt' # Format is <yml filename>,<library name>
PREFIX = 'movies_d-sync_' # prefix for the yml file
INPATH = 'movies_d-sync_template.yml' # template file
OUTDIR = 'recipes'

# Placeholder in the YML file to replace, change this to your need
TRAKT_USERNAME = 'd-sync' # trakt. username
SRC_MEDIA_PATH = '/mnt/downloads/media-staging/' # location to your original video file
NEW_LIB_PATH = '/mnt/downloads/python-plexlibrary-lib' # location to the new lib, this will contain soft link to the original media path above

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

if not os.path.exists(OUTDIR):
    os.mkdir(OUTDIR)

# 1. Make a copy of the yml template
with open (INPUT_LIST, 'r') as file:
    lines =  file.readlines()

for line in lines:
    line = line.rstrip()
    token = line.split(',')
    
    listname = token[0].strip()
    library_name = token[1].strip()
    outfilename = '{}{}.yml'.format(PREFIX, listname)
    outpath = os.path.join(OUTDIR, outfilename)
    print('Copying {} to {}'.format(INPATH, outpath))
    shutil.copy(INPATH, outpath)
    
    # 2. Replace the placeholder in yml file
    dict = {
        "<LISTNAME>" : listname.replace('_', '-'), # spaces or special char is replaced with '-' in trakt
        "<LIBNAME>" : library_name,
        "<TRAKT_USERNAME>" : TRAKT_USERNAME,
        "<SRC_MEDIA_PATH>" : SRC_MEDIA_PATH,
        "<NEW_LIB_PATH>" : NEW_LIB_PATH
    }     
    
    with open (outpath, 'r') as yml:
        new_text = multiple_replace(dict, yml.read())
    with open (outpath, 'w') as yml:    
        yml.write(new_text)