# PatchBot


PatchBot is a web scraper bot made in Python that sends updates through Discord on an hourly timer.It scrapes Steam's API for the games Marvel Rivals, Overwatch 2 and Guilty Gear Strive in order to find the titles for the most recent patch notes. Once PatchBot finds a new patch note it will store it in a JSON file and send the corresponding link for the game that the new patch note relates to. If PatchBot finds a patch note it already has it'll throw it away and go back to waiting so that Discord isn't spammed with messages every hour.


<img width="447" height="350" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/bdd268af-3d69-4e4f-8342-8dfc94786053" />
<img width="434" height="354" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/0615c1e8-7e88-4977-a4bd-57bb029a825c" />
<img width="459" height="357" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/cbd7286f-72b0-4f3a-a860-0f0fc9c5fa0d" />

## Requirements


PatchBot was made in Pycharm and all of the requirements will be in a seperate `.txt` file.

### Extra Info


PatchBot was made as a capstone project for my schooling and is my first solo coding adventure. PatchBot was made for a Discord server that I share with my friends so it most likely won't be compatable with others without some tweaking. I do not have anywhere to host the bot so it only runs when I have my computer on but I am planning to find some way to host it and continue updating it even once my schooling is complete.Below are some of my referances I used to help me learn how to make a web scraper and Discord bot.
- [How to make a Discord bot with Python by pixegami](https://www.youtube.com/watch?v=2k9x0s3awss)
- [Working with Json data in Python by Real Python](https://realpython.com/python-json)
- [Build a web scraper with Python by Real Python](https://realpython.com/beautiful-soup-web-scraper-python)
- [Discord developers docs](https://discord.com/developers/docs/intro)
