{{- define "monolith.name" -}}
{{- default .Chart.Name .Values.nameOverride -}}
{{- end -}}

{{- define "monolith.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- printf "%s" .Values.fullnameOverride }}
{{- else }}
{{- printf "%s-%s" (include "monolith.name" .) .Release.Name }}
{{- end }}
{{- end -}}