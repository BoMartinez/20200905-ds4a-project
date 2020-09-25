# Acerca del data set

## Tabla de datos disponibles

De acuerdo a los datos entregados por la entidad tenemos el siguiente detalle:

|        **FIELD**    |**TYPE** |                                    **DESCRIPTION**                                |
|:------------------- |:------- |:--------------------------------------------------------------------------------- |
| SECUENCIARECORRIDO  | INTEGER | Primary key that identifies the track for a vehicle                               |
| RECORRIDOFINALIZADO | INTEGER | Complete / incomplete flag (S/N)                                                  |
| IDVEHICULO          | INTEGER | unique identifier for a vehicle                                                   |
| CODIGORUTA          | STRING  | unique identifier for a track, each of these identifiers are related to a KML file|
| FECHAREGISTRO       | DATE    | date and time when the data was recorded                                          |
| LATITUD             | FLOAT   | The latitude where passengers board/alight the vehicle*                           |
| LONGITUD            | FLOAT   | The longitude where passengers board/alight the vehicle*                          |
| SUBENDELANTERA      | INTEGER | Quantity of passengers that board the vehicle through the front door              |
| SUBENTRASERA        | INTEGER | Quantity of passengers that board the vehicle through the back door               |
| BAJANDELANTERA      | INTEGER | Quantity of passengers that alight the vehicle through the front door             |
| BAJANTRASERA        | INTEGER | Quantity of passengers that alight the vehicle through the back door              |


### SECUENCIARECORRIDO
Es un indicador unico que identifica la secuencia del corrido del vehiculo por dia, Su tipo es entero.

### RECORRIDOFINALIZADO
Variable tipo factor que indica si el recorrido fue finalizado o no.

### IDVEHICULO
Campo tipo entero que identifica el vehiculo que estan prestando el recorrido en la ruta.

### CODIGORUTA
Codigo de identificacion unic0 del trayecto o ruta en donde se registra la transaccion del pasajero.

### FECHAREGISTRO
Campo de fecha y hora donde sucede el evento de subida y baja del pasajero.

### LATITUD y LONGITUD
Ubicacion geografica expresada en Latitud y longitud del evento.

### SUBENDELANTERA y SUBENTRASERA
Cantidad de personas que abordan el vehiculo por la parte delantera y trasera respectivamente. La suma de estas dos variables corresponde al total de personas que abordan el vehiculo en un instante dado.


### BAJANDELANTERA y BAJANTRASERA
Cantidad de persona que desciende del vehiculo por la parte delantera y trasera respectivamente.

