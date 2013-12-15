Demo data script for FreshBooks
====================

####This script creates some demo data needed when developing with FreshBooks api

##Requirements

```
refreshbooks==1.7.2
fake-factory==0.3.2
```


##Configuration

This script works with the older version of API, without oAUth.
You will need to get your FreshBooks username and the "Authentication Token" from your FreshBooks account -> FreshBooks API page.

Edit the globals section, and change the values to your own.
In the globals, you can also set the number of invoices and clients you want to create.

##Usage

```
pip install -r requirements.txt
python create_demo_data.py
```


## Notes
 - The Refreshbooks library changes the lxml.objectify behavior, so if you plan to use it in your code, be aware


