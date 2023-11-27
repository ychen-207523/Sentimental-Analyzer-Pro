# <img src="https://github.com/amit-99/SE_Project2/blob/develop/sentimental_analysis/realworld/static/images/logo-black-2.png" height="42" width="42"/>The Sentimental Analyser Pro
## Software Engineering Project for CSC 510

[![DOI](https://zenodo.org/badge/295188611.svg)](https://zenodo.org/badge/latestdoi/295188611)
[![GitHub Release](https://img.shields.io/github/release/amit-99/SE_Project2)](https://github.com/amit-99/SE_Project2/releases)
![Build](https://github.com/amit-99/SE_Project2/actions/workflows/main.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-v3.11+-brightgreen.svg)  
![GitHub contributors](https://img.shields.io/github/contributors/amit-99/SE_Project2)
![GitHub issues](https://img.shields.io/github/issues/amit-99/SE_Project2)
![GitHub closed issues](https://img.shields.io/github/issues-closed/amit-99/SE_Project2)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/amit-99/SE_Project2)](https://github.com/amit-99/SE_Project2)  
![GitHub language count](https://img.shields.io/github/languages/count/amit-99/SE_Project2)
![Lines of code](https://tokei.rs/b1/github/amit-99/SE_Project2)
[![GitHub-size](https://img.shields.io/github/languages/code-size/amit-99/SE_Project2)](https://github.com/amit-99/SE_Project2)
[![codecov](https://codecov.io/gh/lyonva/ClassMateBot/branch/master/graph/badge.svg)](https://app.codecov.io/gh/amit-99/SE_Project2)

---
The Sentimental Analyser Pro is a versatile tool that can perform sentiment analysis on different types of data, including text, audio, reviews, and news articles. Sentiment analysis is one of the fastest-growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project, we aim to achieve our goal of accurately predicting a user's sentiment by analyzing the data provided using different types of input data.

[![sentiment](https://github.com/amit-99/SE_Project2/blob/develop/sentimental_analysis/realworld/static/images/sentiment_3.png)](https://youtu.be/FMuVNTV_j8U)

---

## Table of Contents
1. [Introduction](#intro)
2. [Sentimental Analyser Pro Features](#feat)
3. [How to use  Sentimental Analyser Pro?](#exec)
4. [Roadmap and Progress](#roadmap)
5. [Case Study](#casestudy)
6. [Contributing to the product](#contribute)
7. [Connect with us](#Connectwithus)
8. [Team Members](#team)

---
<a name="intro"></a>
## Introduction

### What is Sentimental Analysis Pro?
Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotional tone in a piece of text, audio, or other forms of data. It involves identifying whether the sentiment expressed is positive, negative, or neutral.

### Why is it important?
<ul>
  <li>Sentiment analysis can help businesses and organizations understand how their customers or users feel about their products, services, or experiences. </li>
  <li>Companies can gauge public opinion about their products or services, track trends, and identify emerging issues or opportunities in the market.</li>
  <li>News agencies and media companies use sentiment analysis to analyze public sentiment towards news articles or events. This helps in generating content that aligns with the interests of the audience.</li>
  <li>Sentiment analysis is used in politics to understand public sentiment towards political candidates, parties, or policies. It is also used to gauge public opinion on social issues.</li>
</ul>

### Why use The Sentimental Analyser Pro?

The Sentimental Analyser provides the following:
<ul>
  <li><b>Comprehensive Insights: </b>Different types of data sources provide diverse perspectives. An all-encompassing tool can provide a more comprehensive understanding of public sentiment.</li>
  <li><b>Multichannel Data Analysis:</b> In today's world, opinions and sentiments are expressed across various channels, including social media, customer reviews, audio recordings, and news articles. A tool that can analyze these diverse data sources offers a more accurate picture of public sentiment.</li>
  <li><b>Cost-Efficiency:</b> Instead of using multiple specialized tools, a single tool that can handle multiple data types is cost-effective and streamlines the analysis process.</li>
</ul>

![meme](https://github.com/amit-99/SE_Project2/blob/develop/assets/images/meme.jpg?raw=true)

### How was Sentimental Analyser Pro developed?
The complete development was achieved using the following technologies:
- Python3
- Django
- HTML
- CSS
- Scrapy
- Vader Analysis Tool
- Tensorflow

Although HTML and CSS are used for the front end, the users can merge the backend logic with any of the front end frameworks they wish to use such as React, and AngularJS.

---

<a name="feat"></a>
## What can Sentimental Analyser Pro do?
|Feature|Description  |
|--|--|
|Product Analysis |```Sentimental analysis of Amazon product reviews```|
|News Analysis  |```Sentimental analysis of any recent news topic```|
|Text Analysis | ```Sentimental analysis of text input```|
|Audio Analysis   |``` Sentimental analysis of audio file``` |
|File Analysis   |``` Sentimental analysis of text file``` |
|Live Sentimental Analysis   |``` Sentimental analysis of live recorded audio``` |
|Facebook Post Analysis   |``` Sentimental analysis of Facebook Post``` |
|Twitter Post Analysis   |``` Sentimental analysis of Twitter Post``` |
---

<a name="exec"></a>
## How to use Sentimental Analyser Pro?
### Installation
1. Clone this project:
```
git clone https://github.com/NehaSJ99/Sentimental-Analyzer-Pro.git
```
2. Make sure you are using Python 3.11 or higher. You can get it here: https://www.python.org/downloads/release/python-3115/
3. Install dependencies for the project from the root directory of the project:
```
cd <your_download_dir>\SE_Project2\
pip install -r requirements.txt
```
4. Install ffmpeg:  
For Windows:  
```
winget install ffmpeg
```  
For Linux (Ubuntu):  
```
sudo apt install ffmpeg
```  
For Mac:  
```
brew install ffmpeg
```   
5. Run Django Server using manage.py (Note: Make sure you are in root directory of the project.)
```
cd <your_download_dir>\SE_Project2\
python .\sentimental_analysis\manage.py runserver
```
6. Next, open your browser and type in `localhost:8000` in the search bar to open the user interface of the application.

### Usage

<a name="usecases"></a>
- Start the django server to get to the homepage
![First](https://github.com/amit-99/SE_Project2/blob/develop/assets/gifs/1.gif)

- Amazon Product sentiment Analysis
![second](https://github.com/amit-99/SE_Project2/blob/develop/assets/gifs/3.gif)

- News Sentiment Analysis
![third](https://github.com/amit-99/SE_Project2/blob/develop/assets/gifs/2.gif)

---
<a name="roadmap"></a>
## Roadmap and Progress
### Past Achievement(Previous Work)
- [x] Live Sentiment Analysis Feature inclusion
- [x] News Analysis Feature inclusion
- [x] Fixed and enhanced Amazon Product Analysis
- [x] Unit Tests were written and Test Coverage was improved

### Current Achievements
☑️  Facebook post Analysis using Deep Learning Feature inclusion<br>
☑️  Twitter post Feature inclusion<br>
☑️  Text analysis for Spanish language inclusion<br>
☑️  Image analysis Feature inclusion<br>
☑️  UI Improvement for enriching User interaction with the Application<br>
☑️  Documentation Improvement for reflecting project's value accurately<br>
☑️  Addition of Builds and Workflows for better development activities<br>
☑️  Public facing webpage to get feedbacks, Raise and handle issues, Discuss & Grow with enthusiasts and supportive community<br>  

### Future Scope
- [ ] Implement User Authentication to store the history of each User
- [ ] Recommendation System based on Product Analysis Results 
- [ ] Enhance the Product Analysis by considering the number of users rated for each Product!
      
---  
<a name="casestudy"></a>
## Case Study: Amazon Product Review Sentiment and Text Analysis
We have done a Case Study for our Sentiment Analysis Project. It can be found [here](https://github.com/NehaSJ99/Sentimental-Analyzer-Pro/blob/master/Case_Study.md).

---
<a name="contribute"></a>
## Eager to Contribute?
To Contribute to our application, please refer to [CONTRIBUTING.md](https://github.com/NehaSJ99/Sentimental-Analyzer-Pro/blob/master/CONTRIBUTING.md)

---
<a name="Connectwithus"></a>
## Connect with us 
- Want to share your feedback or raise any issue [click here](https://noteforms.com/forms/sentiment-analyser-pro-uo8m1e)
- Need instant help? discuss over community chat to get help from other community members
- Join our mailing list for regular updates
- Join our discord forum for updates or support or discussions. [Join Here!](https://discord.gg/xYkUnvdzP9)
- Or just want to be part of our journey and get to know more about the Sentiment Analyser Pro and its team

**Visit our web page to be part of [Sentiment Analyser Pro community](https://sustaining-river-90d.notion.site/Sentiment-Analyzer-Pro-df3c7c6680974d08bbb80ccff21a1ebb)**

---

<a name="team"></a>
## Team Members

- Neha Jagtap
- Pranjali Jadhav
- Swaranjali Jadhav
- Shardul Khandekar
