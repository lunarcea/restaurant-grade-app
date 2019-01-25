# rating_app.py
This is an app for searching NYC restaurants with critical health violations.
Many would be surprised with restaurants high graded still have alarming health code violations.
You can search by name, grade, location(zip code) or cuisine category.

## Installation
To install, first, download the source code for this repo:
```shell
git clone git@github.com:lunarcea/restaurant-grade-app.git
cd my-freestyle-project
```

Once the file is downloaded and you enter the folder run the following:
```shell
pip3 install -r requirements.txt
```

Finally, download the NYC Department of Health restaurant violation data and move it to the downloaded repo folder:
```shell
https://data.cityofnewyork.us/api/views/gra9-xbjk/rows.json
```

## Usage

```shell
python3 ratings_app.py
```
