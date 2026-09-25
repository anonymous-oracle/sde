# Makefile — line-by-line analysis

## Lines 1-8
- Declares phony targets and prints available help commands/description.

## Lines 9-16
- Continues help output and starts clean-all target.

## Lines 17-24
- clean-all stops/removes containers, volumes, and images with echo status.

## Lines 25-32
- Finishes cleanup message and defines clean-start-nasiko chaining.

## Lines 33-40
- backend-app target stops app compose, removes backend image, starts compose.

## Lines 41-48
- Waits and starts redis listener, then begins router target definition.

## Lines 49-56
- router target stops/removes router image and restarts router compose.

## Lines 57-64
- orchestrator and redis-listener targets run services via uv.

## Lines 65-72
- start-nasiko target stops/removes containers and volumes.

## Lines 73-75
- Finishes start-nasiko by running orchestrator and redis listener.
