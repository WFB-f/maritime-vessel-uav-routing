# Data description

## Origin and coordinates

The target locations are synthetically constructed for computational experiments motivated by maritime patrol operations in the Bohai Sea region of China. They are specified in a local Cartesian coordinate system, with distances in kilometres. These files contain synthetic coordinates, not GPS observations or mapped maritime records. The departure and return port is `(0, 0)`.

The released coordinate files are copied without changing their numerical values. Each target requires four minutes of monitoring. These input values are computational experiment settings.

## Target-file fields

| Field | Meaning | Unit |
|---|---|---|
| `target_id` | Target identifier, starting at 1 | None |
| `x_km` | Target x coordinate | km |
| `y_km` | Target y coordinate | km |
| `monitoring_minutes` | Required monitoring duration | min |

## Physical settings

| Parameter | Value |
|---|---:|
| Vessel speed | 20 km/h |
| UAV speed | 90 km/h |
| Vessel activation cost | 50,000 CNY per activated vessel |
| Vessel sailing cost | 85 CNY/km |
| UAV flight cost | 5 CNY/km |
| UAV endurance | 1 h |
| Patrol-cycle limit | 20 h |
| UAVs carried per vessel | 1 |

Per-instance values are recorded in `data/instance_catalog.csv`. Counts of targets, available vessels, and task groups vary by instance. The target monitoring duration must be converted from minutes to hours when used with the endurance and patrol-cycle limits.

## Model conventions

Every target is visited once. Each activated vessel supports its dedicated UAV. A sortie's complete launch-to-recovery duration includes flight, monitoring, and any airborne waiting. The vessel's complete route duration includes inter-group movements, synchronization, and return to the port. Sailing and UAV flight during the same sortie occur concurrently and must not be added twice when calculating elapsed patrol time. Sailing and flying distances are Euclidean distances in the coordinate system.

The catalogue's `sha256` field identifies the exact coordinate file for each released instance.
