# Currency Convertor
An API and a CLI for converting currencies based on real-time exchange rates.
The exchange rates are fetched from the [exchangerate.host](https://exchangerate.host) which uses the European Central Bank data.

## How to Start The API Server
Please make sure that the 7575 port on your machine is available. If it is not available, set the environment variable _CONVERTOR_PORT_ as desired either within the docker-compose file or in your operating system if you'd wish to run locally.
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
cd server
sudo chmod +x ./scripts/run_server.sh
```
Then, run it to fire up the API server:
```bash
./scripts/run_server.sh
```

## API Documentations

After the server is fired up, one may access the Swagger documentation by heading to [http://localhost:7575/docs](http://localhost:7575/docs).
From there one can see the schemas for Request and Response, validation policies, and Error schemas. One may also try the API with arbitrary input parameters from the documentation thanks to FastAPI.

## API Server Tests

The server does not need to be up and running to run the tests.
In order to run the tests, first we need to activate the virtual environment (run the server locally once to make sure the virtual environment is created). Then, run the pytest module:
```bash
source ./env/bin/activate
(env) cd src/server
(env) python -m pytest ./tests
```

## How to run the CLI

Please make sure that the _CONVERTOR_PORT_ environment variable is set correctly to the port number of running API server. If you have not changed the port when running the server, it should work by default.
Give execution access to the __cli/scripts/prepare_cli.sh__ so that the virtual environment is created. Then, head to the __src/cli__ directory and run the CLI from there:

```bash
cd cli
sudo chmod +x ./scripts/prepare_cli.sh
./scripts/prepare_cli.sh
cd src/cli
./convertor.py --help
```

## CLI Tests
Please make sure that the API server is up and running. Then, From the __src/cli__ directory run the following commands to run the tests:

```bash
deactivate
source ../../env/bin/activate
(env) python -m pytest ./tests
```

## Decimal Place
In the examples of the instructions, the outputs all had the numbers up to 2 decimal places. However, this would lead to inaccurate results when converting from JPY. I set the decimal place for the outputs to 4 but it is configurable as an optional parameter of the API.

## Open Discussion

- __Will it work with a 2TB input file as well?__
Yes. Since the _readline()_ function loads only a single line to the RAM at once, it is possible to give a gigantic file as input. However, it would take a very long time since the process is executed sequencially. The data processing of each line (record) is independant from the others. As a result, We can use multiprocessing/async techniques to get reasonable results from gigantic inputs.

- __What would happen if the input file has one malformed JSON line towards the
end of the file?__
This is included in the test functions of CLI. I had the reasoning that other lines (records) should have the expected behaviour regardless of malformed JSON lines in the input file. Right now, the root cause of the malformed JSON line would be printed out to the stdout at the respective line.

- __Assume your API should degrade gracefully / still be available in case the
upstream exchange rate service is down. How would you handle this?__
This is handled already to some degree by using in-memory cache for one hour. However, this is only a solution to demonstrate the idea and speed up the API server. If we want to have multiple instances of the API, they should share the same cache and in-memory cache would not be suitable. I would use redis instead. Also, to completely address this problem even if the upstream is down more than the cache TTL, I would suggest keeping a "last seen rate" for each of the rates in redis.

