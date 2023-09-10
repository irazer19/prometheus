from confluent_kafka.admin import AdminClient, ConsumerGroupDescription

conf = {'bootstrap.servers': '172.31.27.25:9093'}
ac = AdminClient(conf)
groups = ac.describe_consumer_groups(group_ids=['trigger_group_prod'])
group_desc = groups['trigger_group_prod'].result()
print(str(group_desc.state))
print(type(group_desc.state))
# group_state = group_desc._group_id
# print(group_state)
