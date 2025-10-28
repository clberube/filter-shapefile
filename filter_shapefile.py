#!/usr/bin/env python3
import geopandas as gpd
import argparse
import sys
from pathlib import Path

# List of columns to always keep
BASE_COLUMNS = [
    "OBJECTID",
    "NUMR_ECHN",
    "NUMR_FEUIL",
    "CODE_TYPE_",
    "DATE_ECHN",
    "FUS",
    "ESTN",
    "NORN",
    "CODE_PREC_",
    "NURM_PROJ_",
    "DATE_DERN_",
    "CODE_INDC_",
    "NUMR_INTER",
    "CODE_SYMBL",
]


def main():
    parser = argparse.ArgumentParser(
        description="Filter a shapefile to keep predefined columns and one user-specified geochemical element column."
    )
    parser.add_argument(
        "input_shp", type=Path, help="Path to the input shapefile (.shp)"
    )
    parser.add_argument(
        "element",
        type=str,
        help="Geochemical element column to keep (e.g., AG for silver)",
    )
    parser.add_argument(
        "output_shp", type=Path, help="Path to the output shapefile (.shp)"
    )
    args = parser.parse_args()

    # Load shapefile
    try:
        gdf = gpd.read_file(args.input_shp)
    except Exception as e:
        sys.exit(f"Error reading shapefile: {e}")

    # Normalize column names for matching
    existing_cols = list(gdf.columns)
    element_col = args.element  # .upper()

    # Check that the requested element exists
    if element_col not in existing_cols:
        sys.exit(
            f"Column '{element_col}' not found in shapefile. Available columns: {existing_cols}"
        )

    # Compute columns to keep
    keep_cols = [col for col in BASE_COLUMNS if col in existing_cols]
    keep_cols.append(element_col)

    # Filter dataframe
    gdf_filtered = gdf[keep_cols]

    # Export to new shapefile
    try:
        gdf_filtered.to_file(args.output_shp)
        print(f"Filtered shapefile saved to {args.output_shp}")
    except Exception as e:
        sys.exit(f"Error writing shapefile: {e}")


if __name__ == "__main__":
    main()
