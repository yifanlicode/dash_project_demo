
## Task

### Create a Dash app that does the following

1. Imports the CSV at the following URL.
	- https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-1000.csv
	- Columns of this CSV are as follows: Index, Organization Id, Name, Website, Country, Description, Founded, Industry, Number of employees
	- The CSV is a listing of companies/organizations and information about them.
2. Displays the information from the CSV as a Dash Table.
3. Displays the information from the CSV as a graph.
	- The graph should be an appropriate type for the data.
	- The graph must not be a Histogram.

## Solution

### Packages Used:

- pandas
- dash
- dash_core_components
- dash_html_components
- plotly.express


### For Mac/Linux:

#### 1.Setup the environment

##### 1.1. Create a virtual environment

```bash
python3 -m venv env
```
##### 1.2. Activate the virtual environment

```bash
source env/bin/activate
```

##### 1.3. Install the requirements

```bash
pip install -r requirements.txt
```

#### 2. Run the app

```bash
python app.py
```

#### 3. Open the app

Open the app in your browser at http://127.0.0.0:8050

#### 4. Deactivate the virtual environment

```bash
deactivate
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Yifan li
