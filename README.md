
# Chiper - FastAPI

This API was created within the recruitment process for Chiper.

## API Reference

#### Make the prediction

```http
  GET /prediction/{preddays}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `preddays` | `integer` | **Required**. The days you want to forecast |

To make the prediction you must put in the address bar of your browser the next url: http://127.0.0.1:8000/prediction/{preddays}; you must change the word "preddays" to the number of days you want to forecast.

After you press enter, the API will run the prediction model and show you the predictions as follows:

![App Screenshot]("https://i.ibb.co/1Gm1Sqs/Untitled.png")

## Installation

Clone the repo wherever you want:

```bash
  https://github.com/Fabioburgos/chiper_tech.git
```
## Virtual enviroment
In order to install all the dependencies, create a virtual enviroment as follow:

Install virtualenv into your local machine:

```bash
  pip install virtualenv
```
After that, you can create your virtualenv as follow:

```bash
  pip virtualenv ./
```
When you create your virtual enviroment, some folders and files are created inside of your project directory.

After you created the virtualenv, it need to be activated typing the route for the "Scripts" folder following by \activate. 
```bash
  D:\chiper_tech\chiper_tech>Scripts\activate
```
You will notice that the name of the virtual enviroments will appear at the beggining:
```bash
  (chiper_tech) D:\chiper_tech\chiper_tech>
```
## Dependencies
In order to get working the project, we need to install all the libraries or frameworks:
```bash
  pip install -r requirements.txt
```
Automatically all the libraries and frameworks will be downloaded and installed.
## FastAPI and Uvicorn
If you want to interact with the API, you need to create the webserver through Uvicorn following the syntax:
```bash
  uvicorn main:app --reload
```

## Screenshots

![App Screenshot](https://i.ibb.co/MsNDJSf/Untitled.png)

To access into the API, follow the url.

## API docs

FastAPI offer a strong tool to see the API documentation. To see it just add to the original url:
```bash
  /docs
```
## API predictions

The number of days to get the prediction can be set from the API docs.
![App Screenshot](https://i.ibb.co/qrrhHzR/Untitled.png)

Deploy the menu for the entrypoint and click on "Try it now", after that, type the value of "day" you want (forecast) and then click on "Execute".

If everything went well, you'll get a 200 code response with the prediction for the number of days you desired.
![App Screenshot](https://i.ibb.co/RHK6m0B/Untitled.png).



