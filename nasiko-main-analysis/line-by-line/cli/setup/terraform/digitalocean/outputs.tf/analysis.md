# outputs.tf — line-by-line analysis

## Lines 1-8
- Outputs cluster name/id values for the DOKS cluster.

## Lines 9-16
- Outputs cluster URN and Kubernetes version.

## Lines 17-24
- Outputs cluster status and API endpoint.

## Lines 25-32
- Outputs IPv4 address and CA certificate (sensitive).

## Lines 33-40
- Outputs kubectl config command and starts node_pools output.

## Lines 41-48
- Outputs node pool info and begins kube_config output.

## Lines 49-56
- Outputs raw kubeconfig YAML (sensitive).

## Lines 57-59
- Closes kube_config output block.
