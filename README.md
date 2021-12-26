# geo_mappeur

### Table of content

- [**Overview**](#overview)
- [**Usage**](#usage)
    - [Python script](#python-script)
    - [Windows executable](#windows-executable)
- [**References**](#references)
### Overview

This script gather online data from [IGN](#https://www.ign.fr/ "IGN website") maps to create an elevation map of a selected area. This script only works for areas in France.
A text file is written in `./data` containing the points of the elevation map. The x,y and altitude coordinates are given in meters. The formatting of the points in the text file is the one used by Grasshopper:`{x,y,z}`.

### Usage

This program can be run using a **python script** or a **compiled windows executable** that doesn't require a python installation.

The considered area is rectangular, selected from its top-left corner and its bottom-right corner. Latitude and longitude of both pionts are needed. I recommand using [Géoportail](#https://www.geoportail.gouv.fr/ "Géoportail website") to find these geographical coordinates.

![How to find coordinate on Géoportail](/img/README_1.png "How to find coordinate on Géoportail")
#### Python script

*Arguments*
```
    -a : top left corner of the rectangle <latitude longitude>
    -b : bottom riht corner of the rectangle <latitude longitude>

    -x_res : number of points on the x-axis of the elevation map (default 50)
    -y_res : number of points on the y-axis of the elevation map (default 50)

    -fn : name of the data file without extension (not necessary)
```

*Command*

Elevation map of Paris and its surrounding area.
100x100 data points saved at `paris_map.txt`

`python elevation_map.py -a 48.900000 2.235000 -b 48.800000 2.455000 -x_res 100 y_res 100 -fn paris_map`
#### Windows executable

*Arguments*
```
    -a : top left corner of the rectangle <latitude longitude>
    -b : bottom riht corner of the rectangle <latitude longitude>

    -x_res : number of points on the x-axis of the elevation map (default 50)
    -y_res : number of points on the y-axis of the elevation map (default 50)

    -fn : name of the data file without extension (not necessary)
```

*Command*

Elevation map of Paris and its surrounding area.
100x100 data points saved at `paris_map.txt`

Open `cmd` on Windows.
```
# 1) Save dist.rar from Github

# 2) Unzip archive dist.rar

# 3) Open cmd and change directory
cd \path\to\folder\dist\

# 4) Run executable
.\elevation_map.exe -a 48.900000 2.235000 -b 48.800000 2.455000 -x_res 100 y_res 100 -fn paris_map
```

### References

- IGN : [Website](#https://www.ign.fr/ "IGN website")
- UTM/GPS conversion : [Python package](https://github.com/Turbo87/utm)