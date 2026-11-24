# Algorithm outline

The procedure combines an initial spatial grouping, group-level route construction, continuous launch-recovery refinement, and three-layer adaptive neighborhood search. The following pseudocode describes the main ideas and is not an executable implementation.

## Main procedure

```text
Input: target coordinates, monitoring durations, physical parameters,
       prescribed group count f, available vessel count m, search budget.

1. Construct an initial target partition and a feasible patrol plan,
   including vessel routes and intra-group UAV visiting orders.
2. Where enabled, use group-level dynamic programming to propose
   vessel assignments and group visiting sequences.
3. Reconstruct each proposed patrol structure and check feasibility.
   Retain the best verified starting plan obtained.
4. Refine launch and recovery locations for the retained structure
   through a continuous SOCP subproblem, and apply route descent.
5. During the remaining search budget:
      Select a task-group, UAV-order, or vessel-route neighborhood.
      Generate a candidate discrete structure.
      Refine its continuous locations and verify the resulting schedule.
      Reject candidates that violate coverage or physical time limits.
      Apply the temperature-based acceptance rule to feasible candidates.
      Update the best feasible plan and neighborhood-layer weights.
      Apply the configured route-intensification and consolidation steps.
6. Perform the configured final refinement and return the best
   physically verified plan obtained within the search budget.
```

## Three search layers

- **Task-group layer:** adjusts which targets belong to each task group.
- **UAV layer:** adjusts visiting orders within task groups.
- **Vessel layer:** adjusts group assignments to vessels and group visiting orders.

The group count is prescribed. Moving targets between groups does not imply optimizing the number of groups.

## Evaluation

The reported objective is the sum of vessel activation, vessel sailing, and UAV flight costs for a feasible patrol plan. Complete UAV airborne durations and complete vessel return times are checked. Geometric scores used to order search proposals do not serve as feasibility certificates or replace the reported objective value.

With the discrete patrol structure fixed, the continuous subproblem refines launch and recovery locations. Conditional global optimality applies to this subproblem when certified by the solver; the complete heuristic does not provide a global optimality guarantee.
