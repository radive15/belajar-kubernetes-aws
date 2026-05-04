# Belajar Kubernetes — From Local to AWS EKS

Portfolio belajar Kubernetes dari nol: lokal (Docker Desktop) hingga production-grade di AWS EKS.  
Dibuat sebagai bagian dari perjalanan kembali ke industri sebagai **SRE / Platform Engineer**.

---

## Tentang Repo Ini

Repo ini mendokumentasikan perjalanan belajar Kubernetes secara hands-on, mulai dari konsep dasar hingga deployment di cloud. Setiap fase punya portfolio checkpoint yang bisa dilihat sebagai bukti progres nyata.

**Stack yang digunakan:**

| Layer | Tool |
|---|---|
| Local cluster | Docker Desktop (Kubernetes built-in) |
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

### Fase 2 — Kubernetes Lokal: Konsep Dasar `[LOKAL]`
> Paham core Kubernetes dengan hands-on

- [ ] Enable Kubernetes di Docker Desktop
- [ ] Verifikasi: `kubectl cluster-info` & `kubectl get nodes`
- [ ] Pod, Node, Cluster — bedanya dengan Docker container
- [ ] Manifest YAML pertama: deploy Pod sederhana
- [ ] Deployment & ReplicaSet
- [ ] Service — ClusterIP, NodePort, LoadBalancer
- [ ] Namespace — isolasi dev/staging
- [ ] ConfigMap & Secret

**Checkpoint**: FastAPI di Kubernetes lokal — Deployment + Service + ConfigMap + Secret ✓

---

### Fase 3 — Kubernetes Lokal: Intermediate `[LOKAL]`
> Storage, health checks, autoscaling, observability

- [ ] Persistent Volume & PVC
- [ ] Liveness & readiness probe
- [ ] Resource requests & limits
- [ ] Ingress + Nginx Ingress Controller
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
├── fase-1-docker/          # Docker & Docker Compose
│   ├── app/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── docker-compose.yml
├── fase-2-k8s-dasar/       # Manifest Kubernetes dasar
│   └── k8s/
├── fase-3-k8s-intermediate/ # Storage, HPA, Ingress
│   └── k8s/
├── fase-4-helm-monitoring/  # Helm charts + Prometheus/Grafana
│   ├── helm/
│   └── monitoring/
├── fase-5-eks/             # EKS deployment
│   └── k8s/
├── fase-6-cicd/            # GitHub Actions + ArgoCD
│   └── .github/workflows/
└── fase-7-terraform/       # IaC
    └── terraform/
```

---

## Setup Lokal

### Prasyarat

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — aktifkan Kubernetes di Settings
- [kubectl](https://kubernetes.io/docs/tasks/tools/) — biasanya sudah terinstall bersama Docker Desktop
- [Helm](https://helm.sh/docs/intro/install/) — dibutuhkan mulai Fase 4

### Verifikasi Kubernetes Lokal

```bash
# Pastikan cluster berjalan
kubectl cluster-info
kubectl get nodes

# Harus muncul satu node dengan status Ready
# NAME             STATUS   ROLES           AGE
# docker-desktop   Ready    control-plane   ...
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
