### problem statement ####

Many people find it hard to track their daily expenses as most bank applications are difficult, the user interface is cluttered, and data is manually recorded.

Common barriers includs

Barrier to Security: Local tracking spreadsheets are accessible to anyone.

Complex Onboarding: The use of financial services that require linking of actual bank accounts or going through multiple menus.

Data Loss: Fixes that temporarily resolve the problem without saving transaction history.

This application provides a light-weight, secure CLI ( command line interface ) that reduces friction through separate, persistent tracking environments per user and does not depend on any third party dependencies or require any connectivity to the Internet.

### scope of project ###

Local identity management with text-based user registration and rigorous check.

Session Persistence: Tracking state by using the physical streams of files for reading and writing database structures in the local machine.

Isolated Ledger System: Where every transaction is kept isolated and linked with the specific user ID.

Aggregate Reporting: Automatic ledger reports indicating total profits, total losses, and net balances.


### target users ###

students like myself who does not have a proper money tracking and cannot afford one

### best features ###

Authenticated access control: During the registration process, the system verifies that each username is unique. The passwords are checked on the basis of their length and number of digits. Moreover, login tries are limited to only 3.

Saving data automatically: The system generates automatic runtime files such as userfiles.txt and {username}_entryfiles.txt that record arrays, strings, and dictionaries in plain text using ||| as delimiter.

Formation of a Classified Ledger: Defined choice between Gain or Loss to categorize the money received or money paid, and security against negative figures or inappropriate currency types.

Net Balance Calculation in Real Time: Create text dashboards which display money in their exact formats ($0,000.00), arrows for the directions (+/-), and net balance equity totals.


### fatures wanted to add ###
wanted to add a encryption system in `{username}_entryfiles.txt` and `userfiles.txt` files but don't have the knowledge to add that.



###### thank you ######