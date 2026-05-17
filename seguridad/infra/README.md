# Operación Hélice Negra — Infraestructura

Este directorio contiene el entorno Docker de la práctica.

## Despliegue

```bash
docker compose up -d --build
```

Tras unos segundos los cinco contenedores quedan corriendo:

| Contenedor | Redes | Puerto host |
|------------|-------|-------------|
| web-nebula | dmz, interna | 8080 |
| api-nebula | interna | — |
| db-nebula | interna | — |
| bastion-nebula | interna, gestion | 2222 |
| vault-nebula | gestion | — |

Verificación rápida:

```bash
curl -s http://localhost:8080/ | head -10
docker compose ps
```

## Reinicio limpio

```bash
docker compose down -v && docker compose up -d --build
```

## Notas

- La red `gestion` está marcada como `internal: true`. Vault sólo es alcanzable desde dentro del bastion.
- Las flags están repartidas a propósito en distintos contenedores y rutas. No las muevas si no quieres romper el walkthrough.
- Los hashes MD5 de la BBDD se han escogido para que `qwerty123` esté en cualquier rockyou estándar.
