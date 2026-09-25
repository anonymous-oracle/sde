# main.tf — line-by-line analysis

## Lines 1-8
- Configures AWS provider region and availability zones data source.

## Lines 9-16
- Defines locals for AZ count, AZ list, and subnet CIDRs.

## Lines 17-24
- Starts VPC module with source/version, name, and CIDR.

## Lines 25-32
- Sets subnet lists and NAT/DNS hostname settings.

## Lines 33-40
- Adds public subnet tags for cluster and ELB role.

## Lines 41-48
- Adds private subnet tags and starts EKS module block.

## Lines 49-56
- Sets EKS module source/version, name, version, VPC IDs.

## Lines 57-64
- Configures public/private endpoints and auth mode settings.

## Lines 65-72
- Starts addons map with vpc-cni and conflict resolution flags.

## Lines 73-80
- Adds pod identity agent and begins aws-ebs-csi-driver settings.

## Lines 81-88
- Completes EBS CSI driver config and adds coredns settings.

## Lines 89-96
- Completes coredns and defines kube-proxy addon settings.

## Lines 97-104
- Ends addons and starts managed node group definition.

## Lines 105-112
- Configures node group AMI, instance types, and scaling.

## Lines 113-120
- Adds node labels and tags for environment and managed-by.

## Lines 121-128
- Closes node groups and adds module tags.

## Lines 129-136
- Sets module tags and starts BuildKit IAM role module.

## Lines 137-144
- Configures BuildKit role name and OIDC provider mapping.

## Lines 145-152
- Adds service account mapping and ECR power user policy.

## Lines 153-160
- Fetches AWS LB controller policy JSON and creates IAM policy.

## Lines 161-168
- Completes IAM policy and starts EBS CSI driver role module.

## Lines 169-176
- Configures EBS CSI role name and policy attachments.

## Lines 177-184
- Adds OIDC provider mapping for EBS CSI controller service account.

## Lines 185-192
- Starts AWS load balancer controller role module configuration.

## Lines 193-200
- Disables built-in policy and attaches custom policy ARN.

## Lines 201-208
- Sets OIDC provider/service account for load balancer controller.

## Lines 209-216
- Outputs BuildKit and EBS CSI role ARNs.

## Lines 217-224
- Outputs load balancer controller role ARN.

## Lines 225-225
- End of file.
