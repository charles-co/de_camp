from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from etl_web_to_gcs import etl_web_to_gcs


github = GitHub.load("zoom-github")

github_dep = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="github-flow",
    infrastructure=github.get_directory("data_warehouse/flows/etl_web_to_gcs.py"),
    ignore_file="../.prefectignore",
    parameters={
        "color": "green",
        "month": 11,
        "year": 2020,
    }
)

if __name__ == "__main__":
    github_dep.apply()
