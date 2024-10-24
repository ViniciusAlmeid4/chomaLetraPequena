# FastAPI Image Processing Application
  This project was done in around 2 hours in a mock hackaton inside unicesumar's WorInTech event, we were challenged to build this app using python (a language I'm not used to) and docker to run the aplication.
This application combines two images, adds a title, and serves the result as a PNG through an API built with FastAPI.

  Other important point is that, due to the short time, we were encouraged to use chatGPT and make teams if we wanted. Since I've worked with chatGPT and have some abilities with prompt engineering I used it a lot.

  The organizers of the workshop were:

- Joao Choma: https://github.com/JoaoChoma
- Tainan Gomes: https://github.com/taigfs

## Prerequisites

- Docker
- Terminal access

# Commands to get the docker running

  These are the commands that were used to create and test the application in a windows machine.

## Building docker image
```
docker build -t fastapi-image-app .
```
## Running the build
```
docker run -p 8000:8000 fastapi-image-api
```
# Testing

  Feel free to test the app the way you want to, since there is an API built on it just remember to use the port 8000 and have the app running

## via basic powershell
```
$body = @{ 
    image1 = "https://tainanfideliscom.s3.sa-east-1.amazonaws.com/personal_tmp/image1.png" 
    image2 = "https://tainanfideliscom.s3.sa-east-1.amazonaws.com/personal_tmp/image2.png" 
    title = "ENSINE MELHOR COM IA" 
}

Invoke-RestMethod -Uri "http://localhost:8000/create_image/" -Method POST -Body ($body | ConvertTo-Json) -ContentType "application/json"
```
