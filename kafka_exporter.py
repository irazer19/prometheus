from prometheus_client import start_http_server, Enum
import time
from confluent_kafka.admin import AdminClient

conf = {"bootstrap.servers": "172.31.27.25:9093"}
ac = AdminClient(conf)
sleep_time = 30

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    port = 9200
    start_http_server(port)
    scan_tools_enum = Enum(
        "scan-tools-consumers-state",
        "Scan tools Consumer Group State",
        states=["stable", "rebalance"],
    )

    conf = {"bootstrap.servers": "172.31.27.25:9093"}
    ac = AdminClient(conf)
    # Generate some requests.
    while True:
        groups = ac.describe_consumer_groups(group_ids=["trigger_group_prod"])
        group_desc = groups["trigger_group_prod"].result()
        curr_state = group_desc.state
        if "PREPARING_REBALANCING" in str(curr_state):
            scan_tools_enum.state("rebalance")
        else:
            scan_tools_enum.state("stable")
        time.sleep(sleep_time)
