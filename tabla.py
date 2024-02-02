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

#Digo que ikidirectorios tengo que analizar
ikidir = '/home/abuccino/disquito/HKa/fede/basedatos'
ikidates = os.listdir(ikidir)
ikidates.remove('1217')

#Analizo ikidirectorios
for ikidate in ikidates:
    obsdir = ikidir + '/' + ikidate
    os.chdir(obsdir)
    dates = os.listdir()
    #Extraigo la informacion de los headers
    rows = []
    print(obsdir)
    for date in dates:
        datedir = obsdir +'/'+ date
        print(datedir)
        os.chdir(datedir)
        fit_files = [ x for x in os.listdir() if x[len(x)-3:] == 'fit' or x[len(x)-4:] == 'fits']
        for file in fit_files:
            print(file)
            with fits.open(file) as f:
                hdr = f[0].header
                values = [hdr[key] for key in keys]
                rows.append([file] + values) # row = fname, -- values --
            
os.chdir('/home/abuccino/disquito/HKa/fede')

#Escribo la tabla
tablename = 'tabla1'

with open(tablename +'.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow( ['FNAME'] + keys )

    # write multiple rows
    writer.writerows(rows)