import pandas as pd
#---------------------set file--------------------------------------
# Default test file
file = 'https://raw.githubusercontent.com/mthwtkr/CSV-without-db/master/us-500.csv'
df = pd.read_csv(file, delimiter = ",", header=0, index_col=None)

#--------------------Set Address Parameters--------------------
#for now, add space to end so that street portion can be positively identified
# print(df.columns)
df['std_address1'] = ' '+df['Address']+' '
df['std_address2'] = ' '+df['County']+' '  #Just using county as a placeholder for now
df['std_city'] = ' '+df['City']+' '

#Capitalize everything
df['std_address1'] = df['std_address1'].str.upper()
df['std_address2'] = df['std_address2'].str.upper()
df['std_city'] = df['std_city'].str.upper()

#-----------City Section----------------------------------------
df['std_city'].replace({' TOWNSHI': ' TOWNSHIP '}, inplace=True, regex=True)
df['std_city'].replace({' TWP.': ' TOWNSHIP '}, inplace=True, regex=True)
df['std_city'].replace({' TWP': ' TOWNSHIP '}, inplace=True, regex=True)
df['std_city'].replace({' ST.': ' SAINT '}, inplace=True, regex=True)
df['std_city'].replace({' ST ': ' SAINT '}, inplace=True, regex=True)
df['std_city'].replace({' FT.': ' FORT '}, inplace=True, regex=True)
df['std_city'].replace({' FT ': ' FORT '}, inplace=True, regex=True)
df['std_city'].replace({' MT.': ' MOUNT '}, inplace=True, regex=True)
df['std_city'].replace({' MT ': ' MOUNT '}, inplace=True, regex=True)

df['std_city'].replace({"'": ''}, inplace=True, regex=True)
df['std_city'].replace({"`": ''}, inplace=True, regex=True)


#------------Address Section---------------------------------------
df['std_address1'].replace({' I-': ' INTERSTATE '}, inplace=True, regex=True)

#US Highway stuff -- preferable in my case to nix altogether, but easy to standardize to desired version
df['std_address1'].replace({'U.S.': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' U. S. ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({'U.S ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' U. S ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' US. ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' U S. ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' US ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({' U S ': ' '}, inplace=True, regex=True)

#Remove Address Punctuation
df['std_address1'] = df['std_address1'].str.replace(",", ' ')
df['std_address1'] = df['std_address1'].str.replace(".", ' ')
df['std_address1'] = df['std_address1'].str.replace("-", ' ')
df['std_address1'] = df['std_address1'].str.replace(";", ' ')

df['std_address1'].replace({"'": ''}, inplace=True, regex=True)
df['std_address1'].replace({'`': ''}, inplace=True, regex=True)

df['std_address2'] = df['std_address2'].str.replace(",", ' ')
df['std_address2'] = df['std_address2'].str.replace(".", ' ')
df['std_address2'] = df['std_address2'].str.replace("-", ' ')
df['std_address2'] = df['std_address2'].str.replace(";", ' ')

df['std_address2'].replace({"'": ''}, inplace=True, regex=True)
df['std_address2'].replace({'`': ''}, inplace=True, regex=True)

#Suite/Unit Adjustments
df['std_address1'].replace({' STE ': ' SUITE '}, inplace=True, regex=True)
df['std_address1'].replace({' NUMBER ': ' SUITE '}, inplace=True, regex=True)
df['std_address1'].replace({' NUM ': ' SUITE '}, inplace=True, regex=True)
df['std_address1'].replace({' UNIT ': ' SUITE '}, inplace=True, regex=True)
df['std_address1'].replace({'#': ' SUITE '}, inplace=True, regex=True)

df['std_address2'].replace({' STE ': ' SUITE '}, inplace=True, regex=True)
df['std_address2'].replace({' NUMBER ': ' SUITE '}, inplace=True, regex=True)
df['std_address2'].replace({' NUM ': ' SUITE '}, inplace=True, regex=True)
df['std_address2'].replace({' UNIT ': ' SUITE '}, inplace=True, regex=True)
df['std_address2'].replace({'#': ' SUITE '}, inplace=True, regex=True)

#Ensuring long format of road
#the ones that need to be isolated to know that they're road portion
df['std_address1'].replace({' AVE ': ' AVENUE '}, inplace=True, regex=True)
df['std_address1'].replace({' CIR ': ' CIRCLE '}, inplace=True, regex=True)
df['std_address1'].replace({' CT ': ' COURT '}, inplace=True, regex=True)
df['std_address1'].replace({' CTR ': ' CENTER '}, inplace=True, regex=True)
df['std_address1'].replace({' DR ': ' DRIVE '}, inplace=True, regex=True)
df['std_address1'].replace({' MT ': ' MOUNT '}, inplace=True, regex=True)
df['std_address1'].replace({' PL ': ' PLACE '}, inplace=True, regex=True)
df['std_address1'].replace({' ST ': ' STREET '}, inplace=True, regex=True)
df['std_address1'].replace({' STR ': ' STREET '}, inplace=True, regex=True)
df['std_address1'].replace({' WY ': ' WAY '}, inplace=True, regex=True)
df['std_address1'].replace({' RT ': ' ROUTE '}, inplace=True, regex=True)
df['std_address1'].replace({' SR ': ' STATE ROUTE '}, inplace=True, regex=True)
df['std_address1'].replace({' SQ ': ' SQUARE '}, inplace=True, regex=True)

#The ones that can be situated any way
df['std_address1'].replace({'BLDG': ' BUILDING '}, inplace=True, regex=True)
df['std_address1'].replace({'BLDING': ' BUILDING '}, inplace=True, regex=True)
df['std_address1'].replace({'BLDNG': ' BUILDING '}, inplace=True, regex=True)
df['std_address1'].replace({'BLVD': ' BOULEVARD '}, inplace=True, regex=True)
df['std_address1'].replace({'CENTRE': ' CENTER '}, inplace=True, regex=True)
df['std_address1'].replace({'FRWY': ' FREEWAY '}, inplace=True, regex=True)
df['std_address1'].replace({'GTWY': ' GATEWAY '}, inplace=True, regex=True)
df['std_address1'].replace({'HWY': ' HIGHWAY '}, inplace=True, regex=True)
df['std_address1'].replace({'PKWY': ' PARKWAY '}, inplace=True, regex=True)
df['std_address1'].replace({'PLZ': ' PLAZA '}, inplace=True, regex=True)
df['std_address1'].replace({'TNPK': ' TURNPIKE '}, inplace=True, regex=True)
df['std_address1'].replace({'TPK': ' TURNPIKE '}, inplace=True, regex=True)
df['std_address1'].replace({'TPKE': ' TURNPIKE '}, inplace=True, regex=True)
df['std_address1'].replace({'TRNPK': ' TURNPIKE '}, inplace=True, regex=True)

#the ones that need some space
df['std_address1'].replace({' CV': ' COVE '}, inplace=True, regex=True)
df['std_address1'].replace({' LN': ' LAVE '}, inplace=True, regex=True)
df['std_address1'].replace({' PK': ' PIKE '}, inplace=True, regex=True)
df['std_address1'].replace({' RD': ' ROAD '}, inplace=True, regex=True)
df['std_address1'].replace({' TRL': ' TRAIL '}, inplace=True, regex=True)

#Numbered roads, up to a point; should be easy enough to find mechanism to do this for all numbered roads
df['std_address1'].replace({' 1ST': ' FIRST '}, inplace=True, regex=True)
df['std_address1'].replace({' 2ND': ' SECOND '}, inplace=True, regex=True)
df['std_address1'].replace({' 3RD': ' THIRD '}, inplace=True, regex=True)
df['std_address1'].replace({' 4TH': ' FOURTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 5TH': ' FIFTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 6TH': ' SIXTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 7TH': ' SEVENTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 8TH': ' EIGHTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 9TH': ' NINTH '}, inplace=True, regex=True)
df['std_address1'].replace({' 10TH': ' TENTH '}, inplace=True, regex=True)

#Replace double space w single space -- run twice to catch 3+ spaces
df['std_city'].replace({'  ': ' '}, inplace=True, regex=True)
df['std_city'].replace({'  ': ' '}, inplace=True, regex=True)

df['std_address1'].replace({'  ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({'  ': ' '}, inplace=True, regex=True)

df['std_address2'].replace({'  ': ' '}, inplace=True, regex=True)
df['std_address2'].replace({'  ': ' '}, inplace=True, regex=True)

#Create function to fix saints ('St. ____') that got changes to 'STREET'
def saints(saint):
    for i, row in df.iterrows():
        df.loc[i,'std_address1']=df.loc[i,'std_address1'].replace(' STREET '+saint,' SAINT '+saint)

# Make list of potential saints names
saint_list = ['AGNES', 'ALBAN', 'ALBANS', 'ANDREW', 'ANTHONY', 'AUGUSTINE', 'BENEDICT', 'BENEDICTS', 'CATHERINE',
'CECEILIA', 'CHARLES', 'CLAUDE', 'CLAUDES', 'CLAUDIA', 'DOMINIC', 'DOMINICS', 'ELIZABETH', 'ELIZABETHS','FERNANDO',
'FRANCES', 'FRANCIS', 'GEORGE', 'GEORGES', 'IGNACE', 'JAMES', 'JOHN', 'JOHNS', 'JOSEPH', 'JOSEPHS', 'JUDE',
'LOUIS', 'LUCY', 'LUKE', 'MARIA', 'MARK', 'MARKS', 'MARTHA', 'MARTIN', 'MARTINS', 'MARY', 'MARYS', 'MATTHEW',
'MATTHEWS', 'MAXMILLIAN', 'MICHAEL', 'PATRICK', 'PAUL', 'PAULS', 'PETER', 'PETERSBURG', 'PHILIP', 'PHILLIP',
'ROSE', 'TERESA', 'THERESA', 'THOMAS', 'VALENTINE']

# loop through list of saints names and run function for each one
for saint in saint_list:
    saints(saint)

#Direction Adjustments
df['std_address1'].replace({' N E ': ' NORTHEAST '}, inplace=True, regex=True)
df['std_address1'].replace({' N W ': ' NORTHWEST '}, inplace=True, regex=True)
df['std_address1'].replace({' S E ': ' SOUTHEAST '}, inplace=True, regex=True)
df['std_address1'].replace({' S W ': ' SOUTHWEST '}, inplace=True, regex=True)

df['std_address1'].replace({' N ': ' NORTH '}, inplace=True, regex=True)
df['std_address1'].replace({' S ': ' SOUTH '}, inplace=True, regex=True)
df['std_address1'].replace({' E ': ' EAST '}, inplace=True, regex=True)
df['std_address1'].replace({' W ': ' WEST '}, inplace=True, regex=True)

df['std_address1'].replace({' NE ': ' NORTHEAST '}, inplace=True, regex=True)
df['std_address1'].replace({' NW ': ' NORTHWEST '}, inplace=True, regex=True)
df['std_address1'].replace({' SE ': ' SOUTHEAST '}, inplace=True, regex=True)
df['std_address1'].replace({' SW ': ' SOUTHWEST '}, inplace=True, regex=True)

#Replace double space w single space -- run twice to catch multi spaces
df['std_address1'].replace({'  ': ' '}, inplace=True, regex=True)
df['std_address1'].replace({'  ': ' '}, inplace=True, regex=True)

df['std_address2'].replace({'  ': ' '}, inplace=True, regex=True)
df['std_address2'].replace({'  ': ' '}, inplace=True, regex=True)

# in case there's a "Suite #" that got changed to "SUITE SUITE"
df['std_address1'].replace({' SUITE SUITE ': ' SUITE '}, inplace=True, regex=True)
df['std_address2'].replace({' SUITE SUITE ': ' SUITE '}, inplace=True, regex=True)

df['std_address1'] = df['std_address1'].str.strip()
df['std_address2'] = df['std_address2'].str.strip()
df['std_city'] = df['std_city'].str.strip()

df = df.filter(['Address','std_address1','address2','std_address2'], axis=1)

print(df)

# df.to_csv('addr_out.csv')
