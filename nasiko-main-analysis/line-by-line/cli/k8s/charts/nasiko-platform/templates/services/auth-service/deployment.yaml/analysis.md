# deployment.yaml — line-by-line analysis

## Lines 1-8
- Defines nasiko-auth Deployment metadata, namespace, and selector.

## Lines 9-16
- Sets pod labels/spec and starts auth container definition.

## Lines 17-24
- Configures container image, port, and NODE_ENV/MONGO_URL env vars.

## Lines 25-32
- Sets Redis URL, JWT secret, DB name, and port env vars.

## Lines 33-40
- Starts Service definition with name/namespace and ClusterIP type.

## Lines 41-48
- Sets service selector and port mapping to 8001.
