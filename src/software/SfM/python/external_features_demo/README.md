**About**

The [Kornia](https://github.com/kornia/kornia) demo script will extract [DISK](https://kornia.readthedocs.io/en/latest/feature.html#kornia.feature.DISK) features and match them with [LightGlue](https://kornia.readthedocs.io/en/latest/feature.html#kornia.feature.LightGlueMatcher) as well as export features, descriptors, and matches.

**Install dependencies**
```
$ pip install -r requirements.txt
```

If install `pyvis` is not working, you can try `conda install --channel conda_forge pyvis`

**How to use**
```
$ python kornia_demo.py --input <string> --matches <string> --output <string>
```
To see all options:
```
$ python kornia_demo.py -h
```

**Example**

Dataset: https://github.com/openMVG/ImageDataset_SceauxCastle

Using pair selection (i.e. VLAD):
```
$ openMVG_main_SfMInit_ImageListing -i "...\ImageDataset_SceauxCastle\images" -o "...\ImageDataset_SceauxCastle\images\sfm\matches" -d "...\sensor_width_camera_database.txt"
$ python kornia_demo.py -i "...\ImageDataset_SceauxCastle\images\sfm\matches\sfm_data.json" -m "...\ImageDataset_SceauxCastle\images\sfm\matches" --preset EXTRACT
$ openMVG_main_ComputeVLAD -i "...\ImageDataset_SceauxCastle\images\sfm\matches\sfm_data.json" -o "...\ImageDataset_SceauxCastle\images\sfm\matches" -p "...\ImageDataset_SceauxCastle\images\sfm\matches\vlad_pairs.txt"
$ python kornia_demo.py -i "...\ImageDataset_SceauxCastle\images\sfm\matches\sfm_data.json" -m "...\ImageDataset_SceauxCastle\images\sfm\matches" -p "...\ImageDataset_SceauxCastle\images\sfm\matches\vlad_pairs.txt" --preset MATCH
```

Using exhaustive pair match:
```
$ openMVG_main_SfMInit_ImageListing -i "...\ImageDataset_SceauxCastle\images" -o "...\ImageDataset_SceauxCastle\images\sfm\matches" -d "...\sensor_width_camera_database.txt"
$ python kornia_demo.py -i "...\ImageDataset_SceauxCastle\images\sfm\matches\sfm_data.json" -m "...\ImageDataset_SceauxCastle\images\sfm\matches" --preset EXTRACT
$ python kornia_demo.py -i "...\ImageDataset_SceauxCastle\images\sfm\matches\sfm_data.json" -m "...\ImageDataset_SceauxCastle\images\sfm\matches" --preset MATCH
```

Afterwards, run openMVG_main_GeometricFilter and openMVG_main_SfM as normal.


openMVG_main_SfMInit_ImageListing -i /home/Ascent-openMVG/SfM_data/images -o /home/Ascent-openMVG/SfM_data -k "15294.117647058822;0;540.0;0;15294.117647058822;960.0;0;0;1"
openMVG_main_ComputeFeatures -i /home/Ascent-openMVG/SfM_data/sfm_data.json -o /home/Ascent-openMVG/SfM_data/matches
openMVG_main_ComputeVLAD -i /home/Ascent-openMVG/SfM_data/sfm_data.json -o /home/Ascent-openMVG/SfM_data/matches -p /home/Ascent-openMVG/SfM_data/matches/vlad_pairs.txt
openMVG_main_ComputeMatches -i /home/Ascent-openMVG/SfM_data/sfm_data.json -p /home/Ascent-openMVG/SfM_data/matches/vlad_pairs.txt -o /home/Ascent-openMVG/SfM_data/matches/matches.putative.bin
openMVG_main_GeometricFilter -i /home/Ascent-openMVG/SfM_data/sfm_data.json -m /home/Ascent-openMVG/SfM_data/matches/matches.putative.bin -p /home/Ascent-openMVG/SfM_data/matches/vlad_pairs.txt -o /home/Ascent-openMVG/SfM_data/matches/matches.f.bin -g f
openMVG_main_SfM -i /home/Ascent-openMVG/SfM_data/sfm_data.json -m /home/Ascent-openMVG/SfM_data/matches -o /home/Ascent-openMVG/SfM_data/sfm_results -s STELLAR -M /home/Ascent-openMVG/SfM_data/matches/matches.f.bin
openMVG_main_ComputeSfM_DataColor -i /home/Ascent-openMVG/SfM_data/sfm_results/sfm_data.bin -o /home/Ascent-openMVG/SfM_data/sfm_results/colorized.ply
openMVG_main_openMVG2openMVS -i /home/Ascent-openMVG/SfM_data/sfm_results/sfm_data.bin -o /home/Ascent-openMVG/SfM_data/mvs/scene.mvs