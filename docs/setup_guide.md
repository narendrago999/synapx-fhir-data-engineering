# Setup Guide

1. Create a Fabric workspace and Lakehouse named lh_fhir.
2. Create/import notebooks under notebooks/ and attach lh_fhir as the default Lakehouse.
3. Ensure the notebook environment can import requests.
4. Run API validation against /metadata and each resource endpoint.
5. Verify _lastUpdated behaviour and pagination before full extraction.
6. Configure Lakehouse paths and pipeline parameters.

Do not commit credentials or tokens. The public HAPI endpoint does not require authentication.
