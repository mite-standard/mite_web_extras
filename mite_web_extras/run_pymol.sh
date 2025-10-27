#!/bin/bash

mkdir -p /data/img

for pdb in data/pdb/*.pdb; do
  filename=$(basename -- "$pdb");
  filename=${filename%.pdb}
  output_path="/data/img/$filename.png"

  if [ -f "$output_path" ]; then
    echo "Skipping $filename (image already exists)"
    continue
  fi

  echo "Generating image for $filename"
  pymol -c "$pdb" -d "bg_color white; hide everything; show cartoon; spectrum count, red blue; set opaque_background, 0; png $output_path, 0, 0, -1, ray=1; quit;";
  done