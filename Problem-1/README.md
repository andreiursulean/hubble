## Python parsing

Code a Python3 program that parses data from an HTML page and saves it as a CSV file.

You will need to parse [this page](https://www.formulastudent.de/academy/20200829-waymo/) and get all the teams from the table.

Each team has a homepage that is not available in the table. To be able to get that you will need to navigate to the specific team web page which is available as an anchor on their name.

After you get all the information, you need to save it as a CSV file.
Name the file `teams.csv` and follow the format:

```
team_name,category,country,city,university,homepage
CURE,D,Germany,Mannheim,DHBW Mannheim,https://www.curemannheim.de/
...
```

You are encouraged to use any library. If you do so, please provide a way to simply install all your required dependencies. Providing a `requirements.txt` file would be a good idea.

Please use **Python version 3.6** or above to solve this problem.
