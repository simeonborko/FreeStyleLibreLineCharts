# FreeStyle Libre -- Line Charts

"FreeStyle Libre -- Line Charts" visualize your glucose data from FreeStyle Libre scanner. It is implemented as Python server using Plotly.

This tool uses only Historic glucose and Scan glucose data records. In plots, there are blue lines with points for Historic glucose and orange points for Scan glucose.

Here you can see a screenshot:

![Screenshot](https://github.com/simeonborko/FreeStyleLibreLineCharts/blob/master/screenshot.png)

### Run syntax
```
python3 server.py <file> [<port>]
```

### How to use it

1. Install Python 3
2. Download or pull this repository
3. Open terminal and change directory to the project folder
4. Install requirements by running: ```pip3 install -r requirements.txt```
5. Export data from official FreeStyle Libre Software (File -> Export Data), let's say to file `data.txt`
6. Run server by: ```python3 server.py <FILE>```, where `<FILE>` is the path for your data file (previous point)
7. Open `http://localhost:8000/` in your web browser
8. Select date you are interested in
9. Enjoy and learn from plot ;)
10. Terminate server by Ctrl+C or by closing your terminal

### Disclaimer

You can use this tool without warranty, on your own risk. This tool is given as-is.

### Contact

In case you have any problem with this tool or have any idea how to improve it, please create new issue or contact me directly by email: simeon.borko@gmail.com
