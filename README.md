#  Pulse Monitoring System — Backend + Dashboard

Sistema de monitorización en tiempo real de datos de satélites (ISS) con generación automática de alertas y visualización en dashboard interactivo.

 Demo local: http://127.0.0.1:5500/frontend/index.html

---

## ¿Qué es Pulse Monitoring System?

Aplicación backend + frontend que simula un sistema real de monitorización de telemetría espacial.

Obtiene datos en tiempo real de un satélite (ISS), los almacena, analiza su comportamiento y genera alertas automáticamente si detecta condiciones críticas.

Incluye un dashboard visual para observar:
- Datos en tiempo real
- Alertas generadas
- Flujo interno del sistema (logs)

---

##  Arquitectura del sistema

Arquitectura desacoplada cliente-servidor:

- **Frontend** — HTML + CSS + JavaScript (dashboard en tiempo real)
- **Backend** — Python + FastAPI (API REST + lógica)
- **Base de datos** — SQLite (persistencia local)
- **Worker interno** — Thread en background (ingesta continua de datos)

---

##  Tecnologías

| Capa | Tecnología |
|------|----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Base de datos | SQLite |
| API externa | WhereTheISS.at |
| Visualización | Chart.js |
| Concurrencia | Threading |
| Gestión | Git, GitHub |

---

##  Flujo del sistema

1. El sistema consulta una API externa (ISS)
2. Obtiene velocidad del satélite
3. Guarda el dato en base de datos (Pulse)
4. Si supera el umbral → genera alerta
5. Registra logs internos del proceso
6. El frontend consulta la API cada pocos segundos
7. Se actualiza el dashboard en tiempo real

---

##  Endpoints principales

| Endpoint | Descripción |
|--------|------------|
| `/pulse` | Lista de datos del satélite |
| `/alerts` | Alertas generadas |
| `/logs` | Logs internos del sistema |
| `/health` | Estado del servicio |

---

## 📊 Dashboard

El sistema incluye un dashboard interactivo que muestra:

- 📡 Pulses (datos en tiempo real)
- 🚨 Alerts (eventos críticos)
- 🧠 Logs (flujo interno del sistema)
- 📈 Gráfica de velocidad del satélite

Actualización automática mediante polling cada pocos segundos.

---

## 🧪 Lógica de negocio

```python
if data["value"] > 20000:
    # generar alerta crítica
