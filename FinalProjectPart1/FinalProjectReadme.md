FinalProjectInput is a program that take in user input for three files. Item information file, Item Price file, and Item Service Dates file

The program takes the information from these files and sorts them in various ways

The program outputs a file called Fullinventory.csv that outputs the information of each item by row. It orders each item by item ID number

The program outputs a file for each item type with the name of the item type followed by Inventory.csv. It orders items in each file by item ID number

The program outputs a file called PassedServiceDateInventory.csv for each item that as a passed due service date. It orders the itmes by service date from earliest to latest

The program outputs a file called DamagedInventory.csv for each item that is damaged. It orders each item by most expensive to least expensive

The program then gets input from the user for a manufacturer name and item type. The program searches for the item from the previous input files.
If the item is not passed its service due date an not damaged then the program returns the highest priced item with manufacturer and item type. Then the program searches for
an item of the same item type but with a different manufacurer name that has the closest price to the previous item. It returns this item if it is not passed its service due
date or damaged.
