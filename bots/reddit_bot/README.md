# Reddit Reply Bot 🤖

### How it works:
This reply bot utilises praw to login to Reddit where it then scrapes 10 comments from [r/test](https://www.reddit.com/r/test/) looking for mentions of dogs, cats or both toghether. The bot then replies with a message including a link to an image of the mentioned animal.

The bot stores the replied to comments and stores them in a text file for refrence so double replies shouldn't occur.

---

### Setup:

The script should run out of the box with the exception of creating a "config.py" file setup like so:

```{python}
username = "ChuckNorris"
password = "SuperSecretPassword"
client_id = "XXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXX"
```
- **username**: Your reddit username
- **password**: Your reddit password
- **client_id & client_secret**: Can be obtained with the [Reddit API](https://www.reddit.com/prefs/apps), more details on how to use the Reddit API can be found in this [tutorial](https://www.youtube.com/watch?v=FdjVoOf9HN4&ab_channel=JamesBriggs)

---

### Languages & Tools:
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)



### Educational Content Used:
- [How-to Use The Reddit API in Python](https://www.youtube.com/watch?v=FdjVoOf9HN4&ab_channel=JamesBriggs)
- [How To Make A reddit Bot : P1,2,3](https://www.youtube.com/watch?v=krTUf7BpTc0&ab_channel=busterroni11)
