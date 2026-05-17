# Prácticas — Coordi Canarias

Ejercicios para el alumnado en prácticas: redes con Cisco Packet Tracer y
seguridad ofensiva con Docker.

## Estructura

```
practicas/
├── setup_entorno/   Sesión 0 — preparación del equipo (Ubuntu + Docker + Kali + Packet Tracer)
├── redes/           Operación Doble Nodo — dos casas inteligentes con VLANs, NAT, ACLs e IoT cruzado
└── seguridad/       Operación Hélice Negra — CTF sobre cinco contenedores en tres redes Docker
    └── infra/       docker-compose y servicios vulnerables del laboratorio
```

## Orden recomendado

1. **`setup_entorno/`** — instalación de Ubuntu y dependencias. Imprescindible antes de las prácticas.
2. **`redes/before_alumno`** — conceptos previos para la práctica de redes (no es la práctica).
3. **`redes/enunciado_alumno`** — práctica con Cisco Packet Tracer en modo multiusuario.
4. **`seguridad/before_alumno`** — conceptos previos para la práctica de seguridad (no es la práctica).
5. **`seguridad/enunciado_alumno`** — CTF con cinco flags `HELICE{...}` sobre la infraestructura Docker.

## Despliegue del laboratorio de seguridad

```bash
cd seguridad/infra
docker compose up -d --build
```

Para más detalle ver `seguridad/infra/README.md`.

## Aviso

Las vulnerabilidades de `seguridad/infra/` son **intencionadas y didácticas**.
NO replicar estas configuraciones en sistemas reales y NO conectar el host a
redes Wi-Fi públicas mientras los contenedores estén corriendo.
