# currency-convertor
An API for converting currencies based on real-time exchange raates

## How to Start The API Server

### Docker
If you have docker and docker-compose installed, just run the following command:
```bash
cd server
docker-compose up --build
```
Or one may use the Dockerfile to build and run the container without using docker-compose.
### Local
If you'd wish to run the server locally for development purposes, just make sure you have given the __scripts/run_server.sh__ script execution privilages after checking the content of it :)
```bash
sudo chmod +x ./scripts/run_server.sh
```
Then, run it to fire up the API server:
```bash
./scripts/run_server.sh
```


## Decimal Place
In the examples of the instructions, the outputs all had the numbers up to 2 decimal places. However, this would lead to inaccurate results when converting from JPY. I set the decimal place for the outputs to 4 but it is configurable as an optional parameter of the API.