# PrBoom HTTP

PrBoom modified to read demos over HTTP.

## Usage
Start `doom_http`:
```
cd doom_http
pip install -r requirements.txt
python3 main.py
```

Build PRBoom:
```
mkdir build
cmake ../
make -j8
```

Run PRBoom:
```
./prboom-plus -iwad Doom1.WAD -playdemo ../http_doom/dummy.lmp -levelstat
```
