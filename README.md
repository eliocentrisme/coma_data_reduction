# Coma cluster Data

These folders contain VLA observations of the Coma cluster in L- and P-band, across several configurations.

## Folder Structure

- `coma-pband/barray/MM.DD/`: P-band observations in B-array taken on the given date.
- `coma-pband/carray/MM.DD/`: Same, but for C-array.
- `coma-lband/carray/MM.DD/`: Same, but for L-band in C-array.
    - `coma-lband/carray/03.09/`: Contains elio-corrected and VLA-corrected.
- `coma-lband/darray/MM.DD/`: Same, but for L-band in D-array.

### Commands to download the data
##### P-Band B-array 2020-07-04: pbandB1
Uncalibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2014047215/32ltesbc3ma1ofdum7bkianq5m/20A-198.sb37594223.eb38435025.59034.208921261576/`

##### P-Band B-array 2020-07-05: pbandB2
Uncalibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2013917575/gi4a45auhpnts145kf8hauqpqi/20A-198.sb37594223.eb38436624.59035.19188032407/`

##### P-Band C-array 2020-02-18: pbandC1
Uncalibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2008763404/etpcrrbfr40uaspco2l5gp4pnb/20A-198.sb37901689.eb37922752.58897.22256230324/`

##### P-Band C-array 2020-03-26: pbandC2
Uncalibrated: 

##### L-Band C-array 2020-03-09: lbandC1
Calibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/1991575193/e70f4c25ca4f766404b4c924d7c054ae/`

Uncalibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/1979970869/su5fdqtr1jbnmajhlkp48a5em8/20A-198.sb37594219.eb37963764.58917.21076973379/`

##### L-Band C-array 2020-02-25: lbandC2
Calibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2006577175/514ed1b296a99e9e800df38c506100dd/`

##### L-Band D-array 2021-03-30: lbandD1
Calibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2006581838/8c4e28ce738907fdb563d64c9a275f61/`

##### L-Band D-array 2021-04-15: lbandD2
Calibrated: `wget -r -l 10 --reject "index.html*" -np -nH --cut-dirs=3 https://dl-dsoc.nrao.edu/anonymous/2006585114/80e0489b34b1e7c88c6a9a677d3e99c4/`

## Notes

- All data are in Measurement Set (MS) format.
- L-band data are calibrated by the NRAO pipeline.

