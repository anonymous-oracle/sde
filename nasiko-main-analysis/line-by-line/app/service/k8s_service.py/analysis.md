# k8s_service.py — line-by-line analysis

## Lines 1-8
- Imports logging/typing, Kubernetes client/config, settings, and starts K8sService class.

## Lines 9-16
- Class docstring and __init__ begin; stores logger and K8S_ENABLED flag.

## Lines 17-24
- Comments on config loading; disabled path sets API handles to None.

## Lines 25-32
- Sets namespace/buildkit/secret names and returns; tries incluster config.

## Lines 33-40
- Falls back to local kubeconfig and logs success; handles config exceptions.

## Lines 41-48
- Disables service on config failure and sets constants before returning.

## Lines 49-56
- Initializes Kubernetes API clients and starts constants block.

## Lines 57-64
- Sets namespace/buildkit address/secret names; _ensure_enabled guard defined.

## Lines 65-72
- Raises when disabled; _is_harbor_registry checks Harbor internal URL.

## Lines 73-80
- _get_buildctl_command extracts registry and defines base buildctl args.

## Lines 81-88
- Continues base buildctl args for dockerfile context.

## Lines 89-96
- Adds insecure output for Harbor and standard output for others.

## Lines 97-104
- Returns command; create_build_job signature and docstring start.

## Lines 105-112
- Docstring args; ensures enabled, builds job_name.

## Lines 113-120
- Defines emptyDir workspace volume.

## Lines 121-128
- Defines harbor auth secret volume with dockerconfigjson path.

## Lines 129-136
- Defines git-clone init container with workspace mount.

## Lines 137-144
- Defines buildkit client container and BUILDKIT_HOST env.

## Lines 145-152
- Sets buildctl command and workspace/auth mounts.

## Lines 153-160
- Builds Job spec metadata and JobSpec parameters.

## Lines 161-168
- Builds PodTemplateSpec with init/main containers and volumes.

## Lines 169-176
- Sets security context and submits job via Batch API.

## Lines 177-184
- Logs submission and handles API exceptions with False return.

## Lines 185-192
- deploy_agent signature and docstring start.

## Lines 193-200
- Docstring args; ensures enabled and sets app label.

## Lines 201-208
- Prepares image/secret and handles Harbor NodePort conversion.

## Lines 209-216
- Logs conversion and builds env vars list with PORT.

## Lines 217-224
- Adds env_vars and starts Deployment definition.

## Lines 225-232
- Sets Deployment metadata/spec with selector and template.

## Lines 233-240
- Configures pod spec with image_pull_secrets and container.

## Lines 241-248
- Sets container image/ports/env and closes Deployment.

## Lines 249-256
- Creates deployment in namespace and starts Service definition.

## Lines 257-264
- Defines ClusterIP service and submits via Core API.

## Lines 265-272
- Builds internal DNS URL and returns deployment metadata.

## Lines 273-280
- Handles AlreadyExists and logs other API errors.

## Lines 281-288
- get_job_status reads job and returns status state string.

## Lines 289-296
- Handles API exception by returning "unknown".

## Lines 297-304
- create_build_job_from_upload signature and docstring start.

## Lines 305-312
- Describes upload build flow/args and ensures enabled; builds job_name.

## Lines 313-320
- Defines workspace/auth volumes and initializes volumes_list.

## Lines 321-328
- Handles local_files_path for ConfigMap or host path usage.

## Lines 329-336
- Logs ConfigMap usage and defines configmap volume.

## Lines 337-344
- Defines init container to copy/decode ConfigMap files.

## Lines 345-352
- Sets init container mounts for workspace/configmap data.

## Lines 353-360
- HostPath branch: mount local files and define copy-local-files container.

## Lines 361-368
- copy-local-files command/mounts and begins backend download branch.

## Lines 369-376
- Computes version_param from agent_path and logs versioned download.

## Lines 377-384
- Builds download URL and logs, then defines download init container.

## Lines 385-392
- download init container curl/tar command and workspace mount.

## Lines 393-400
- Defines buildkit client container for upload jobs.

## Lines 401-408
- Sets buildctl command and mounts workspace/auth config.

## Lines 409-416
- Builds Job spec with init/main containers and volumes list.

## Lines 417-424
- Sets TTL/backoff and pod security context in JobSpec.

## Lines 425-432
- Submits job to namespace and returns True on success.

## Lines 433-440
- Handles API exceptions and returns False.

## Lines 441-448
- list_agent_deployments signature/docstring and list deployments call.

## Lines 449-456
- Filters deployments by prefix and accumulates matches.

## Lines 457-464
- Logs count, returns list, handles API errors.

## Lines 465-472
- delete_agent_deployment signature/docstring and begins deletion.

## Lines 473-480
- Deletes deployment, handles 404, and tracks success flag.

## Lines 481-488
- Defines download-agent init container command and workspace mount.

## Lines 489-496
- Closes init container and starts buildkit client container.

## Lines 497-504
- Sets buildctl command and workspace/auth volume mounts.

## Lines 505-512
- Closes container and begins Job spec with metadata.

## Lines 513-520
- Adds JobSpec fields, pod template, and init/main containers.

## Lines 521-528
- Sets volumes/security context and closes Job spec.

## Lines 529-536
- Submits upload build job and handles ApiException with False return.

## Lines 537-544
- list_agent_deployments signature/docstring and argument details.

## Lines 545-552
- Starts try block and lists deployments in namespace.

## Lines 553-560
- Filters deployments by agent_id prefix and accumulates matches.

## Lines 561-568
- Logs count, returns list, and handles ApiException.

## Lines 569-576
- Returns empty list on errors and starts delete_agent_deployment signature.

## Lines 577-584
- delete_agent_deployment docstring describes purpose/args/return.

## Lines 585-592
- Starts deletion, sets flag, and calls delete deployment API.

## Lines 593-600
- Logs deletion, handles 404, and logs other errors.

## Lines 601-608
- Marks failure and starts deleting associated service.

## Lines 609-616
- Logs service deletion and handles 404/not found cases.

## Lines 617-624
- Logs service delete errors, returns deletion_success, or False on exception.

## Lines 625-632
- create_configmap_with_files signature and docstring header.

## Lines 633-640
- Docstring args/returns and begins try block.

## Lines 641-648
- Constructs ConfigMap object with metadata and data payload.

## Lines 649-656
- Creates ConfigMap, logs success, and returns True.

## Lines 657-664
- Handles API/generic exceptions and returns False.

## Lines 665-672
- delete_configmap signature and docstring header.

## Lines 673-680
- Docstring returns, deletes ConfigMap, and logs success.

## Lines 681-688
- Returns True and begins ApiException handling for 404.

## Lines 689-696
- Returns True on 404; logs errors and returns False otherwise.

## Lines 697-698
- Logs generic exception and returns False.
