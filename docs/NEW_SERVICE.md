# New Service Playbook (Helm)

This is the step‑by‑step flow to add a new deployable service chart into this repo so ArgoCD can deploy it.

This repo **stores charts only**. Values and Argo Applications live in `platform-gitops`.

## Prereqs (Cross-Repo)
- Vault access boundaries and ESO stores exist:
  - Repo: `temitayocharles/vault-ops`
- Non‑secret config exists and ConfigMaps are generated:
  - Repo: `temitayocharles/configurations`
- Argo Application and environment values exist:
  - Repo: `temitayocharles/platform-gitops`

## 1) Create the chart (from template)
```bash
cd /Users/charlie/Desktop/helm-charts

python3 scripts/new_microservice_chart.py \
  --chart-dir cila-health-patient-service \
  --chart-name patient-service \
  --app-name cila-health-microservices \
  --service-name patient-service \
  --image-repo cila-health-patient-service \
  --hostname patient-service.local \
  --vault-repo cila-health-microservices \
  --vault-service patient-service
```

This generates:
- `applications/<chart-dir>/Chart.yaml`
- `applications/<chart-dir>/values.yaml`
- `applications/<chart-dir>/templates/*`

## 2) Validate the chart locally
```bash
helm lint applications/<chart-dir>
helm template test applications/<chart-dir> --values applications/<chart-dir>/values.yaml >/tmp/render.yaml
```

## 3) Commit and push
```bash
git add applications/<chart-dir> scripts/new_microservice_chart.py
git commit -m "feat(chart): add <chart-dir>"
git push origin main
```

## 4) Next step
Create the matching Argo Application and environment values in `platform-gitops`.
Start here:
- `platform-gitops/docs/DEPLOY_APP.md`

