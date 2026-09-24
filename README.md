# Personal Finance Ledger System

This is a command line program that is implemented using **Python**. It enables the user to create their account, login safely, and keep their record of money earned (income) and spent (expenses).

# guide for running it in local machine 

Through this guide, we will be able to set up and execute the finance ledger software on your local computer.

# requirments for running the code 

Before running the project, make sure you have the following installed:
**Runtime:** **Python 3.14.7** 
**Dependencies:** None (This project relies strictly on Python's built-in standard library).


# Setup & Installation

Follow these quick steps to set up your project environment:

## 1. Clone the Repository

Clone the repository on your local machine and navigate into the project directory:

## 2. File Verification

The app stores data persistently using local plain text files.

once you create a new user it will create a txt file in the same folder as the project named `userfiles.txt`

and once you add any finintial entry  it will create a txt filen in the same folder named      `{username}_entryfiles.txt`

# Running the Project

To get the system started, run the main Python file through your terminal:

# Application Rules & Features

**Password Security Requirements:** When registering a new user, passwords must be at least **10 characters long** and contain a minimum of **2 numbers**.

**Login Security:** Users are granted a maximum of **3 login attempts**. Exceeding this limit returns the user to the main menu.

**Persistent Dashboard:** Every unique user receives their own transaction ledger that reloads automatically upon logging back into the dashboard.


##### thanks you ######