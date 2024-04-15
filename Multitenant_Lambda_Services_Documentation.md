
# Servicios Lambda Multitenant

## Tablas de Datos

### 1. **tenantTable**:
Almacena detalles de cada inquilino con campos como identificación, token, email, nombre de la empresa, entre otros.

**Ejemplo de registro en DynamoDB:**
```json
{
  "tenant_id": "client_example",
  "created_at": "2024-01-01",
  "email": "contact@example.com",
  "name": "Example Corporation",
  "offset_in_seconds": "-18000",
  "status": true,
  "time_zone": "GMT-5"
}
```

### 2. **userTenant**:
Relaciona los correos de usuarios de Cognito con su correspondiente tenant en `tenantTable`.

**Ejemplo de registro en DynamoDB:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "status": true,
  "tenant_id": "client_example"
}
```

## Funciones Lambda Detalladas

### 1. **Validación de Usuario por Email (`validateUserByEmail`)**:
Confirma la existencia de un usuario y su asociación con un tenant activo.

**Flujo de validación:**
- Extraer el email del evento.
- Consultar `userTenant` para obtener el `tenant_id`.
- Usar `tenant_id` para obtener datos del tenant de `tenantTable`.
- Confirmar que ambos registros están activos.
- Devolver datos relevantes del tenant.

**Código de ejemplo para validar usuario:**
```python
def get_table_item(email, table_name):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'email': email})
    return response['Item'] if 'Item' in response else None

user_info = get_table_item(email, 'userTenant')
tenant_info = get_table_item(user_info['tenant_id'], 'tenantTable')
```

### 2. **Inicio de Sesión y Generación de Token con Cognito**:
Autentica usuarios y genera un token de acceso cuando la validación es exitosa.

**Flujo de autenticación:**
- Validar el usuario con la función anterior.
- Si es válido, usar Cognito para iniciar sesión y generar un token.
- Devolver el token y los datos del tenant.

**Código de ejemplo para generar token con Cognito:**
```python
def initiate_auth(email, password, client_id):
    cognito_client = boto3.client('cognito-idp')
    response = cognito_client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': email,
            'PASSWORD': password
        },
        ClientId=client_id
    )
    return response['AuthenticationResult']['IdToken']

token = initiate_auth(email, password, client_id)
```

### 3. **Verificación de Token de Acceso (`verify_token`)**:
Verifica la validez del token proporcionado mediante AWS Cognito.

**Código de ejemplo para verificar token:**
```python
def verify_token(token):
    cognito_client = boto3.client('cognito-idp')
    try:
        response = cognito_client.get_user(AccessToken=token)
        return True
    except:
        return False

is_valid = verify_token(token)
```
