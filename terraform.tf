terraform {
	backend "gcs" {
		bucket			= "gke-state-bucket"
		prefix      = "terraform/state"
	}
}


