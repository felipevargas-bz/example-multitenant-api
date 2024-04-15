
# Documentación de Servicios Lambda Multitenant

## Tablas de Datos

### 1. **tenantTable**: 
Esta tabla almacena información detallada sobre cada  (tenant). Cada registro incluye información como ID de tenant, token, correo electrónico, nombre de la empresa, zona horaria, y más.
   
**Ejemplo de registro:**
```json
{
  "tenant_id": "client_example",
  "created_at": "YYYY-MM-DD",
  "email": "contact@example.com",
  "name": "Example Inc",
  "offset_in_seconds": "time_offset",
  "status": true,
  "time_zone": "GMT-X"
}
```

### 2. **userTenant**: 
Relaciona los correos electrónicos de los usuarios, registrados en Cognito, con la tabla tenant. Contiene campos como email, nombre del usuario, estado del usuario, y ID del tenant.

**Ejemplo de registro:**
```json
{
  "email": "user@example.com",
  "name": "Example User",
  "status": true,
  "tenant_id": "client_example"
}
```

## Funciones Lambda para Autenticación y Gestión de Usuarios

### 1. **Validación de Usuario por Email (`validateUserByEmail`)**: 
Valida si un usuario existe y si pertenece a un tenant activo.
   
- Recibe el email del usuario.
- Busca en la tabla `userTenant` por email para obtener el `tenant_id`.
- Busca en la tabla `tenantTable` usando el `tenant_id` para obtener detalles del tenant.
- Verifica que ambos, usuario y tenant, estén activos.
- Devuelve datos relevantes del tenant si todo es correcto o un error si no.

**Ejemplo de código:**
```python
user_db = get_table_item('email', email, 'userTenant')
tenant_id = user_db['tenant_id']
company_db = get_table_item('tenant_id', tenant_id, 'tenantTable')
```

### 2. **Inicio de Sesión de Usuario (`lambda_handler` en función de login)**: 
Maneja el proceso de autenticación del usuario.
   
- Extrae el email y la contraseña del cuerpo de la solicitud.
- Invoca `validateUserByEmail` para verificar la existencia del usuario y obtener datos del tenant.
- Si el usuario es validado, procede a autenticar con Cognito usando `initiate_auth`.
- Retorna los resultados de la autenticación junto con los datos del tenant.

**Ejemplo de código:**
```python
validation_result = validate_user({'email': email})
```

### 3. **Verificación de Token de Acceso (`verify_token`)**: 
Verifica si el token proporcionado es válido usando el servicio de Cognito.
   
- Recibe un token de acceso.
- Utiliza `cognito-idp` para validar el token con `get_user`.
- Devuelve verdadero si el token es válido, falso de lo contrario.

**Ejemplo de código:**
```python
response = cognito_client.get_user(AccessToken=token)
```

## Consideraciones Generales

- **Control de Acceso**: Utiliza headers de CORS adecuados para permitir o restringir accesos según necesidades.
- **Manejo de Errores**: Implementa una gestión de errores robusta para cada función, capturando excepciones y proporcionando mensajes de error claros.
- **Seguridad**: Asegura que toda comunicación con servicios externos sea realizada usando tokens y permisos adecuados para proteger los datos sensibles y operaciones críticas.

Esta documentación cubre los aspectos críticos de las operaciones en un entorno multitenant usando AWS Lambda y DynamoDB, diseñada para desarrolladores familiarizados con estos servicios. Asegúrate de adaptar las funciones y ejemplos de código a tus necesidades específicas y verificar que cumplen con los requerimientos de seguridad de tu organización.
