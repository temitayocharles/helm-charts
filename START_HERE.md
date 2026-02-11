# Start Here

This repo holds Helm charts only. Values live in GitOps. Follow in order.

## 1. What This Repo Is
Central Helm chart repository. Each app has its own chart under `applications/<app>`.

## 2. Repo Map (What Lives Where)
- Charts: [applications](applications)
- Shared templates/helpers: [shared](shared)

## 3. Add a New Chart
1. Create a new chart folder under `applications/<app>`.
1. Add `Chart.yaml`, `values.yaml`, and templates.
1. Keep defaults minimal and safe.

## 4. Update a Chart
1. Edit templates or default values.
1. Increment chart version in `Chart.yaml`.
1. Commit and push.

## 5. How It’s Consumed
ArgoCD applications in the platform‑gitops repo reference these charts as a source.

## 6. Troubleshooting
- If Argo shows render errors, run `helm template` locally with the values from GitOps.
