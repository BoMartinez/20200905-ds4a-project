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


The dataset comes from the records made by the devices installed in each of the vehicles in operation of El Valle de Aburrá public transport system and which are part of the Metropolitan Collective Public Transport Management Plataform (GTPC).

### SECUENCIARECORRIDO
Datatype: Integer type number.  
Meaning: It is a unique identifier of the trip of a public transport vehicle on a date and on a certain route.  
Values taken: The identifier is generated automatically with each new trip.  
Utility: By uniquely identifying the trip of a vehicle, it allows obtaining information such as the start and end date of a tour and the number of events where there was passenger movement for any trip recorded in the time horizon of the dataset. Counting the unique values of the variable returns the total recorded trips.  

### RECORRIDOFINALIZADO
Datatype: Single character text.  
Meaning: a binary variable that indicates if the vehicle's journey or route ended, that is, if it completed the route, or did not.  
Values taken: S if the vehicle tour was completed successfully, N otherwise.  
Utility: allows a trip to be classified as successful or unsuccessful during the observation time recorded in the dataset. A metric such as the rate of incomplete trips per route, for a certain transport vehicle or per period of time could be constructed.  

### IDVEHICULO
Datatype: Integer type number.  
Meaning: is an unique identifier for each vehicle that operates on the public transportation network whose trips were recorded in the dataset.  
Values taken: the number is an internal code of the entity to identify each vehicle in operation.  
Utility: It would allow obtaining the characteristics of each vehicle in an eventual crossing of the dataset with another that contains important attributes such as number of seats, number of foot passengers, maximum capacity, incidents due to mechanical failures, among others. It also allows calculating the number of vehicles in operation on a certain route or section of route or during a certain period of time, that is, the frequency of vehicles.  

### CODIGORUTA
Datatype: Integer type number.  
Meaning: Code that identifies the route for transmission to the platform.  
Values taken: Unique identifier for each route assigned by the entity.  
Utility: It is the analogous to the variable IDVEHICULO. Although each route corresponds to only one vehicle and one route, a route can have different routes as well as different associated vehicles.  

### FECHAREGISTRO
Datatype: Text containing date and time of the form dd/mm/yyyy hh:mm.  
Meaning: it is the record of the moment in which a passenger movement event occurs, that is, the date and time in which passengers board and alight each time the vehicle stops.  
Values taken: It is a date with the format dd / mm / yyyy hh: mm, where dd: is the day of the month (0 to 31), mm: is the month of the year (1 to 12), yyyy is the year (2019 and 2020) , hh: mm is the hour (00 to 23) and the minutes (00 to 59). The dates of the events are unique per trip, vehicle and route.  
Utility:  It allows filtering any data registered in the dataset, variable or metric calculated for a certain instant or time interval. The minimum interval of interest is the hour and the maximum the day.  

### LATITUD and LONGITUD
Datatype: Float type number.  
Meaning: It is the exact location in geographical coordinates of the occurrence of a passenger movement event. Latitude is the distance in degrees between any parallel and the line of the equator. Longitude is the measure of the arc between the zero meridian and the meridian of any point.  
Values taken: Latitude is between 6.10 and 6.30 degrees to the north (positive values) and longitude between 75.5 and 75.6 degrees to the west (negative values).  
Utility: In addition to georeferencing the events, it allows associating them to the nodes that the entity established in the entire public transport network of El Valle de Aburrá. This will be useful when calculating metrics on the number and flow of passengers in certain areas and route segments of the network.  

### SUBENDELANTERA and SUBENTRASERA
Datatype: Integer type number.  
Meaning: It counts the total number of passengers who board the bus at each stop on the route (designated by the two previous variables) through the front or rear door respectively.  
Values taken: Non-negative integers.  
Utility: These are the variables required to calculate the passenger load by date, by arc and by route of the public transport network. The sum of the two variables returns the total number of passengers who board a vehicle. This number when filtering by any other variable, range or group of variables, returns the number of boardings per category of variables, the rate of boardings per range, among others. Therefore, it is quite useful to build performance indicators (KPIs) that describe the operation and capabilities of the public bus transport system. By grouping boardings by areas of the transportation network, those that demand more or less transportation services can be identified.  
SUBENTRASERA usually occurs when the bus is overloaded, therefore, this variable could be used later, to find cases where such event exists.  

### BAJANDELANTERA and BAJANTRASERA
Datatype: Integer type number.  
Meaning: It is the number of passengers who alight through the front / rear door of a vehicle each time it stops.  
Values taken: Non-negative integers.  
Utility: These are the variables required to calculate the passenger load by date, by arc and by route of the public transport network. The sum of the two variables returns the total number of passengers alighting from a vehicle. This number when filtering by any other variable, range or group of variables, returns the number of alights by category of the variable, the rate of alights by range, among others. Along with the boardings, performance indicators (KPIs) can be built. By grouping the alights in passengers by zones of the transport network, the most or less popular destinations can be identified.  
