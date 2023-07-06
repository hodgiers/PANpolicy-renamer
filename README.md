# PANpolicy-renamer
Ingests PAN config via api call and renames the policies according to requirements

Create a .env file in the directory this repo was cloned into.
The .env file should contain:
	PAN_API_KEY=<YOUR PAN API KEY>
	DEVICE_GROUP=<THE DG THAT THE POLCIES NEED TO BE RANAMED ON>
	FW_HOST=<HOSTNAME OR IP ADDRESS OF PANORAMA>

Build the dockerfile by running: 
docker build -t <The name you'd like to apply to the docker container> .
	Example:
	docker build -t policyrenamer .
Once it's done building run:
	docker run --rm -it -v $(pwd):/scripts policyrenamer
From within the docker container run:
	python3 grabandparse.py
