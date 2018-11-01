# IBM Cloud Private for Data (ICP4D) - Ecosystem participation samples
The intent of this repository is to provide sample applications demonstrating how customers/partners can leverage ICP for Data API interface to participate in the ICP4D platform ecosystem. 

## ICP4D - API Tags/Resources
There are three high level tags in the ICP4D API's, this includes
* Governance
* Machine Learning
* Platform Capabilities

##### Note: The initial version of the ICP4D is going to be a limited subset of APIs to enable platform participation. We may deprecate some functions and add new resources/functions going forward that would require some migration effort. We will provide guidance on the migration to future versions of the API. 


## Sample applications
### Sharing metadata with the enterprise governance catalog
Python based Map Reduce application that does a simple filtering and aggregation of data to demonstrate that you can share metadata about the application with the ICP4D platform. 


### Governed Data Science
Jupyter notebook based interface where we share metadata about the individual steps in the notebook with the governance catalog. We will also demonstrate how we are able to both create new machine learning models and also use existing existing storing end points. 

### Data lifecycle management
Simple Node-Red application to demonstrate the ability to read the existing governance policies and rules from the governance catalog and perform custom actions to manage the data lifecycle. 
