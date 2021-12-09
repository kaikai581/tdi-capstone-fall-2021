# tdi-capstone-fall-2021
This repository is to set up a website for The Data Incubator's capstone project.

## Distribute with Panel
The first technology I tried was Streamlit. Later I found Streamlit did not support `ipywidgets`'s callback function.  
An alternative called `Panel` was recommended through googling, and I am moving to this technology.  
```
$ panel serve panel_app_no_sidebar.ipynb
```

## Deploy to Heroku
Before one can deploy to Heroku, (s)he needs a Heroku account and has to install Heroku. Please follow the [official document](https://devcenter.heroku.com/articles/getting-started-with-python) for all these.  

To deploy to Heroku, one has to  
1. Put your command you want to run in the `Procfile`. This repo provides an example.  
2. Put all dependency packages of your app in `requirements.txt`  
2. Issue the following commands.  
```
$ heroku create <your_project_name>
$ git push # push all changes to your project repo first
$ git push heroku HEAD:master
```
 In this project, my project name is `sklin-capstone`.  

After deployment, the app can be accessed with the following link.  
[https://sklin-capstone.herokuapp.com/panel_app_no_sidebar](https://sklin-capstone.herokuapp.com/panel_app_no_sidebar)

## Distribute with Streamlit
### Running the app locally
To run the app locally, issue the following command.
```
$ streamlit run streamlit_app.py
```

## Heroku Deployment
### References
1. [minimal-heroku-demo](https://github.com/holoviz-demos/minimal-heroku-demo)

### Troubleshooting
- Error message saying  
 ```remote:  !     No default language could be detected for this app.```  
 Have you pushed all changes to GitHub already?
