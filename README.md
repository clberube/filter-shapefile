# Filter Shapefile CLI

A simple command-line interface (CLI) to filter a shapefile based on a predefined list of columns and one user-specified geochemical element column.  
This tool is useful for standardizing geochemical or geological shapefiles before further analysis.

---

## Features

- Imports a shapefile using **GeoPandas**
- Keeps only a fixed set of columns (e.g., `OBJECTID`, `NUMR_ECHN`, `DATE_ECHN`, etc.)
- Preserves one additional column specified by the user (e.g., `AG` for silver)
- Exports the filtered shapefile to a new file

---

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/filter-shapefile-cli.git
cd filter-shapefile-cli
pip install -r requirements.txt
```

---

## Usage

```bash
python filter_shapefile.py <input_shapefile> <element> <output_shapefile>
```

### Example

```bash
python filter_shapefile.py data/Geochem_points.shp AG output/Geochem_AG_filtered.shp
```

**Explanation:**
- `data/Geochem_points.shp` → path to the input shapefile  
- `AG` → geochemical element column to keep  
- `output/Geochem_AG_filtered.shp` → output shapefile path  

---

## 📋 Columns Kept

The script preserves the following columns by default:

```
OBJECTID
NUMR_ECHN
NUMR_FEUIL
CODE_TYPE_
DATE_ECHN
FUS
ESTN
NORN
CODE_PREC_
NURM_PROJ_
DATE_DERN_
CODE_INDC_
NUMR_INTER
CODE_SYMBL
```

Plus one additional column corresponding to the selected geochemical element.

---

## Example Output

When run successfully, you’ll see:

```
Filtered shapefile saved to output/Geochem_AG_filtered.shp
```

---

## Dependencies

- [geopandas](https://geopandas.org/)

Install them with:

```bash
conda install geopandas
```

or 

```bash
pip install geopandas
```

---

## License

This project is released under the [MIT License](LICENSE).

---

## 👤 Author

**Charles L. Bérubé**  
Department of civil, geological & mining engineering  
Polytechnique Montréal  
