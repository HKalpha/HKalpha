from astropy.io import fits
import os
import csv

keys = ['SIMPLE',
 'BITPIX',
 'NAXIS',
 'NAXIS1',
 'NAXIS2',
 'BSCALE',
 'BZERO',
 'OBSERVAT',
 'DATE-OBS',
 'TIME-OBS',
 'UT',
 'ST',
 'HA',
 'RA',
 'DEC',
 'EQUINOX',
 'MJD-OBS',
 'ZD',
 'AIRMASS',
 'RA2000',
 'DEC2000',
 'EXPTIME',
 'TELESCOP',
 'DETECTOR',
 'GAIN',
 'RDNOISE',
 'IMAGETYP',
 'OBJECT',
 'PROG-ID',
 'OBSERVER',
 'INSTRUME',
 'COMMENT']

basedir = input(f"Input files directory: ")
tabledir = input(f"Inpute table directory: ")

basedates = os.listdir(basedir)

#Extraigo la informacion de los headers
rows = []
for basedate in basedates:
    basedatedir = basedir + "/" + basedate
    dates = [date for date in os.listdir(basedatedir) if date.isdigit() or date[1:].isdigit()]
    
    for date in dates:
        datedir = basedatedir +'/'+ date
        fit_files = [ x for x in os.listdir(datedir) if x[len(x)-3:] == 'fit' or x[len(x)-4:] == 'fits']
        os.chdir(datedir)
        
        for file in fit_files:
            values = []
            
            with fits.open(file) as f:
                hdr = f[0].header
                
            for key in keys:
                try:
                    values.append(hdr[key])
                except:
                    values.append("None")
                        
            rows.append([file] + values) # row = fname, -- values --
            
os.chdir(tabledir)

#Escribo la tabla
tablename = 'table'

with open(tablename +'.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow( ['FNAME'] + keys )

    # write multiple rows
    writer.writerows(rows)

