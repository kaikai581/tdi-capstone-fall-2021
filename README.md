# tdi-capstone-fall-2021
This repository is to set up a website for The Data Incubator's capstone project.

## Distribute with Panel
The first technology I tried was Streamlit. Later I found Streamlit did not support `ipywidgets`'s callback function.  
An alternative called `Panel` was recommended through googling, and I am moving to this technology.  
```
$ panel serve panel_app.ipynb
```

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
