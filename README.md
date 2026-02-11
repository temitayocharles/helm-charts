# Helm Charts Library

Central Helm chart library for platform tools and shared components.

## Structure
- Each folder is a chart (tools or shared components).
- Values overrides live in the GitOps repo and are applied by ArgoCD.

## Dependency Graph
```
helm-charts
  -> platform-gitops (ArgoCD Applications reference these charts)
  -> configurations (ConfigMaps mounted by charts)
  -> Vault (secrets injected via ESO)
```
