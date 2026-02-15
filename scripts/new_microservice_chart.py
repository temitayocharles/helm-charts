#!/usr/bin/env python3
"""Create a new application chart by copying the microservice template.

This is intentionally simple (string substitution only) so it works without extra deps.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "applications" / "_templates" / "microservice"


def replace_in_file(path: Path, mapping: dict[str, str]) -> None:
    text = path.read_text()
    for k, v in mapping.items():
        text = text.replace(k, v)
    path.write_text(text)


def main() -> None:
    p = argparse.ArgumentParser(description="Create a new chart from the microservice template")
    p.add_argument("--chart-dir", required=True, help="Directory name under applications/ (e.g. cila-health-labs-api)")
    p.add_argument("--chart-name", required=True, help="Helm chart name (e.g. labs-api)")
    p.add_argument("--app-name", required=True, help="Human app name (e.g. cila-health-microservices)")
    p.add_argument("--service-name", required=True, help="Service/component name (e.g. patient-service)")
    p.add_argument("--image-repo", required=True, help="GHCR image repo name only (e.g. cila-health-patient-service)")
    p.add_argument("--hostname", required=True, help="Ingress hostname (e.g. patient-service.local)")
    p.add_argument("--vault-namespace", default="temitayo", help="Vault namespace prefix under kv/ (default: temitayo)")
    p.add_argument("--vault-env", default="staging", help="Vault env segment (default: staging)")
    p.add_argument("--vault-repo", required=True, help="Vault repo segment (default: repo name, e.g. cila-health-microservices)")
    p.add_argument("--vault-service", required=True, help="Vault service segment (default: service name)")

    args = p.parse_args()

    if not TEMPLATE_DIR.exists():
        raise SystemExit(f"Template dir not found: {TEMPLATE_DIR}")

    dest = ROOT / "applications" / args.chart_dir
    if dest.exists():
        raise SystemExit(f"Chart already exists: {dest}")

    shutil.copytree(TEMPLATE_DIR, dest)

    mapping = {
        "__CHART_NAME__": args.chart_name,
        "__APP_NAME__": args.app_name,
        "__SERVICE_NAME__": args.service_name,
        "__IMAGE_REPO__": args.image_repo,
        "__HOSTNAME__": args.hostname,
        "__VAULT_NAMESPACE__": args.vault_namespace,
        "__VAULT_ENV__": args.vault_env,
        "__VAULT_REPO__": args.vault_repo,
        "__VAULT_SERVICE__": args.vault_service,
    }

    for f in dest.rglob("*"):
        if f.is_file():
            replace_in_file(f, mapping)

    print(f"Created chart: {dest}")


if __name__ == "__main__":
    main()

