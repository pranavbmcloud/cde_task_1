# cde_task_1

## Workflow:
### Ingests the source file
### Cleans the data
### Creates a local clean copy
### Processes from the clean copy
### Flattens (if required)
### Writes to final file
  
## Usage
#### Please change the input_file variable in the main.py module to choose the file to process
  
## Tests
#### Project uses the Python unittest testing framework for the tests
#### Tests can be run using "python -m unittest" in the root
  
## Thoughts

### Data could Originate from multiple sources:
#### File from local file system
#### File from online url
#### API response
#### NoSQL tables


### There could be multiple cleaning requirements:
#### Malformed json, xml


### Data could be of multiple types:
#### Text files
#### Binaries
#### JSON
#### XML
#### YAML
#### sql

### There could be a need for multiple transformations:
#### JSON to XML



### Data might need to be sent to multiple destinations:
#### Local file system
#### Web endpoints
#### Exposed as a REST API
