{{- define "device-ingestion.name" -}}
{{- default .Chart.Name .Values.nameOverride -}}
{{- end -}}

{{- define "device-ingestion.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- printf "%s" .Values.fullnameOverride }}
{{- else }}
{{- printf "%s-%s" (include "device-ingestion.name" .) .Release.Name }}
{{- end }}
{{- end -}}