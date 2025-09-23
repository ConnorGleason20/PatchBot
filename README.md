# PatchBot


PatchBot is a web scraper bot made in Python that sends updates through Discord on an hourly timer. It scrapes Steam's API for the games Marvel Rivals, Overwatch 2 and Guilty Gear Strive in order to find the titles for the most recent patch notes. Once PatchBot finds a new patch note it will store it in a JSON file and send the corresponding link for the game that the new patch note relates to. If PatchBot finds a patch note it already has it'll throw it away and go back to waiting so that Discord isn't spammed with messages every hour.


<img width="459" height="357" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/80375bed-3bb3-43df-a81d-fb79530923fb" />
<img width="434" height="354" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/9588f277-14ae-4eef-92bf-4ce16228a82e" />
<img width="447" height="350" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/2e648b06-b03c-4900-9518-bd0f0e5934e1" />




## Requirements


PatchBot was made in Pycharm and all of the requirements will be in a separate `.txt` file.

### How to Run PatchBot


I run the code through PyCharm and using my Discord Developer link to add it to my server. If you'd like to have this bot on your own server you'll have to go to the Discord Developer portal and make a new bot and get it's id then you'll have to make a `.env` file containing your bot id, server id, channel id and the links to Steam's api for any game you wish to get the patch notes for. For the Steam api link you'll use http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=''gameID''/&count=1&format=json and you can find the game id number by checking Steam's store page and once you click on the game you want to get notifications for the number is at the end of the URL.

#### Extra Info


PatchBot was made as a capstone project for my schooling and is my first solo coding adventure. PatchBot was made for a Discord server that I share with my friends so it most likely won't be compatable with others without some tweaking. I do not have anywhere to host the bot so it only runs when I have my computer on but I am planning to find some way to host it and continue updating it even once my schooling is complete.Below are some of my referances I used to help me learn how to make a web scraper and Discord bot.
- [How to make a Discord bot with Python by pixegami](https://www.youtube.com/watch?v=2k9x0s3awss)
- [Working with Json data in Python by Real Python](https://realpython.com/python-json)
- [Build a web scraper with Python by Real Python](https://realpython.com/beautiful-soup-web-scraper-python)
- [Discord developers docs](https://discord.com/developers/docs/intro)
