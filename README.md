# Creación de una Función en FunctionGraph con Python 3.9

Este repositorio proporciona una guía para crear funciones de FunctionGraph utilizando Python 3.9. Se abordará cómo crear las funciones, ingresar el código y cargar las dependencias necesarias para realizar distintas operaciones en los servicios de CCE y RDS dentro de Huawei Cloud. Las operaciones cubiertas por los scripts contenidos en este repositorio son:

- **CCE**:
  - Hibernar un clúster con su respectivo ID.
  - Despertar un clúster con su respectivo ID.
- **RDS**:
  - Detener instancias RDS en lote.
  - Iniciar una instancia RDS con su respectivo ID.

## Colaboradores

- Franco Báez, Arquitecto de Soluciones en Huawei Cloud.

## Prerrequisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.9**: Los scripts fueron desarrollados en Python versión 3.9. Asegúrate de que el entorno de desarrollo dentro de FunctionGraph sea el mismo.

- **Permisos adecuados**: Es fundamental que el *agency* cuente con los permisos necesarios para llevar a cabo las operaciones deseadas. Por ejemplo, para hibernar un clúster de CCE, es necesario que el *agency* seleccionado tenga los permisos correspondientes.

## Creación de la Función

1. **Crear una función en FunctionGraph**: Accede a la consola de Huawei Cloud y dirígete al servicio FunctionGraph. Dentro de este servicio, selecciona "Create Function" y luego "Create from Scratch". En el formulario que se despliega, completa los siguientes campos:
   - **Function Type**: Selecciona "Event Function".
   - **Region**: Región donde se creará la función.
   - **Project**: ID del proyecto de la región (usa el predeterminado para la región).
   - **Function Name**: Nombre que deseas asignar a la función.
   - **Agency**: *Agency* con el que se ejecutará la función (recuerda elegir uno con los permisos adecuados).
   - **Runtime**: Entorno de ejecución para el código (Python 3.9).

   ![Creación de Función](/images/CreateFunction.png)

2. **Cargar el código**: Una vez creada la función, dirígete a la pestaña de código y copia el código de uno de los scripts, pegándolo en el editor que proporciona FunctionGraph.

   ![Pegar Código de la Función](/images/PasteFunction.png)

3. **Configurar las variables de entorno**: Después de ingresar el código de la función, es necesario configurar las variables de entorno que utilizará. Estas se configuran en la sección "Configuration" -> "Environment Variables". Allí, selecciona la opción de editar variables de entorno para modificar las existentes o agregar nuevas. Para los scripts de este repositorio, las variables de entorno son las siguientes:

   - **CCE**:
     - `region`: la-south-2
     - `clusterId`: "INGRESAR EL CLUSTER ID AQUÍ"
     - `ak`: "INGRESAR EL AK DE LA CUENTA AQUÍ"
     - `sk`: "INGRESAR EL SK DE LA CUENTA AQUÍ"
   - **RDS**:
     - Para iniciar un RDS:
       - `region`: la-south-2
       - `ak`: "INGRESAR EL AK DE LA CUENTA AQUÍ"
       - `sk`: "INGRESAR EL SK DE LA CUENTA AQUÍ"
       - `projectId`: "INGRESAR EL PROJECT ID DE LA REGIÓN UTILIZADA"
       - `instanceId`: "INGRESAR LA ID DE LA INSTANCIA A INICIAR"
     - Para detener un RDS:
       - `region`: la-south-2
       - `ak`: "INGRESAR EL AK DE LA CUENTA AQUÍ"
       - `sk`: "INGRESAR EL SK DE LA CUENTA AQUÍ"
       - `projectId`: "INGRESAR EL PROJECT ID DE LA REGIÓN UTILIZADA"
     - Para detener múltiples RDS:
       - `region`: la-south-2
       - `ak`: "INGRESAR EL AK DE LA CUENTA AQUÍ"
       - `sk`: "INGRESAR EL SK DE LA CUENTA AQUÍ"
       - `projectId`: "INGRESAR EL PROJECT ID DE LA REGIÓN UTILIZADA"
     - Para escalar RDS:
       - `region`: la-south-2
       - `ak`: "INGRESAR EL AK DE LA CUENTA AQUÍ"
       - `sk`: "INGRESAR EL SK DE LA CUENTA AQUÍ"
       - `projectId`: "INGRESAR EL PROJECT ID DE LA REGIÓN UTILIZADA"
       - `instanceId`: "INGRESAR LA ID DE LA INSTANCIA A INICIAR"
       - `flavor`: "INGRESAR EL FLAVOR CODE A ESCALAR"

   Para el caso de detener el RDS en lote, los IDs de las instancias se especifican dentro del código.

   ![Variables de Entorno](/images/EnvironmentVariables.png)

4. **Agregar las dependencias**: Los scripts utilizan el SDK de Huawei para funcionar, por lo que es necesario cargar las dependencias para que FunctionGraph pueda utilizarlas. Dentro de este repositorio, en la carpeta "dependencies", se encuentran dos archivos con los SDK para ser cargados en FunctionGraph. Para hacerlo, ve a la sección "Code" -> "Dependencies", haz clic en el botón "Add" y, dentro del tipo privado, selecciona "Create Dependency" para cargar el archivo .zip. Una vez cargado, estará disponible para ser seleccionado desde la opción de agregar dependencia. Si el .zip pesa más de 10 MB, es necesario cargarlo previamente a OBS y luego seleccionarlo como "Upload from OBS" para crear la dependencia.

   ![Agregar Dependencias](/images/AddDependencies.png)

## Advertencias

Existe la posibilidad de que la ejecución de la función tome más de 3 segundos en completarse. En este caso, será necesario incrementar el "Timeout time" en la sección "Configuration" -> "Basic Settings".

## Documentación

- [Crear Función](https://support.huaweicloud.com/intl/es-us/usermanual-functiongraph/functiongraph_01_1441.html)
- [Gestión de Dependencias](https://support.huaweicloud.com/intl/es-us/usermanual-functiongraph/functiongraph_01_0391.html)
- [Crear Dependencia Privada](https://support.huaweicloud.com/intl/en-us/devg-functiongraph/functiongraph_02_0616.html)
