## Use start.sh to run the container and stop.sh to stop and unmount
### Use flags -w -p -n for start and -n for stop
## START
### -w is the workshop that will have its avg service time calculated (DEFAULT: 1)
### -p is the port on which the service will be exposed on the host (DEFAULT: 5000)
### -n is the name of the container you want to create, if omitted it will be random
## STOP
### -n is mandatory and stops and deletes the container with this name
#### Remember to chmod the scripts to be executable