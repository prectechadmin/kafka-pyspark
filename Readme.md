Simple pySpark Data Pipeline
This project build 3 docker containers to demostrate writing
data from a python kafka producer to kafka for consumtion by a pyspark application

### To run it
 ```bash
docker-compose build
docker-compose up
```
You should see the message sent from the Producer container in the console of
the consuming pyspark container.

All done. Thank you.
