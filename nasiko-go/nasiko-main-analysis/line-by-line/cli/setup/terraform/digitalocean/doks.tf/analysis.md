# doks.tf — line-by-line analysis

## Lines 1-8
- Reads available Kubernetes versions and begins DOKS cluster resource.

## Lines 9-16
- Configures cluster version/upgrade/HA and starts node_pool settings.

## Lines 17-24
- Sets autoscaling min/max and labels/tags for node pool.

## Lines 25-32
- Closes primary cluster tags and starts additional node pool resource.

## Lines 33-40
- Configures additional pool sizing and autoscaling.

## Lines 41-47
- Sets labels/tags for additional pool and closes resource.
