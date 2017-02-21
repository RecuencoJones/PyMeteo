# PyMeteo

Simple Python example of retrieving and parsing XML data.

Uses a Flask server to expose endpoints from which to retrieve information.

## Requirements

- Python 2.7

## Installing 

```
pip install -r requirements.txt
```

## Running

```
python server.py
```

The server will start on `http://localhost:5000`.

## Endpoints

### Weather
- Path: `/api/weather/<id>`
- Parameters:
    - id: int
        An integer representing a municipality in Spain.
        A full list of municipities can be found in this [Excel file](http://www.ine.es/daco/daco42/codmun/codmun09/09codmun.xls).
- Returns: string
    - The name of the municipality of given id.
    - An error message if the municipality id is not valid.
- Examples:

```
> http://localhost:5000/api/weather/50297

Name: Zaragoza Municipality ID: 50297
```