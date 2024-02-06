# Obtener una tabla a partir de los headers de CASLEO

## Organización del directorio con los archivos

El directorio con los archivos *fit* deben estar organizados de una forma en particular. Es necesario que exista un directorio base que contenga subdirectorios cuyos nombres (YYYYMMDD) se correspondan con la fechas en las que se realizaron las observaciones contenidas en dichos subdirectorios. Por observaciones se entienden a los archivos de extension *fit*, aunque en estos subdirectorios también pueden haber otros tipos de archivos que le seran transparentes a la lectura del script que se introducirá a continuación.

### Ejemplo de directorio base:
![image](https://github.com/HKalpha/HKalpha/assets/158530486/7b41d1c4-0e3b-4152-9cb1-c49b5222f726)
### Ejemplo de subdirectorio:
![image](https://github.com/HKalpha/HKalpha/assets/158530486/598d6d76-106e-4b50-ad30-2d10c550093e)

## Como hacer la tabla

La tabla se construye a partir de los headers de los archivos *fit*. Las columnas de la tabla se nombran a partir de las *keys* de los headers, aunque en el módulo **table.py** estos *keys* estan contenidos en una lista, por lo que se puede modificar de acuerdo a lo requerido, ya sea porque los archivos fit tengan headers con *keys* distintos o porque se quiera hacer la tabla solo con algunas *keys* een particular.
