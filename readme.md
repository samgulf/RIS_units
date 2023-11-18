# Rome Imperium Surrectum unit cross-checker
This tool is designed to do two things:
1. create a csv file contains all the RIS units with their stats, descriptions and building requirements
2. check for inconsistencies between the export_descr_unit.txt and export_descr_buildings.csv

It was written for RIS 0.6.3, and uses regular expressions to process the text files, so any major changes 
to file structure that occur as a result of further development will probably break it.

It assumes data structures as per https://www.twcenter.net/forums/showthread.php?111344-The-Complete-EDU-Guide

## Setup
Install the conda environment from environment.yml (see here for instructions: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file), or just read environment.yml and manually install those packages if you're not using conda.

## Inputs
The code needs the following files to be put into the inputs folder (because these are the files it checks):
- export_descr_buildings.txt
- export_descr_units.txt
- export_units.txt

## Outputs
The code produces the following output csvs:
1. ris_units_no_buildings.csv - this contains just the units with stats and descriptions but no information about building requirements. It only contains player recruitable units.
2. ris_units_combined - this contains the units with stats, descriptions AND building requirements. It only contains player recruitable units.
3. blank_building_requirements.csv - this contains any units that don't have a building requirement (which are probably bugs)
4. inconsistent_buildings.csv - this contains any units that have inconsistent requirements across factions. This may be correct (e.g. requiring faction-specific hidden resources, but may also highlight some bugs)
5. unit_cross_check_issues.csv - this contains a comparison of here base, aor and merc variants of units are inconsistent across the units and buildings file (probably bugs).
6. aor_unit_diffs.csv - this contains any aor units that have different numeric stats from their base units (probably bugs). 