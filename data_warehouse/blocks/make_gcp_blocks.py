from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
from prefect.filesystems import GitHub
from pathlib import Path


gcp_cred_path = Path(__file__).parent.parent.resolve() / "de-zoomcamp-375211-fe38ad3ca696.json"


credentials_block = GcpCredentials(
    service_account_path=gcp_cred_path
)
credentials_block.save("zoom-gcp-creds", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("zoom-gcp-creds"),
    bucket="de_zoom",
)

bucket_block.save("zoom-gcs", overwrite=True)

github_block = GitHub(
    repository="https://github.com/charles-co/de_camp",
)

github_block.save("zoom-github", overwrite=True)