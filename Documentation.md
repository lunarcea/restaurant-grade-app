# Documentaiton
•	As I was developing this application, what manual steps did I take to ensure it was functioning properly? Can I automate those manual processes?
  Checking to make sure that zip code was entered correctly and if there were no results with certain features users were reprompted to give another selections.

•	Is it possible for the application to receive user inputs that are unexpected or invalid? How should the application handle various invalid inputs?
  Yes. Zip codes don’t meet five digits length or if invalid characters entered in any filters users reprompted to correct their errors.

•	How should the application's component functions perform given various inputs, whether valid or invalid?
  The functions should be optimized for error preventions to lower input errors and user dissatisfaction.

•	Are there any functions or sections of the code which aren't easy to read or understand? Is there a way to use examples to communicate what is supposed to happen?
  Detailed description and expressive variables enable to read easily and understand.

•	If the application processes data from the Internet: Is there a way to test the application's functionality without making any additional network requests? (see also: Stocks App testing notes and example tests)
  Yes. Create a dummy array with indexes with a length of nineteen and proper datatypes for each index’s index. Or do a single download of a local copy of json file as instructed on readme.md

•	If the application processes data from a CSV file or database: Is there a way to test the application's functionality without affecting the development environment datastore? (see also: Inventory Mgmt App example tests)
  Rather than directly modifying the target file you could create a separate variable to duplicate the contents of the data file and test functions on that variable without permanently changing the original data file. Then, use print function to check modifications/functions.
