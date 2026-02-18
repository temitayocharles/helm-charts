# Helm Charts Library


## Start Here
- Read [START_HERE.md](START_HERE.md) for the chronological playbook.

Central Helm chart library for platform tools and shared components.

## Structure
```
helm-charts/
  platform-tools/   # Tooling charts (Argo, ESO, Prometheus, etc.)
  applications/     # App charts (per app or per service)
  shared/           # Shared helper charts (optional)
```

Values overrides live in `platform-gitops` and are applied by ArgoCD.

## Dependency Graph
```
helm-charts
  -> platform-gitops (ArgoCD Applications reference these charts)
  -> configurations (ConfigMaps mounted by charts)
  -> Vault (secrets injected via ESO)
```


## Architecture Maps
- [DEPENDENCY_LADDER.md](./DEPENDENCY_LADDER.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
