from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "sb-14887d710e94d19063448b39c2945d9f"})     # Initialize Mira Client
flow = CompoundFlow(source="configuration.yaml")           # Load flow configuration

test_input = {                                              # Prepare test inputs
    "prime_input_1": "test data",
    "prime_input_2": "test parameters"
}

try:
    response = client.flow.test(flow, test_input)           # Test entire pipeline
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))                           # Handle test failure
