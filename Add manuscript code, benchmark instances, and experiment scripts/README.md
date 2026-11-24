# Maritime vessel-UAV collaborative routing: selected data and algorithm outline

Supporting materials for *Collaborative Routing of Coastal Patrol Vessels and UAVs for Maritime Patrol and Law Enforcement*.

This repository provides four selected synthetic input instances, physical parameters, an algorithm outline, and a small Python example for reading the data. The full optimization implementation and experimental result files are not included.

## Files

- `data/instances/`: target coordinates and monitoring times.
- `data/instance_catalog.csv`: instance sizes, port coordinates, physical parameters, and input-file checksums.
- `data/algorithm_parameters.csv`: selected algorithm and baseline parameters.
- `docs/data_description.md`: data origin, coordinate conventions, and field definitions.
- `docs/algorithm_outline.md`: conceptual pseudocode for the hierarchical solution procedure.
- `examples/read_instance.py`: a data-reading example using only the Python standard library.

## Included instances

| Instance | Role | Targets | Available vessels | Task groups |
|---|---|---:|---:|---:|
| 36_4_16 | Benchmark | 36 | 4 | 16 |
| 10_2_3 | Small example | 10 | 2 | 3 |
| 30_3_8 | Medium example | 30 | 3 | 8 |
| 50_7_18 | Large example | 50 | 7 | 18 |

An instance label follows `n_m_f`: the numbers of targets, available vessel-UAV units, and task groups. Available vessels are an upper bound; the number activated is a decision. Group membership can be adjusted while the prescribed group count remains fixed.

## Read a dataset

From the repository folder, run:

```bash
python examples/read_instance.py 36_4_16
```

The example checks the input format and prints the instance metadata. It does not optimize routes and does not require Gurobi or third-party Python packages.
