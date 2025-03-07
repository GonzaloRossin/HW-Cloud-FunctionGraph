# Creación de una Función en FunctionGraph con Python 3.9

Este repositorio proporciona una guía para crear funciones de FunctionGraph utilizando Python 3.9. Se abordará como crear las funciones, ingresar el código y cargar las dependencias necesarias para poder realizar distintas operaciones para los servicios de CCE y RDS dentro de Huawei Cloud. Las operaciones alcanzadas por los scripts contenidos en este repositorio sonÑ

 - CCE
    - Hibernar un cluster con su respectivo id
    - Despertar un cluster con su respectivo id
 - RDS
  - Parar instancias RDS en batch
  - Iniciar una instancia RDS con su respectivo id

## Colaboradores

 - Franco Baez, Huawei Cloud Solution Architect 

## Prerrequisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.9**: Los scripts fueron desarrollados en Python versión 3.9. Asegurarse que el entorno de desarrollo dentro de FunctionGraph sea el mismo.

- **Permisos adecuados**: Es fundamental que el agency cuente con los permisos necesarios para llevar a cabo las operaciones que se deseen. Por ejemplo, para hibernar un cluster de CCE, es necesario que el agency seleccionado tenga los permisos para realizar esta operacion.

## Creación de la Función

1. **Crear una funcion en FunctionGraph**: Ir a la consola de Huawei cloud, servicio FunctionGraph. Dentro de este servicio seleccionar "Create Function" y luego seleccionar la opcion "Create from Scratch". En el formulario que se despliega se solicitara los siguientes campos:
- Function Type: seleccionar la opcion "Event Function"
- Region: region donde se va a crear la funcion
- Project: project id de la region (usar el default que se selecciona para la region)
- Function Name: nombre que se desea colocar a la funcion
- Agency: agency con el que se ejecutara la funcion (recordar elegir uno con los permisos adecuados)
- Runtime: Entorno de ejecucion con el que se ejecutara el codigo (Python 3.9)

2. **Cargar el codigo**: Una vez creada la funcion dirigirse a la pestana de codigo y copiar el codigo de uno de los scripts y pegarlo en el editor que FunctionGraph posee.

3. **Cargar las variables de entorno**: Una vez ingresado el codigo de la funcion es necesario ingresar las variables de entorno que usara esa funcion. Las variables de entorno se configuran en la seccion de "Configuration" -> "Environment Variables". Una vez en esa pantalla seleccionar la opcion de editar variables de entorno para modificar las existentes y agregar nuevas. Para los scripts de este repositorio, las variables de entorno son las siguientes:
- CCE
    - region: la-south-2
    - clusterId: "INGRESAR EL CLUSTER ID AQUI"
    - ak: "INGRESAR EL AK DE LA CUENTA AQUI"
    - sk: "INGRESAR EL SK DE LA CUENTA AQUI"
- RDS
Para iniciar un rds:
- region: la-south-2
- ak: "INGRESAR EL AK DE LA CUENTA AQUI"
- sk: "INGRESAR EL SK DE LA CUENTA AQUI"
- projectId: "INGRESAR EL PROJECT ID DE LA REGION UTILIZADA"
- instanceId: "INGRESAR LA ID DE LA INSTANCIA A INICIAR"

Para detener un rds:
- region: la-south-2
- ak: "INGRESAR EL AK DE LA CUENTA AQUI"
- sk: "INGRESAR EL SK DE LA CUENTA AQUI"
- projectId: "INGRESAR EL PROJECT ID DE LA REGION UTILIZADA"

para el caso de detener el rds en batch, los ID de las instancias se especifican dentro del codigo

4. **Agregar las dependencias**: los scripts usan el sdk de Huawei para funcionar, es necesario cargar las mismas para que FunctionGraph las pueda utilizar. Dentro de este repositorio, dentro de la carpeta "dependencies" se encuentran 2 archivos con los sdk para ser cargados dentro de FunctionGraph. Para hacer esto es necesario ir a la seccion de Code -> Dependencies, clickear el boton "Add" y dentro del tipo private seleccionar la opcion de "create dependency" para para poder cargar el archivo .zip. Una vez cargado el .zip ya va a estar disponible para ser seleccionado desde la opcion de agregar dependencia. En caso que el .zip pese mas de 10MB, es necesario previamente cargar el .zip a OBS y cargarla como "Upload from OBS" para luego poder crear la dependencia.

## Advertencias
Existe la posibilidad que la ejecucion de la funcion tome mas de 3 segundos en terminar su ejecucion, en este caso sera necesario incrementar el "Timeout time" dentro de la seccion de "Configuration" -> "Basic Settings"


## Documentacion