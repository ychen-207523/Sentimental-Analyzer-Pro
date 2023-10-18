# SE Project 2

# C.E.L.T: The Sentimental Analyser 

### YouTube Link: 

[![Demo Video](https://i9.ytimg.com/vi_webp/zvme9ARshD8/mqdefault.webp?sqp=CJTzs_sF&rs=AOn4CLBkjs-_C1oPtVtZgfWL2llzZA_dKw)](https://youtu.be/VLoJCemCdHg)

---

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

## Contents
1. [Introduction](#intro)
2. [Steps for execution](#exec)
3. [Product Walkthrough](#usecases)
4. [Roadmap and Progress](#roadmap)
5. [Case Study](#casestudy)
6. [Contributing to the product](#contribute)
7. [Team Members](#team)

---
<a name="intro"></a>
## Introduction

Sentiment analysis is one of the fastest-growing research areas in computer science, making it challenging to keep track of all the activities in the area. In our project, we aim to achieve our goal of accurately predicting a user's sentiment by analyzing the data provided in any of the four different methods. They are Document Analysis, Text Analysis, Product Analysis, and Audio Analysis. This project though currently in the initial stages of development, can be further applied to numerous domains that can be useful for society. This document provides a major perspective for the users to understand and take up the project as an Open source software and add on multiple features before releasing it to the market. Also, the document aids the developers in understanding the code and acts as a reference point for starting the project.

The complete development was achieved using the following technologies and it is recommended that the next set of developers who take up this project have these technologies installed and keep them running before proceeding further:
- Python3
- Django
- HTML
- CSS
- Scrappy
- Vader Analysis Tool

Although we have used HTML and CSS for the FrontEnd, the users can merge the backend logic with any of the front end frameworks they wish to use such as React, angularJS, etc.

---

<a name="exec"></a>
## Steps for Execution
1. Clone this project into your system
```
git clone https://github.com/amit-99/SE_Project2.git
```
2. Make sure you are using Python 3.11 or higher
3. Intall dependencies for the project from root directory of the project:
    a. To install python library dependencies use requirements.txt 
    b. We also need install and import nltk and supporting libraries
```
cd <your_download_dir>\SE_Project2\
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
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
6. Run Django Server using manage.py (Note: Make sure you are in root directory of the project)
```
python .\sentimental_analysis\manage.py runserver
```
6. Next, open your browser and type in `localhost:8000` in the search bar to open the webUI of the application.5. The UI typically looks as shown below and here you have a choice between URL, file or normal text input.
7. Great!! Now you are into the application

---

<a name="usecases"></a>
![First](https://user-images.githubusercontent.com/43075652/97276268-31ce6100-17f4-11eb-8b57-7741069bf311.png)
![second](https://user-images.githubusercontent.com/43075652/97276507-82de5500-17f4-11eb-88e0-0ea41bc9b424.png)

The UI for URL input is as shown below:
![product](https://user-images.githubusercontent.com/43075652/97276542-925d9e00-17f4-11eb-910f-103be084ad13.png)

The UI for file input is as shown below:
![docum](https://user-images.githubusercontent.com/43075652/97277008-2891c400-17f5-11eb-901a-1ebd3da5a32b.png)

The UI for text input is as shown below:
![text](https://user-images.githubusercontent.com/43075652/97277038-33e4ef80-17f5-11eb-8fbc-76bad26adcc9.png)

The UI for audio input is as shown below:
![audio](https://user-images.githubusercontent.com/43075652/97277059-3d6e5780-17f5-11eb-8dcf-a5935d6613ae.png)

The Output as below:
![output](https://user-images.githubusercontent.com/43075652/97277225-74446d80-17f5-11eb-89f5-2b27c957827e.png)
![out](https://user-images.githubusercontent.com/43075652/97277310-8e7e4b80-17f5-11eb-8910-03ec42ea0ff7.png)

---
<a name="roadmap"></a>
## Roadmap and Progress
### Past Achievement(Previous Work)
- [x] Creating C.E.L.T. Django Project/Website
- [x] Sentiment Analysis Model's Algorithm addition
- [x] Text Analysis and Document Analysis Feature inclusion
- [x] Audio Analysis Feature inclusion
- [x] Amazon Product Analysis Feature addition
- [x] Case Study done for Amazon Product Review Sentiment Analysis 
- [x] Simple Documentation, Unit tests addition

### Current Achievements
☑️  Live Sentiment Analysis Feature inclusion<br>
☑️  News Analysis Feature inclusion<br>
☑️  UI Improvement for enriching User interaction with the Application<br>
☑️  Documentation Improvement for reflecting project's value accurately<br>
☑️  Addition of Builds and Workflows for better development activities<br>
☑️  Unit Tests were written and Test Coverage was improved<br>
☑️  Public facing webpage to get feedbacks, Raise and handle issues, Discuss & Grow with enthusiasts and supportive community<br>
☑️  <br>
☑️  <be>

### Future Scope
- [ ] Implement User Authentication to store the history of each User
- [ ] Recommendation System based on Product Analysis Results 
- [ ] Enhance the Product Analysis by considering the number of users rated for each Product!
- [ ] Extend the Sentiment Analysis to Facebook, Twitter, LinkedIn Posts
- [ ] To Be Added..

---  
<a name="casestudy"></a>
## Case Study: Amazon Product Review Sentiment and Text Analysis
We have done a Case Study for our Sentiment Analysis Project. It can be found [here](https://github.com/amit-99/SE_Project2/blob/develop/Case_Study.md).

---
<a name="contribute"></a>
## Eager to Contribute?
To Contribute to our application, please refer to [CONTRIBUTING.md](https://github.com/amit-99/SE_Project2/blob/develop/CONTRIBUTING.md)

---

## FUTURE SCOPE

Implement user authentication to store history for each user.

Recommendation system based on analysis results.

Live speech to text sentiment analysis.

Enhance the analysis by taking into consideration the number of users rated for each product!

Extend the analysis to the Facebook, Twitter and LinkedIn Posts

---
### Connect with us 
- Want to share you feedback or raise any issue
- Need instant help ? discuss over community chat to get help from other community members
- Join our mailing list for regular updates
- Or just want to be part of our journey and get to know more about the C.E.L.T and it's team

Visit our web page to be part of [C.E.L.T. community](https://factual-squash-083.notion.site/C-E-L-T-The-Sentiment-Analyzer-f771d9e92c494c9b85a4faeb6e3621a1?pvs=4)
---

<a name="team"></a>
## Team Members

- Akash Kore
- Amit Bhujbal
- Sohamkumar Patel
- Yogesh Hasabe
