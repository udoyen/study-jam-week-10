provider "google" {
  credentials = file("terraform-gke-keyfile.json")
  project     = var.project_id
  region      = var.region
  zone 				= var.zone
}
