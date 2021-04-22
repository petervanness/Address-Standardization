# Address-Standardization
Very brute force mechanism to create standardized formats of US address data

This was something I've had a need to do multiple times because addresses can be pretty screwy with a range of formats to mean the same thing. Mainly useful for duplicate checking as new addresses are added to a database. Very emergent nature -- new quirks likely to arise with each batch of data. There is nothing fancy about this, and some of the replace mechanisms vary, but it gets the job done. Some of the operations should be put into functions since they're applied to both address1 and address2, but that doesn't feel super valuable. 

Room for improvement would be converting numbered streets (e.g. 25th Street to Twenty-fifth or vice versa) to words; only includes crude way of doing that up to 10th Street.
