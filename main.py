from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-14887d710e94d19063448b39c2945d9f"})

version = "1.0.3"
input_data = {
    "blog_topic": "Mira Learning",
    "content_type": "Education",
    "audience_requirements": "students"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@super-labs/blog-post-generator/{version}"
else:
    flow_name = "@super-labs/blog-post-generator"

result = client.flow.execute(flow_name, input_data)
print(result)