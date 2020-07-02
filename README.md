# credicxo_internship_task

##URLs
1. /banks/get_branch_details/
  REQUEST METHOD : 
        - GET
    PARAMETERS REQUIRED : 
        - ifsc
    SUCCESS :
        - Details of the bank that has the same ifsc code is returned
    FAILURE :
        - nothing is sent in response only HTTP 404 is sent
2. /banks/get_branches_in_city/
  REQUEST METHOD : 
        - GET
    PARAMETERS REQUIRED : 
        - bank_name
        - city
    SUCCESS :
        - a list of banks with same name and same city
    FAILURE :
        - nothing is sent in response only HTTP 404 is sent
