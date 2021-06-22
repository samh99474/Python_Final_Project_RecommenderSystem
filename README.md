# :clapper:Python Final Project - Movie Recommender System 電影推薦系統 #

# :heart: YouTube - Project Presentation and Demo
Presentation and demo by 謝尚泓 Shang-Hong Xie and 陳良葳 Jeff.
> 🔗 https://www.youtube.com/watch?v=aSEBuPXpsd4

## :dart: Introduction ##
<br />Recommendation systems are becoming increasingly important in today’s extremely busy world.
<br />The purpose of a recommendation system basically is to search for content that would be interesting to an individual. 
<br />Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. 
<br />Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual.

<br />We build a movie recommender system in python, and then our recommender system consists of the basic 3 methods.
<br />1. Content-Based Filtering
<br />2. Collaborative Filtering
<br />3. Hybrid
<br />The movie dataset is from Kaggle, and we convert the original CSV file to DB file so that we can process the data in SQLite
<br />
<br />Kaggle - The Movies Dataset:
> 🔗 https://www.kaggle.com/rounakbanik/the-movies-dataset

<br />As for GUI, we use PyQt6 to show the Socket Client interface(DB and RS is in Socket Server).
<br />Therefore User (client) can send a command to the server to request Movie information, user information, recommendation output list, and so on.
<br /><img src="./readme_Image/GUI_HomePage.jpg"/>
<br /><img src="./readme_Image/GUI_VideoPage.jpg"/>

## :dart: System Architecture ##
<img src="./readme_Image/SystemArchitecture.png"/>

## :dart: Recommender System ##
<img src="./readme_Image/RecommenderSystem-1.png"/>
<img src="./readme_Image/RecommenderSystem-2.PNG"/>
<img src="./readme_Image/RecommenderSystem-3.PNG"/>
<img src="./readme_Image/RecommenderSystem-4.PNG"/>
<img src="./readme_Image/RecommenderSystem-5.PNG"/>
