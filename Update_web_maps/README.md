# Update_web_maps

Use case: I need to replace existing layers with new ones.

## Set up

On my desktop I am using an existing conda environment called "arcgis_tools"
which should already have what I need in it. Namely, "arcgis.py".

(See also the arctic repo.)

    conda activate arcgis_tools

Create the .env file, and don't check it in.

    PORTAL=yourportal
    USER=
    PASSWORD=

## The scripts

### extract_layer.py

Extracts the layers we need to update from the CC Map Template.

Currently the files extracted are

* layers/taxlots.json
* layers/county_aerials_brief.json
* layers/county_aerials.json
* layers/roads.json

Next, I can edit these files by hand.
Then you should feed them back into the template map using "map_repair"!
That way I don't extract the wrong layers next time I run an extract.

### map_repair.py (working for now!!)

Writes JSON layer files (both operational and basemap layers) into the mapfiles.
Finds the list of layers by querying the Portal.

### old_map_repair.py

Clumsy version that will find all the maps using
the old services or whatever, and replace it with the new.
### find_map_layers.py (deprecated)

This will look for all the maps in Portal and list them.
You can set various queries and filters.

It generates a python list that you can paste into other scripts,
for example, repair_maps.py

### build_taxlots.py (WIP)

Generates the JSON for a taxlot layer from misc input.

## Resources 

There are samples in the arcgis.py repo, start there.
See "05_content_publishers/using_and_updating_GIS_content"

