# Belajar Kubernetes — From Local to AWS EKS

Portfolio belajar Kubernetes dari nol: lokal (Docker Desktop) hingga production-grade di AWS EKS.  
Dibuat sebagai bagian dari perjalanan kembali ke industri sebagai **SRE / Platform Engineer**.

---

## Tentang Repo Ini

Repo ini mendokumentasikan perjalanan belajar Kubernetes secara hands-on, mulai dari konsep dasar hingga deployment di cloud. Setiap fase punya portfolio checkpoint yang bisa dilihat sebagai bukti progres nyata.

**Stack yang digunakan:**

| Layer | Tool |
|---|---|
| Local cluster | kind (Kubernetes in Docker) |
| Container registry (lokal) | Docker Hub |
| Cloud cluster | AWS EKS |
| Cloud registry | AWS ECR |
| App | Python (FastAPI) |
| IaC | Terraform (fase akhir) |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus + Grafana |

---

## Roadmap Belajar

### Fase 1 — Docker Dulu Sebelum Kubernetes `[LOKAL]`
> Pastikan Docker solid sebelum masuk Kubernetes

- [ ] Docker Desktop terinstall & berjalan
- [ ] Review: image, container, port mapping, volume, network
- [ ] Buat `Dockerfile` untuk FastAPI sederhana
- [ ] Build & run image lokal
- [ ] Docker Compose — app + PostgreSQL
- [ ] Multi-stage build

**Checkpoint**: FastAPI + PostgreSQL via `docker compose up` ✓

---

### Fase 2 — Kubernetes Lokal: Konsep Dasar `[LOKAL]` ✅
> Paham core Kubernetes dengan hands-on

- [x] Enable Kubernetes — pakai kind cluster
- [x] Verifikasi: `kubectl cluster-info` & `kubectl get nodes`
- [x] Pod, Node, Cluster — bedanya dengan Docker container
- [x] Manifest YAML pertama: deploy Pod sederhana
- [x] Deployment & ReplicaSet
- [x] Service — NodePort + `kubectl port-forward`
- [x] Namespace — isolasi dev/staging
- [x] ConfigMap & Secret

**Checkpoint**: nginx di Kubernetes lokal — Deployment + Service + ConfigMap + Secret ✅

---

### Fase 3 — Kubernetes Lokal: Intermediate `[LOKAL]` 🔄
> Storage, health checks, autoscaling, observability

- [x] Persistent Volume & PVC
- [x] Liveness & readiness probe
- [x] Resource requests & limits
- [x] Ingress + Nginx Ingress Controller
- [ ] DNS di dalam cluster
- [ ] Horizontal Pod Autoscaler (HPA)
- [ ] DaemonSet & StatefulSet
- [ ] Metrics-server & `kubectl top`

**Checkpoint**: Stack lengkap — FastAPI + PostgreSQL (StatefulSet) + Ingress + HPA ✓

---

### Fase 4 — Monitoring & Helm `[LOKAL]`
> Monitor cluster + paket manifest dengan Helm

- [ ] Deploy Prometheus + Grafana (via Helm)
- [ ] Scrape metrics FastAPI (`/metrics` endpoint)
- [ ] Grafana dashboard sederhana
- [ ] Helm: install, upgrade, rollback
- [ ] Buat Helm chart sendiri
- [ ] Multi-environment: `values-dev.yaml`, `values-prod.yaml`

**Checkpoint**: Stack monitoring + Helm chart yang bisa deploy ke environment berbeda ✓

---

### Fase 5 — AWS EKS `[CLOUD — BERBAYAR]`
> Deploy cluster production-grade di cloud

> ⚠️ Estimasi biaya jika lupa dihapus: ~$4.44/hari. Hapus segera setelah selesai!

- [ ] Konsep EKS vs self-managed Kubernetes
- [ ] Buat EKS cluster (`eksctl`, node type `t3.small`)
- [ ] IAM roles & IRSA
- [ ] AWS Load Balancer Controller
- [ ] ECR — push & pull image
- [ ] EBS CSI Driver — persistent storage
- [ ] Cluster Autoscaler
- [ ] Secrets Manager + External Secrets Operator

**Checkpoint**: Stack FastAPI lengkap di EKS dengan ECR + ALB + EBS ✓

---

### Fase 6 — GitOps & CI/CD `[CLOUD]`
> Otomatisasi deployment seperti di perusahaan nyata

- [ ] GitHub Actions — build & push ke ECR otomatis
- [ ] CD pipeline ke EKS via GitHub Actions
- [ ] ArgoCD — GitOps
- [ ] Multi-environment pipeline (dev/staging/prod)

**Checkpoint**: Push kode → build image → deploy otomatis ✓

---

### Fase 7 — Infrastructure as Code (Terraform) `[CLOUD]`
> Semua infra reproducible dari kode

- [ ] Terraform dasar — resource, variable, output, state
- [ ] VPC dengan Terraform
- [ ] EKS cluster dengan Terraform
- [ ] Terraform modules
- [ ] State di S3 + DynamoDB locking
- [ ] Full stack: VPC + EKS + RDS via Terraform

**Checkpoint**: Satu repo Terraform — `terraform apply` buat semua, `terraform destroy` hapus semua ✓

---

## Struktur Repo

```
belajar-kubernetes/
├── README.md
├── .gitignore
└── k8s/                        # Manifest Kubernetes (Fase 2 & 3)
    ├── namespace.yaml           # Namespace: dev
    ├── configmap.yaml           # ConfigMap: env vars non-sensitif
    ├── secret.yaml.example      # Secret template (nilai asli jangan di-commit!)
    ├── deployment.yaml          # Deployment nginx — resource limits, probe, env injection
    ├── service.yaml             # Service NodePort
    └── pvc.yaml                 # PersistentVolumeClaim 100Mi
```

> Folder `helm/`, `monitoring/`, dan `terraform/` akan ditambahkan sesuai fase belajar.

---

## Setup Lokal

### Prasyarat

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) — Kubernetes in Docker
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/) — dibutuhkan mulai Fase 4

### Buat Cluster kind

```bash
kind create cluster --name belajar-k8s
```

### Deploy ke Cluster

```bash
# Apply semua manifest sekaligus
kubectl apply -f k8s/

# Verifikasi
kubectl get all -n dev

# Akses app di browser (port-forward karena kind tidak support NodePort langsung)
kubectl port-forward service/web-app-svc 8080:80 -n dev
# Buka: http://localhost:8080
```

### Verifikasi Cluster

```bash
kubectl cluster-info
kubectl get nodes

# Harus muncul satu node dengan status Ready
# NAME                       STATUS   ROLES           AGE
# belajar-k8s-control-plane  Ready    control-plane   ...
```

---

## Konvensi

- Semua manifest YAML harus punya **resource limits** dan **health checks**
- Jangan pernah pakai image tag `:latest` — pakai versi spesifik (`:v1.0.0`)
- Secret tidak boleh di-commit — pakai `secret.yaml.example` sebagai template
- Setiap folder fase punya README sendiri yang menjelaskan cara menjalankannya

---

## Lisensi

MIT License — bebas dipakai sebagai referensi belajar.
