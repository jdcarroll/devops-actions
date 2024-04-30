from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def list_resource_groups():
    # Authenticate with default credentials
    credential = DefaultAzureCredential()
    
    # Create a client instance
    subscription_id = ''  # replace with your subscription ID
    client = ResourceManagementClient(credential, subscription_id)
    
    # List resource groups
    resource_groups = client.resource_groups.list()
    
    # Print resource group names
    for group in resource_groups:
        print(f"Resource Group: {group.name}")

if __name__ == "__main__":
    list_resource_groups()
