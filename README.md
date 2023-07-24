# PANpolicy-renamer
Ingests PAN config via api call and renames the policies according to requirements

# Create a .env file
```
It should be created within the directory this repo was cloned into.
The .env file should contain:
<<<<<<< HEAD
	```
	'PAN_API_KEY=<YOUR PAN API KEY>'
	'DEVICE_GROUP=<THE DG THAT THE POLCIES NEED TO BE RANAMED ON>'
	'FW_HOST=<HOSTNAME OR IP ADDRESS OF PANORAMA>'
	```
=======

	PAN_API_KEY=<YOUR PAN API KEY>
	DEVICE_GROUP=<THE DG THAT THE POLICIES NEED TO BE RENAMED ON>
	FW_HOST=<HOSTNAME OR IP ADDRESS OF PANORAMA>

```
## Build the dockerfile by running: 
```
docker build -t <The name youd like to apply to the docker container> .
	Example:
	docker build -t policyrenamer .

Once it's done building run:
	docker run --rm -it -v $(pwd):/scripts policyrenamer

You should now be inside of the docker container.

From within the docker container run:
	python3 grabandparse.py 
```
