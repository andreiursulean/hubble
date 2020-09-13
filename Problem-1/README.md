## Python parsing

Make a python program that parses the [Formula Student Germany page](https://www.formulastudent.de/academy/20200829-waymo/), gets all the teams and saves the information into a csv file.

You will need to parse [this page](https://www.formulastudent.de/academy/20200829-waymo/) and get all the teams from the table.

Each team has a homepage not available in the table, to be able to get that you will need to navigate to the specific team web page which is available as an anchor on their name.

After you get all this information, you need to save it in a CSV files.
The CSV will be named `teams.csv` and will contain all the information with the following format:
team_name, category, country, city, university, homepage

Ex: For team CURE we will have an entry that looks like this:
```
CURE,D,Germany,Mannheim,DHBW Mannheim,https://www.curemannheim.de/
```

You are encouraged to use any library. If you do so, please provide a way to simply install all your required dependencies. Providing a `requirements.txt` file would be a good idea.

Python Version: 3.x.x or above
CSV Format: team_name, category, country, city, university, homepage
Site: [https://www.formulastudent.de/academy/20200829-waymo/](https://www.formulastudent.de/academy/20200829-waymo/)
