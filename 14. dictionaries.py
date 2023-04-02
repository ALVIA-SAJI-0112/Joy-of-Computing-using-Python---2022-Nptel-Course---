//key - unique identifier for an item
//value - value 
//curly braces is used for dictionaries
conversion_factor={} //empty dictionary
conversion_factor['dollar']=60
conversion['euro']=80
print(conversion_factor)
conversion_factor['euro']  //to know the value corresponding to euro
conversion_factor.keys()   //to display all the keys
list(conv_facto.keys())    //to convert it into list
list(conv_facto.values())   //to list the values
conversion_factor.items()   //to list both values and keys simulatneously
//to list all the functianlities type - "conversion_factor" and press the tab key
conversion_factor.pop?      //to know what the pop functonality does
conversion_factor['dollar']=65
conversion_factorconversion_factor['yen']=50
del conversion_factor['yen'] //to delete
//euro_rs conversion
euro=30
e=30
r=e*conversion_factor['euro']
r